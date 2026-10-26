import cv2  # Import the OpenCV library

# =========================================================================
# STEP 1: READ THE INPUT IMAGE
# =========================================================================
# 'input_path' tells the program exactly where to look on your computer.
# Replace 'sample_image.jpg' with the actual path to your picture.
input_path = "c:/collage/courses/ITA0517 COMPUTERVISION/LAB EXPERIMENTS CODES/exp2/sample_image.jpg"

original_image = cv2.imread(input_path)

# Verify that the image loaded successfully to avoid running errors
if original_image is None:
    print(
        f"Error: Could not load the image from '{input_path}'. Check the path!"
    )
else:
    # =========================================================================
    # STEP 2: APPLY GAUSSIAN BLUR PROCESS
    # =========================================================================
    # Define the kernel width and height (must be odd numbers).
    # (15, 15) provides a moderate, visually distinct blurring effect.
    kernel_size = (15, 15)

    # cv2.GaussianBlur takes: (source_image, kernel_size, sigmaX)
    # Setting sigmaX (standard deviation) to 0 lets OpenCV auto-calculate it based on kernel size.
    blurred_image = cv2.GaussianBlur(original_image, kernel_size, 0)

    # =========================================================================
    # STEP 3: DISPLAY RESULTS (REAL-TIME OUTPUT INTERFACE)
    # =========================================================================
    # cv2.imshow opens graphic windows to display the matrices visually.
    cv2.imshow("1. Original Image Window", original_image)
    cv2.imshow("2. Gaussian Blurred Image Window", blurred_image)

    print("Windows opened! Press ANY key on your keyboard to close them.")

    # =========================================================================
    # STEP 4: MEMORY CLEAN-UP
    # =========================================================================
    # cv2.waitKey(0) pauses execution indefinitely until the user strikes a key.
    # If omitted, windows would instantly crash open and shut in milliseconds.
    cv2.waitKey(0)

    # Safely clears the GUI windows out of your operating system's active memory.
    cv2.destroyAllWindows()
