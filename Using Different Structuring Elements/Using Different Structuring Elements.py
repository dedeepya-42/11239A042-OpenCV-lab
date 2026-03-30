import cv2

img = cv2.imread("image.jpg", 0)

# Prevent crash if image is not loaded
if img is None:
    print("Error: Image not found")
    exit()

# Create different structuring elements
kernel_rect = cv2.getStructuringElement(cv2.MORPH_RECT, (7,7))
kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7,7))
kernel_cross = cv2.getStructuringElement(cv2.MORPH_CROSS, (7,7))

# Apply erosion with each kernel
rect = cv2.erode(img, kernel_rect)
ellipse = cv2.erode(img, kernel_ellipse)
cross = cv2.erode(img, kernel_cross)

# Display results
cv2.imshow("Rect Kernel", rect)
cv2.imshow("Ellipse Kernel", ellipse)
cv2.imshow("Cross Kernel", cross)

cv2.waitKey(0)
cv2.destroyAllWindows()