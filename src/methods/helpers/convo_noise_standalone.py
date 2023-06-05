import numpy as np
from skimage import filters

def add_gaussian_noise(img, std_dev):
    # Generate the gaussian bruit with the same dimentions of the image
    noise = np.random.normal(0, std_dev, img.shape)
    # Add the bruit to the image
    noisy_image = img + noise
    # Ensures that the values are within the valid range [0, 1]
    noisy_image = np.clip(noisy_image, 0, 1)
    return noisy_image

def add_convolutional_noise(img, sig):
    #convolutional gaussian noise
    output = filters.gaussian(img, sigma=sig) 
    noisy_image = output + add_gaussian_noise(img, sig)
    return noisy_image