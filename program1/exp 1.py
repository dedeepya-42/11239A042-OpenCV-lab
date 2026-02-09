import cv2

# Read image with absolute path or ensure it's in the same folder
img = cv2.imread(r"image.py")

# Check if image loaded successfully
if img is None:
    print("Error: Could not read the image. Check the file path or filename.")
    exit()

# Display image
cv2.imshow("Original Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()