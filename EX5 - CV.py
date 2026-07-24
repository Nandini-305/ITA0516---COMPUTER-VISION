import cv2
import numpy as np



# Read image
image = cv2.imread("cv image.jpg")

# Check whether image is loaded
if image is None:
    print("Image not found!")
else:
    # Display original image
    cv2.imshow("Original Image", image)

    # Create kernel
    kernel = np.ones((5,5), np.uint8)

    # Apply erosion
    eroded = cv2.erode(image, kernel, iterations=1)

    # Display eroded image
    cv2.imshow("Eroded Image", eroded)

    # Save output image
    cv2.imwrite("EX5 - CV.jpg", eroded)
