import os
import numpy as np
from PIL import Image

def add_noise(image, noise_level):
    """Add Gaussian noise to an image."""
    row, col, ch = image.shape
    mean = 0
    sigma = noise_level
    gauss = np.random.normal(mean, sigma, (row, col, ch))
    noisy = image + gauss
    noisy = np.clip(noisy, 0, 255)
    return noisy.astype(np.uint8)

def process_images(input_folder, output_folder, noise_level):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".png"):
            img_path = os.path.join(input_folder, filename)
            image = Image.open(img_path)
            image = np.array(image)
            noisy_image = add_noise(image, noise_level)
            noisy_image = Image.fromarray(noisy_image)
            noisy_image.save(os.path.join(output_folder, filename))

input_folder = '/data/liguanlin/codes/project212/TreeRecognition/datasets/DBS_noisy50/train/gt'
output_folder = '/data/liguanlin/codes/project212/TreeRecognition/datasets/DBS_noisy50/train/noisy'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
noise_level = 25

process_images(input_folder, output_folder, noise_level)
