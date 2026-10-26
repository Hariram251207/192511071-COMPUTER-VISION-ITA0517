import cv2
import os

def rotate_image_90_clockwise(image_path):
    # 1. Verify if the file exists at your absolute path
    if not os.path.exists(image_path):
        print(f"\n[ERROR] Input image not found at: '{image_path}'")
        print("Please verify that your 'sample' image is copied inside your 'exp10' folder.")
        return

    # 2. Read the input image
    image = cv2.imread(image_path)
    if image is None:
        print("[ERROR] Could not decode or load the image file format.")
        return

    # 3. Perform a 90-degree clockwise rotation
    # cv2.ROTATE_90_CLOCKWISE turns the image 90 degrees to the right
    rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

    # 4. Resize both images so they fit nicely on your laptop screen without being cut off
    screen_width, screen_height = 500, 400
    display_original = cv2.resize(image, (screen_width, screen_height))
    # For the rotated image, swap width and height so the aspect ratio stays natural
    display_rotated = cv2.resize(rotated_image, (screen_height, screen_width))

    # 5. Display the original and rotated images
    print("Displaying windows... Press any key inside the image windows to close.")
    cv2.imshow("Original Image", display_original)
    cv2.imshow("90-Degree Clockwise Rotated", display_rotated)
    
    # Wait until a key is pressed, then release system windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Image rotation completed successfully.")

if __name__ == "__main__":
    # --- HARDFACED PATH SYSTEM FOR EXP10 ---
    # Points directly to the file named 'sample.jpg' inside your new exp10 folder
    input_image = r"C:\collage\courses\ITA0517 COMPUTERVISION\LAB EXPERIMENTS CODES\exp10\sample.jpg"
    
    rotate_image_90_clockwise(input_image)
