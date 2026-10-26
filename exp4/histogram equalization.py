import cv2  # Import the OpenCV computer vision library

# =========================================================================
# STEP 1: READ THE SOURCE IMAGE (Absolute Path Safeguard)
# =========================================================================
# Using the exact explicit system path to ensure VS Code runs it cleanly
input_path = "c:/collage/courses/ITA0517 COMPUTERVISION/LAB EXPERIMENTS CODES/exp2/sample_image.jpg"
original_image = cv2.imread(input_path)

# Validation check to ensure file integrity and path accuracy
if original_image is None:
    print(
        f"CRITICAL ERROR: Could not locate or read the image at: {input_path}"
    )
    print("Verify that your 'sample_image.jpg' file exists inside that folder.")
else:
    # =========================================================================
    # STEP 2: CONVERT TO GRAYSCALE & EQUALIZE HISTOGRAM
    # =========================================================================
    # Histogram equalization requires a single-channel 8-bit image to recalculate values
    gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

    # cv2.equalizeHist stretches the global contrast matrix across a full 0-255 range
    equalized_image = cv2.equalizeHist(gray_image)

    # =========================================================================
    # STEP 3: INITIALIZE RESIZABLE SCALING WINDOWS (Fix for Cut-Off Frames)
    # =========================================================================
    # Explicitly name the windows so they can be registered by the window manager
    window_original = "1. Original Grayscale Image"
    window_equalized = "2. Histogram Equalized Result"

    # Enforce WINDOW_NORMAL so windows dynamically adapt to your screen scale
    cv2.namedWindow(window_original, cv2.WINDOW_NORMAL)
    cv2.namedWindow(window_equalized, cv2.WINDOW_NORMAL)

    # =========================================================================
    # STEP 4: REAL-TIME COMPARISON DISPLAY INTERFACE
    # =========================================================================
    # Render both arrays to compare side-by-side
    cv2.imshow(window_original, gray_image)
    cv2.imshow(window_equalized, equalized_image)

    print("Windows loaded successfully! Scaling mechanics unlocked.")
    print(
        "REAL-TIME INPUT INSTRUCTION: Click inside an image window, then press ANY keyboard key to exit."
    )

    # =========================================================================
    # STEP 5: DESKTOP WAIT CYCLE AND RAM CLEANUP
    # =========================================================================
    # Freezes window termination until a hardware keyboard event is registered
    cv2.waitKey(0)

    # Destroys all open graphical windows to prevent VS Code memory locks
    cv2.destroyAllWindows()
