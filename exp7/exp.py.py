import cv2
import os

def play_video_at_different_speeds(video_path):
    # Check if your video file actually exists in the folder
    if not os.path.exists(video_path):
        print(f"\n[ERROR] The video file was not found at: '{video_path}'")
        print("Please ensure your video file is saved inside your 'exp7' folder and named exactly 'my_video.mp4'.\n")
        return

    # Define our three speed stages (measured in milliseconds of delay)
    # Normal ~ 30ms delay (~33 FPS)
    # Slow Motion ~ 120ms delay (4x slower)
    # Fast Motion ~ 5ms delay (6x faster)
    modes = [
        {"name": "Normal Motion", "delay": 30},
        {"name": "Slow Motion (4x Slower)", "delay": 120},
        {"name": "Fast Motion (6x Faster)", "delay": 5}
    ]

    # Run through each playback speed sequentially
    for mode in modes:
        # Initialize video reader stream
        cap = cv2.VideoCapture(video_path)
        print(f"Now playing: {mode['name']}. (Press 'q' to skip to next speed mode)")
        
        while cap.isOpened():
            ret, frame = cap.read()
            
            # If ret is False, the video has reached its end frame
            if not ret:
                break
                
            # Overlay the current speed mode banner onto the image
            cv2.putText(frame, f"Mode: {mode['name']}", (30, 50), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 255), 2)
            
            # Render the frame to the output monitor window
            cv2.imshow("Experiment 7 - Video Processing", frame)
            
            # The waitKey delay alters execution loop speed directly
            if cv2.waitKey(mode['delay']) & 0xFF == ord('q'):
                print(f"Skipped {mode['name']}")
                break
                
        # Close the stream reader before opening it for the next round
        cap.release()
        
    cv2.destroyAllWindows()
    print("All speed simulation modes completed successfully.")

if __name__ == "__main__":
    # --- AUTOMATED CONFIGURATION ---
    # Automatically finds the absolute directory path where this script file lives
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Joins the script path cleanly with your video name
    input_video = os.path.join(script_dir, "my_video.mp4")
    
    # Run the function
    play_video_at_different_speeds(input_video)
