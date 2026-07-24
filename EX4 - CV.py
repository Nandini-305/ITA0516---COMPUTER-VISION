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

    # Apply dilation
    dilated = cv2.dilate(image, kernel, iterations=1)

    # Display dilated image
    cv2.imshow("Dilated Image", dilated)

    # Save output image
    cv2.imwrite("EX4 - CV.jpg", dilated)

