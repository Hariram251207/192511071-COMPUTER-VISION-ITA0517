import cv2
import numpy as np
import os

def perform_affine_transformation(image_path, output_path):
    # 1. Verify if the file exists at your absolute path
    if not os.path.exists(image_path):
        print(f"\n[ERROR] Input image not found at: '{image_path}'")
        print("Please verify that your 'sample' image is copied inside your 'ex13' folder.")
        return

    # 2. Read the input image
    image = cv2.imread(image_path)
    if image is None:
        print("[ERROR] Could not decode or load the image file format.")
        return

    # Get image dimensions (height and width)
    rows, cols, ch = image.shape

    # 3. Define 3 reference points from the input image
    # We take the top-left, top-right, and bottom-left coordinates
    points_src = np.float32([[50, 50], [cols - 100, 50], [50, rows - 100]])

    # 4. Define where those 3 points should move to in the output image
    # Shifting the coordinates creates a distinctive skewed/sheared warp effect
    points_dst = np.float32([[100, 100], [cols - 50, 150], [50, rows - 50]])

    # 5. Calculate the Affine Transformation Matrix
    matrix = cv2.getAffineTransform(points_src, points_dst)

    # 6. Apply the transformation warp to the image
    transformed_image = cv2.warpAffine(image, matrix, (cols, rows))

    # 7. Save the output image into the same folder
    success = cv2.imwrite(output_path, transformed_image)
    if success:
        print(f"[SUCCESS] Transformed image successfully saved as: '{output_path}'")
    else:
        print("[ERROR] Failed to save the transformed image file.")

    # 8. Resize both images so they fit nicely on your laptop screen
    screen_width, screen_height = 500, 400
    display_original = cv2.resize(image, (screen_width, screen_height))
    display_transformed = cv2.resize(transformed_image, (screen_width, screen_height))

    # 9. Display the original and transformed images side-by-side
    print("Displaying windows... Press any key inside the image windows to close.")
    cv2.imshow("Original Image", display_original)
    cv2.imshow("Affine Transformed Image", display_transformed)
    
    # Wait until a key is pressed, then release system windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # --- HARDFACED PATH SYSTEM FOR EX13 ---
    # Points directly to your ex13 folder as requested
    input_image = r"C:\collage\courses\ITA0517 COMPUTERVISION\LAB EXPERIMENTS CODES\exp13\sample.jpg"
    output_image = r"C:\collage\courses\ITA0517 COMPUTERVISION\LAB EXPERIMENTS CODES\exp13\affine_output.jpg"
    
    perform_affine_transformation(input_image, output_image)
