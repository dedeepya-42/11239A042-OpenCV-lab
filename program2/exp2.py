import cv2

# Read image
img = cv2.imread(r"image.py")

# Check if image loaded successfully
if img is None:
    print("Error: Could not read the image. Check the file path or filename.")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Grayscale Image", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()