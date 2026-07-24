import cv2

# Read image
image = cv2.imread("cv image.jpg")

# Check whether image is loaded
if image is None:
    print("Image not found!")
else:
    # Show original image
    cv2.imshow("Original Image", image)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Show grayscale image
    cv2.imshow("Grayscale Image", gray)

    # Save grayscale image
    cv2.imwrite("EX1- CV.jpg", gray)
