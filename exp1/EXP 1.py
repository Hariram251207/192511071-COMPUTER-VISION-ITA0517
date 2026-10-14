###Experiment 1: Read an Image and Convert It to Grayscale Using Python


import cv2
import matplotlib.pyplot as plt

# Step 1: Read the image
import os

folder = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(folder, "flower.jpg")
img = cv2.imread(image_path)

# Step 2: Check whether the image is loaded
if img is None:
    print("Error: Image not found!")
else:
    # Step 3: Convert the image to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Step 4: Display the original and grayscale images
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(gray_img, cmap="gray")
    plt.title("Grayscale Image")
    plt.axis("off")

    plt.show()

    # Step 5: Save the grayscale image
    cv2.imwrite("grayscale.jpg", gray_img)

    print("Image converted to grayscale successfully!")