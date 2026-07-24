import cv2
# Read image
image = cv2.imread("cv image.jpg")

# Check whether image is loaded
if image is None:
    print("Image not found!")
else:
    # Display original image
    cv2.imshow("Original Image", image)

    # Apply Gaussian Blur
    blur = cv2.GaussianBlur(image, (15, 15), 0)

    # Display blurred image
    cv2.imshow("Blurred Image", blur)

    # Save blurred image
    cv2.imwrite("EX2 - CV.jpg", blur)
