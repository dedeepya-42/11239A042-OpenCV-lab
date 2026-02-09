import cv2
import numpy as np

# Create a blank black image
img = np.zeros((500, 500, 3), dtype=np.uint8)

# Draw some shapes
cv2.rectangle(img, (50, 50), (200, 200), (0, 255, 0), -1)   # filled green rectangle
cv2.circle(img, (350, 150), 75, (255, 0, 0), -1)            # filled blue circle
cv2.line(img, (50, 300), (450, 300), (0, 0, 255), 5)        # red line

# Add text
cv2.putText(img, "OpenCV", (120, 450),
            cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 3)

# ---- Resize ----
resized = cv2.resize(img, (400, 300))

# ---- Convert to grayscale ----
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

# ---- Blur ----
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# ---- Edge detection ----
edges = cv2.Canny(blur, 100, 200)

# ---- Display ----
cv2.imshow("Original", img)
cv2.imshow("Resized", resized)
cv2.imshow("Gray", gray)
cv2.imshow("Blur", blur)
cv2.imshow("Edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()