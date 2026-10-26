import cv2
import os

def perform_image_scaling(image_path):
    # 1. Verify if the file exists at your absolute path
    if not os.path.exists(image_path):
        print(f"\n[ERROR] Input image not found at: '{image_path}'")
        print("Please verify your file placement.")
        return

    # 2. Read the input image
    image = cv2.imread(image_path)
    if image is None:
        print("[ERROR] Could not decode or load the image file format.")
        return

    # -------------------------------------------------------------
    # STEP 3: Downscaling (Resizing to a smaller size)
    # -------------------------------------------------------------
    # cv2.INTER_AREA is recommended for shrinking to prevent pixel aliasing
    small_width, small_height = 400, 300
    scaled_smaller = cv2.resize(image, (small_width, small_height), interpolation=cv2.INTER_AREA)

    # -------------------------------------------------------------
    # STEP 4: Upscaling (Resizing to a bigger size)
    # -------------------------------------------------------------
    # cv2.INTER_CUBIC gives sharp, high-quality results when magnifying an image
    big_width, big_height = 1200, 900
    scaled_bigger = cv2.resize(image, (big_width, big_height), interpolation=cv2.INTER_CUBIC)

    # -------------------------------------------------------------
    # STEP 5: Displaying the scaled images
    # -------------------------------------------------------------
    print("Displaying windows... Press any key inside the image windows to close.")
    
    # We display the smaller version
    cv2.imshow("1. Scaled Down (Smaller - 400x300)", scaled_smaller)
    
    # We display the bigger version 
    cv2.imshow("2. Scaled Up (Bigger - 1200x900)", scaled_bigger)
    
    # Wait until a key is pressed, then release windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Image scaling transformations completed successfully.")

if __name__ == "__main__":
    # --- HARDFACED PATH SYSTEM ---
    # Reuses your verified sample file inside the exp8 directory
    input_image = r"C:\collage\courses\ITA0517 COMPUTERVISION\LAB EXPERIMENTS CODES\exp9\sample.jpg"
    
    perform_image_scaling(input_image)
