# EDGE-DETECTION
## Aim:
To perform edge detection using Sobel, Laplacian, and Canny edge detectors.

## Software Required:
Anaconda - Python 3.7

## Algorithm:
### Step1:
Import all the necessary modules for the program.

### Step2:
Load a image using imread() from cv2 module.

### Step3:
Convert the image to grayscale

### Step4:
Using Sobel operator from cv2,detect the edges of the image.

### Step5:

Using Laplacian operator from cv2,detect the edges of the image and Using Canny operator from cv2,detect the edges of the image.

## PROGRAM:
## Developed by: RAMYA R
## Register number: 21223230169
### SOBEL EDGE DETECTOR
```
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

```
### LAPLACIAN EDGE DETECTOR
```
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

```
### CANNY EDGE DETECTOR
```
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

```
## Output:
### SOBEL EDGE DETECTOR

![Screenshot 2024-09-30 161942](https://github.com/user-attachments/assets/86b425f2-f9a2-4a6c-907a-9d06f619cfb6)

![Screenshot 2024-09-30 161950](https://github.com/user-attachments/assets/8ac16e9a-89d9-4bb5-b1a7-1ee1747fb3b1)

![Screenshot 2024-09-30 161957](https://github.com/user-attachments/assets/7b377123-6fd5-4782-982d-b64f6ba3c8d8)

### LAPLACIAN EDGE DETECTOR
![Screenshot 2024-09-30 162003](https://github.com/user-attachments/assets/1ed96cb9-df34-46fc-993f-d8b8399d27df)


### CANNY EDGE DETECTOR
![Screenshot 2024-09-30 162254](https://github.com/user-attachments/assets/1fd79a58-c1d0-4b02-918a-464fff34c1bd)


## Result:
Thus the edges are detected using Sobel, Laplacian, and Canny edge detectors.
