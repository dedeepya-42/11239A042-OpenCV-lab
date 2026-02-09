import cv2

# Read image
img = cv2.imread(r"image.py")

# Check if image loaded successfully
if img is None:
    print("Error: Could not read the image. Check the file path or filename.")
    exit()

# Add text
cv2.putText(
    img,
    "OpenCV Lab",
    (50, 50),  # Position (x, y)
    cv2.FONT_HERSHEY_SIMPLEX,  # Font
    1,  # Font scale
    (0, 255, 0),  # Color (BGR) - Green
    2  # Thickness
)

# Display image
cv2.imshow("Image with Text", img)
cv2.waitKey(0)
cv2.destroyAllWindows()