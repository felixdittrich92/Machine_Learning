from skimage import io, exposure

image = io.imread("dragon.png")
io.imshow(image)
io.show()

print(image.shape)
image_brighter = image[:, :, :3] + 20
io.imshow(image_brighter)
io.show()

 # R G B A(Alpha)
image_without_alpha = image[:, :, :3]
image_brighter = image_without_alpha + 20
image_brighter[image_brighter < image_without_alpha] = 255
io.imshow(image_brighter)
io.show()