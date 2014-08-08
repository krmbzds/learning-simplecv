from SimpleCV import VirtualCamera

# Load an existing video into the virtual camera
vir = VirtualCamera("./videos/test.mp4", "video")

vir.live()

