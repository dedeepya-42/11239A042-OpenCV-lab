import cv2
import numpy as np

# Read image
img = cv2.imread("image.py")

# Check if image loaded successfully
if img is None:
    print("Error: Could not read the image.")
    exit()

# Resize (width=400, height=300)
resized = cv2.resize(img, (400, 300))

# Convert to grayscale
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

# Blur
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Edge detection
edges = cv2.Canny(blur, 100, 200)

# Display windows
cv2.imshow("Original", img)
cv2.imshow("Resized", resized)
cv2.imshow("Gray", gray)
cv2.imshow("Blur", blur)
cv2.imshow("Edges", edges)

# Wait for key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()