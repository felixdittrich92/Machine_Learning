import numpy as np
from skimage import io, exposure
from sklearn.cluster import KMeans

image = io.imread("dragon.png")[:, :, :3] # nur ersten 3 Werte RGB ohne Alpha
io.imshow(image)
io.show()

print(image.shape)
print(image.reshape(-1, 3)[0]) # Werte erste Pixel
image_reshaped = image.reshape(-1, 3)

model = KMeans(n_clusters = 32, n_init = 1) # nur 1 Durchlauf
model.fit(image_reshaped)

colors = model.cluster_centers_.astype("uint8") # konvertieren in Ganzzahl
pixels = model.labels_

# komprimiert speichern
np.savez_compressed("image.npz", pixels = pixels, colors = colors)
# laden
with np.load("image.npz") as file:
    pixels = file["pixels"]
    colors = file["colors"]

pixels_transformed = []
for pixel in pixels:
    pixels_transformed.append(colors[pixel])

pixels_transformed = np.array(pixels_transformed)
image_restored = pixels_transformed.reshape(900, 1200, 3)

io.imshow(image_restored)
io.show()