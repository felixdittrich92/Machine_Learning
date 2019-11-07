# Damit setzen wir das Working Directory auf den Ordner dieser Datei
if (!is.null(parent.frame(2)$ofile)) {
  this.dir <- dirname(parent.frame(2)$ofile)
  setwd(this.dir)
}

library(data.table)
library(ggplot2)
library(caret)

# http://yann.lecun.com/exdb/mnist/
read.mnist <- function(file.data, file.labels) {
  data.file <- gzfile(file.data , "rb")
  readBin(data.file, "int", n = 1, size = 4)
  dims <- readBin(data.file, "int", n = 3, size = 4, endian = "big")
  data.bin <- readBin(data.file, "int", n = dims[1] * dims[2] * dims[3], size = 1, signed = FALSE, endian = "big")
  data <- matrix(data.bin, ncol = dims[2] * dims[3], byrow = TRUE)
  close(data.file)
  
  label.file <- gzfile(file.labels , "rb")
  readBin(label.file, "int", n = 1, size = 4, endian = "big")
  size <- readBin(label.file, "int", n = 1, size = 4, endian = "big")
  if (size != dims[1]) {
    stop("Label file doesn't match data file")
  }
  labels <- readBin(label.file, "int", n = dims[1], size = 1, endian = "big", signed = FALSE)
  close(label.file)
  
  return(list(data = data, labels = labels))
}

train <- read.mnist(
  "train-images-idx3-ubyte.gz", 
  "train-labels-idx1-ubyte.gz"
)

test <- read.mnist(
  "t10k-images-idx3-ubyte.gz", 
  "t10k-labels-idx1-ubyte.gz"
)

# print(train$labels[2])
# plot(as.raster(matrix(train$data[2, ], ncol = 28, byrow = TRUE) / 256))

train.data <- data.table(train$data)
train.data$label <- train$labels == 5

model <- glm(label ~ ., data = train.data[1:1000, ], family = binomial())
print(model)

test.data <- data.table(test$data)
test.data$label <- test$labels == 5

pred <- predict(model, test.data, type = "response")
print(confusionMatrix(pred > 0.5, test.data$label)$overall["Accuracy"])
