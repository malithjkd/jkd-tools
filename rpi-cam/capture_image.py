import subprocess
import time

def capture_image(filename):
    # Use libcamera-still to capture an image

    command = ['libcamera-still', '--immediate', '-o', filename]
    
    try:
        # Run the command and capture the image
        subprocess.run(command, check=True)
        print(f"Image saved as {filename}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
