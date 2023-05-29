import numpy as np
from skimage import filters

def gaussian_impulse_response(sig, impulse_response_size):
    x = np.linspace(-impulse_response_size // 2, impulse_response_size // 2, impulse_response_size)
    y = np.exp(-(x ** 2) / (2 * sig ** 2))
    return y / np.sum(y)

class ImpulseResponseCallable:
    def __init__(self, sig, impulse_response_size):
        self.sig = sig
        self.impulse_response_size = impulse_response_size

    def __call__(self, *args, **kwargs):
        return gaussian_impulse_response(self.sig, self.impulse_response_size)

def apply_wiener_filter(img, sig):
    # Define Gaussian impulse response parameters
    impulse_response_size = (img.shape[0] + 1) * (img.shape[1] + 1)

    # Create an instance of the callable class with the desired parameters
    impulse_response_callable = ImpulseResponseCallable(sig, impulse_response_size)

    # Apply Wiener filtering with the callable impulse response
    rebuilt_image = filters.wiener(img, impulse_response_callable)

    return rebuilt_image
