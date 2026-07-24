import cv2

# Read image
image = cv2.imread("cv image.jpg")

# Check whether image is loaded
if image is None:
    print("Image not found!")
else:
    # Display original image
    cv2.imshow("Original Image", image)

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny Edge Detection
    edges = cv2.Canny(gray, 100, 200)

    # Display edge image
    cv2.imshow("Canny Edge Image", edges)

    # Save edge image
    cv2.imwrite("EX3 - CV.jpg", edges)

