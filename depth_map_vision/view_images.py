# view images from folder location 

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the images
image_folder = "/home/malithjkd/Documents/pi_camera_data/"
image_path_0 = os.path.join(image_folder, "camera0.jpg")
image_path_1 = os.path.join(image_folder, "camera1.jpg")

image_0 = cv2.imread(image_path_0, cv2.IMREAD_GRAYSCALE)
image_1 = cv2.imread(image_path_1, cv2.IMREAD_GRAYSCALE)

# Display the first image
plt.figure(figsize=(5, 5))
plt.imshow(image_0, cmap='gray')
plt.title('Left Image')
plt.axis('off')  # Hide the axis
plt.show()

# Display the second image
plt.figure(figsize=(5, 5))
plt.imshow(image_1, cmap='gray')
plt.title('Right Image')
plt.axis('off')  # Hide the axis
plt.show()
