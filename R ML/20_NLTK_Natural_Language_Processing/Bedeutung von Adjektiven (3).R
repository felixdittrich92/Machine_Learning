# Damit setzen wir das Working Directory auf den Ordner dieser Datei
if (!is.null(parent.frame(2)$ofile)) {
  this.dir <- dirname(parent.frame(2)$ofile)
  setwd(this.dir)
}

# Sicherstellen, dass alle Pakete korrekt geladen werden, etc. 
source("Installation.R", echo = FALSE)

######################################################################

library(data.table)
library(RDRPOSTagger)
library(caret)

reviews <- fread("Reviews_10000.csv", encoding = "UTF-8")
tagger <- rdr_model(language = "English", annotation = "POS")

pb <- txtProgressBar(min = 0, max = nrow(reviews))

# adj <- sapply(reviews$Text, function(text) {
#   pb.value <- getTxtProgressBar(pb) + 1
#   setTxtProgressBar(pb, pb.value)
#   # print(paste(pb.value, text, sep = ": "))
#
#   res <- tryCatch({
#     tagged <- rdr_pos(tagger, text)
#     paste(tagged[tagged$pos == "JJ", "token"], collapse = " ")
#   }, error = function(err) {
#     return("")
#   })
#   return(res)
# })
# close(pb)
# saveRDS(adj, "Reviews_10000_adj.rds")

adj <- readRDS("Reviews_10000_adj.rds")

library(naivebayes)
library(tm)

corpus <- Corpus(VectorSource(adj))
print(corpus)

freq <- findFreqTerms(DocumentTermMatrix(corpus), lowfreq = 200)
print(freq)

dtm <- DocumentTermMatrix(corpus, control = list(dictionary = freq))
dtm.prepared <- as.matrix(dtm > 0)

model <- naive_bayes(dtm.prepared, as.numeric(reviews$Score >= 4))
words <- names(model$tables)

res <- sapply(words, function(word) {
  table <- model$tables[[word]]
  score <- table[2, 1] / table[2, 2]
  return(score)
})
res <- sort(res)
print(res)
