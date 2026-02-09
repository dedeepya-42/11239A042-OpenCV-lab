import cv2
import numpy as np

# Read image in grayscale with absolute path
img = cv2.imread(r"image.py", 0)

# Check if image loaded successfully
if img is None:
    print("Error: Could not read the image. Check the file path.")
    exit()

# Binary Thresholding
_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Structuring Element (Kernel)
kernel = np.ones((5, 5), np.uint8)

# Erosion
erosion = cv2.erode(binary, kernel, iterations=1)

# Dilation
dilation = cv2.dilate(binary, kernel, iterations=1)

# Opening (Erosion followed by Dilation)
opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)

# Closing (Dilation followed by Erosion)
closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

# Display Results
cv2.imshow("Original Image", img)
cv2.imshow("Binary Image", binary)
cv2.imshow("Erosion", erosion)
cv2.imshow("Dilation", dilation)
cv2.imshow("Opening", opening)
cv2.imshow("Closing", closing)

cv2.waitKey(0)
cv2.destroyAllWindows()