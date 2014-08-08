from SimpleCV import Camera, ImageSet
import time

cam = Camera()

camImages = ImageSet()

maxImages = 10

for i in range(maxImages):
    # Capture a new image
    img = cam.getImage()

    # Add image to set
    camImages.append(img)

    # Show the image and wait before capturing another
    img.show()
    time.sleep(1)

camImages.save(destination="./images/imagesets/")

