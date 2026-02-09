import cv2

# Read image
img = cv2.imread(r"image.py")

# Check if image loaded successfully
if img is None:
    print("Error: Could not read the image. Check the file path or filename.")
    exit()

# Image properties
height, width, channels = img.shape
size = img.size
datatype = img.dtype

print("Width :", width)
print("Height :", height)
print("Channels :", channels)
print("Image Size :", size)
print("Data Type :", datatype)