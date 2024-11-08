#click_image.py this program clicks the image
# of the text through the raspberry pi camera

import subprocess

def capture_image(filename="test_image.jpg"):
    try:
        # Use espeak to announce the start of the image capture process
        # This will provide an audio cue saying "Clicking picture"
        subprocess.run(["espeak", "Clicking picture"], check=True)

        # Capture image using libcamera-still command
        # The `-o` flag specifies the output filename for the image
        # `sudo` is used as libcamera-still may require root privileges
        subprocess.run(["sudo", "libcamera-still", "-o", filename], check=True)
        
        # Use espeak to announce the completion of the image capture
        # This will provide an audio cue saying "Picture clicked"
        subprocess.run(["espeak", "Picture clicked"], check=True)
        
        # Print a confirmation message in the console about the saved image
        print(f"Image captured and saved as {filename}")
    
    except subprocess.CalledProcessError as e:
        # If an error occurs during any of the subprocess calls, this block will be triggered
        print("Failed to capture image:", e)

# Call the capture function, specifying the filename for the saved image
capture_image("test_image.jpg")

