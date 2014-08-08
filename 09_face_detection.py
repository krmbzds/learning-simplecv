from SimpleCV import Image, Camera, Display
import time

camera = Camera()
display = Display(camera.getImage().size())

counter = 0
while display.isNotDone():

    img = camera.getImage()

    faces = img.findHaarFeatures('face_cv2.xml') # Look for faces

    if faces is not None:
        try:
            counter += 1
            face = faces.sortArea()[-1] # Get the largest face
            face.draw() # Draw a rectangle around the face

            img.save("./images/faces/image-" + str(counter) + ".jpg")

            time.sleep(1)

        except IndexError:
            pass

    img.save(display)
