import cv2
import numpy as np

# Create a blank image (example: white canvas)
img = np.ones((500, 500, 3), dtype=np.uint8) * 255

# Safety check
if img is None:
    print("Error: Image not available!")
else:
    # Save in multiple formats
    cv2.imwrite("output.jpg", img)
    cv2.imwrite("output.png", img)
    cv2.imwrite("output.bmp", img)
    cv2.imwrite("output.tif", img)

    print("Image converted and saved as:")
    print("output.jpg, output.png, output.bmp, output.tif")