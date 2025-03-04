from PIL import Image
import matplotlib.pyplot as plt
import cv2
import numpy as np

# Load the images
image_path_0 = "/home/malithjkd/Documents/pi_camera_data/camera0.jpg"
image_path_1 = "/home/malithjkd/Documents/pi_camera_data/camera1.jpg"

image_0 = cv2.imread(image_path_0, cv2.IMREAD_GRAYSCALE)
image_1 = cv2.imread(image_path_1, cv2.IMREAD_GRAYSCALE)

# Compute the disparity map
stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
disparity = stereo.compute(image_0, image_1)

# Normalize the disparity map for visualization
disparity_normalized = cv2.normalize(disparity, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
disparity_normalized = np.uint8(disparity_normalized)

# Display the disparity map
plt.imshow(disparity_normalized, cmap='gray')
plt.axis('off')  # Hide the axis
plt.show()

# Calculate the depth map
focal_length = 1.0  # Example focal length in pixels
baseline = 0.083  # Example baseline in meters
depth_map = (focal_length * baseline) / (disparity + 1e-6)  # Add a small value to avoid division by zero

# Clip the depth map to a specific range (e.g., 1 to 3 meters)
depth_map = np.clip(depth_map, 1, 3)

# Display the depth map
plt.imshow(depth_map, cmap='jet')
plt.colorbar(label='Depth (meters)')
plt.axis('off')  # Hide the axis
plt.show()