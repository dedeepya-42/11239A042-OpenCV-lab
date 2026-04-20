import cv2
import pytesseract

# Set Tesseract path (important for Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Read image
img = cv2.imread("input.jpg")

# Check if image loaded
if img is None:
    print("Image not found")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply threshold
thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1]

# OCR
text = pytesseract.image_to_string(thresh)

print("Detected Text:")
print(text)

# Show images
cv2.imshow("Original", img)
cv2.imshow("Processed", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()