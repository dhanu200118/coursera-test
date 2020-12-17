from PIL import Image

im = Image.open("flywheel.jpg")
im.rotate(45).show()
