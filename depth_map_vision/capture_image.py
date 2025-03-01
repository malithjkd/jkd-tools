import subprocess

def capture_image(filename, camera_id):
    command = ['libcamera-still', '--immediate', '-o', filename, '--camera', str(camera_id)]
    try:
        subprocess.run(command, check=True)
        print(f"Image from camera {camera_id} saved as {filename}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred for camera {camera_id}: {e}")

# Capture images from both cameras
capture_image("camera0.jpg", 0)
capture_image("camera1.jpg", 1)
