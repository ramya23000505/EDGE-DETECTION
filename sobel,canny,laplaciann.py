import cv2
import matplotlib.pyplot as plt

# Read the image using imread
img = cv2.imread('cartoon_6.jpg')  # Replace with your image path
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert the image to grayscale
gray = cv2.GaussianBlur(gray, (3, 3), 0)  # Apply Gaussian Blur

# Sobel X axis
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.imshow(gray, cmap='gray')
plt.title("Original Image")
plt.axis("off")
plt.subplot(1, 2, 2)
plt.imshow(sobelx, cmap='gray')
plt.title("Sobel X axis")
plt.axis("off")
plt.show()

# Sobel Y axis
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)  # Sobel for Y axis
plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.imshow(gray, cmap='gray')
plt.title("Original Image")
plt.axis("off")
plt.subplot(1, 2, 2)
plt.imshow(sobely, cmap='gray')
plt.title("Sobel Y axis")
plt.axis("off")
plt.show()

# Sobel XY axis
sobelxy = cv2.Sobel(gray, cv2.CV_64F, 1, 1, ksize=5)
plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.imshow(gray, cmap='gray')
plt.title("Original Image")
plt.axis("off")
plt.subplot(1, 2, 2)
plt.imshow(sobelxy, cmap='gray')  # Display Sobel XY result
plt.title("Sobel XY axis")
plt.axis("off")
plt.show()

# Laplacian Edge Detector
lap = cv2.Laplacian(gray, cv2.CV_64F)
plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.imshow(gray, cmap='gray')
plt.title("Original Image")
plt.axis("off")
plt.subplot(1, 2, 2)
plt.imshow(lap, cmap='gray')  # Display Laplacian result
plt.title("Laplacian Edge Detector")
plt.axis("off")
plt.show()

# Canny Edge Detector
canny = cv2.Canny(gray, 120, 150)
plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.imshow(gray, cmap='gray')
plt.title("Original Image")
plt.axis("off")
plt.subplot(1, 2, 2)
plt.imshow(canny, cmap='gray')  # Display Canny result
plt.title("Canny Edge Detector")
plt.axis("off")
plt.show()
