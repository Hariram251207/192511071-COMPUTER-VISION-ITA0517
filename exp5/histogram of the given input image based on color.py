import cv2
import matplotlib.pyplot as plt
import os

def analyze_color_histogram(image_path):
    """
    Analyzes and plots the color histogram (Blue, Green, Red) of an input image.
    """
    # 1. Check if the file exists
    if not os.path.exists(image_path):
        print(f"Error: The image file was not found at '{image_path}'.")
        print("Please check the path and filename.")
        return

    # 2. Load the image using OpenCV
    # OpenCV loads images in BGR format by default
    image = cv2.imread(image_path)
    
    if image is None:
        print("Error: Could not open or read the image.")
        return

    # 3. Split the image into its Blue, Green, and Red channels
    channels = cv2.split(image)
    colors = ('b', 'g', 'r')
    channel_names = ('Blue Channel', 'Green Channel', 'Red Channel')
    
    # 4. Set up the matplotlib plot
    plt.figure(figsize=(10, 5))
    plt.title('Color Histogram Analysis')
    plt.xlabel('Color Level (0 - 255)')
    plt.ylabel('Number of Pixels')

    # 5. Calculate and plot the histogram for each channel
    # cv2.calcHist(images, channels, mask, histSize, ranges)
    for channel, color, name in zip(channels, colors, channel_names):
        hist = cv2.calcHist([channel], [0], None, [256], [0, 256])
        plt.plot(hist, color=color, label=name, linewidth=2)
        plt.xlim([0, 256])

    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

# --- Execution ---
if __name__ == "__main__":
    # Provide the path to your input image here
    input_image_path = "sample_image.jpg" 
    
    analyze_color_histogram(input_image_path)
