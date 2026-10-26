import cv2
import numpy as np
import os

def perform_image_dilation(image_path):
    # 1. Verify if the file exists
    if not os.path.exists(image_path):
        print(f"\n[ERROR] Input image not found at: '{image_path}'")
        return

    # 2. Read the input image
    image = cv2.imread(image_path)
    if image is None:
        print("[ERROR] Could not decode or load the image file format.")
        return

    # 3. Create a structuring element (Kernel) for Dilation
    kernel = np.ones((5, 5), np.uint8)

    # 4. Apply the dilation operation
    dilated_image = cv2.dilate(image, kernel, iterations=1)

    # 5. NEW STEP: Resize both images so they fit perfectly on your laptop screen
    # (Width = 600 pixels, Height = 400 pixels)
    screen_width, screen_height = 600, 400
    display_original = cv2.resize(image, (screen_width, screen_height))
    display_dilated = cv2.resize(dilated_image, (screen_width, screen_height))

    # 6. Display the resized windows side-by-side
    print("Displaying images... Press 'q' or any key inside the window to close.")
    cv2.imshow("Original Image (Resized)", display_original)
    cv2.imshow("Dilated Image (Processed & Resized)", display_dilated)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Dilation operation completed successfully.")

if __name__ == "__main__":
    # Absolute path targeting your verified sample file
    input_image = r"C:\collage\courses\ITA0517 COMPUTERVISION\LAB EXPERIMENTS CODES\exp8\sample.jpg"
    
    perform_image_dilation(input_image)
