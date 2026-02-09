import cv2

# Read image with absolute path or ensure it's in the same folder
img = cv2.imread(r"image.py")

# Check if image loaded successfully
if img is None:
    print("Error: Could not read the image. Check the file path or filename.")
    exit()

# Convert to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Display
cv2.imshow("Original Image", img)
cv2.imshow("HSV Image", hsv)

cv2.waitKey(0)
cv2.destroyAllWindows()