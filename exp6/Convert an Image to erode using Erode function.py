import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# 1. Dynamically get the absolute folder path where this script lives
script_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Try loading as JPG/JPEG (which matches your image file icon type)
img_path = os.path.join(script_dir, 'flower.jpg')
bgr_image = cv2.imread(img_path)

# Fallback: If it's a jpeg or png extension instead
if bgr_image is None:
    img_path = os.path.join(script_dir, 'flower.jpeg')
    bgr_image = cv2.imread(img_path)
if bgr_image is None:
    img_path = os.path.join(script_dir, 'flower.png')
    bgr_image = cv2.imread(img_path)

# 3. Verify and run processing operations
if bgr_image is None:
    print(f"Error: Could not locate 'flower' image file inside: {script_dir}")
else:
    # ----------------------------------------------------
    # EXECUTION 1: Color Histogram Analysis
    # ----------------------------------------------------
    plt.figure(figsize=(12, 4))
    
    plt.subplot(1, 3, 1)
    colors = ('b', 'g', 'r')
    labels = ('Blue Channel', 'Green Channel', 'Red Channel')
    for i, (col, lab) in enumerate(zip(colors, labels)):
        hist = cv2.calcHist([bgr_image], [i], None, [256], [0, 256])
        plt.plot(hist, color=col, label=lab)
    plt.title('1. Color Distribution')
    plt.xlabel('Intensity Value')
    plt.ylabel('Pixel Count')
    plt.legend()
    plt.grid(True, alpha=0.3)

    # ----------------------------------------------------
    # EXECUTION 2: Grayscale and Erosion Process
    # ----------------------------------------------------
    gray_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((5, 5), np.uint8)
    eroded_image = cv2.erode(gray_image, kernel, iterations=1)

    plt.subplot(1, 3, 2)
    plt.imshow(gray_image, cmap='gray')
    plt.title('2. Original Grayscale')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(eroded_image, cmap='gray')
    plt.title('3. Eroded Result (5x5)')
    plt.axis('off')

    plt.tight_layout()
    plt.show()
