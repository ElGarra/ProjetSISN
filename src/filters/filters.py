# from skimage import io, img_as_ubyte, data, restoration
# from skimage.filters import median, gaussian, laplace
# from scipy.signal import convolve2d
# import numpy as np
# import matplotlib.pyplot as plt

# def apply_filter(image, image_name):
#     print("####################################################################################################\n")
#     print(" --> Applying filters, please wait...'\n")
#     median_filter(image, image_name)
#     gauss_filter(image, image_name)
#     wiener_filter(image, image_name)
#     laplace_filter(image, image_name)

# def median_filter(image, image_name):
#     print(" --> Applying median filter'\n")
#     # Apply the median filter
#     filtered_image = median(image, footprint=None, out=None, mode='nearest', cval=0.0, behavior='ndimage')
#     # Create a mask to show the pixels map
#     mask = np.abs(image - filtered_image)
#     # Save the images
#     save_images(image, filtered_image, mask, image_name, "median", "mask")
#     # Plot the figure
#     fig, axes = plt.subplots(1, 3, figsize=(12, 4))
#     # Original image
#     axes[0].imshow(image, cmap='gray')
#     axes[0].set_title('Original image')
#     # Filtered image
#     axes[1].imshow(filtered_image, cmap='gray')
#     axes[1].set_title('Filtered image')
#     # Mask of the filter
#     axes[2].imshow(mask, cmap='gray')
#     axes[2].set_title('Mask')
#     # Plot parameters
#     plt.suptitle("Median filter", fontsize=16, color='black', ha='center')
#     plt.tight_layout()
#     # Show plot
#     plt.show()

# def gauss_filter(image, image_name):
#     print(" --> Applying low-pass filter'\n")
#     # Apply Low-bass filter
#     filtered_image = gaussian(image, sigma=3, mode='reflect')
#     filtered_image = np.uint8(filtered_image * 255)
#     # Create gaussian mask
#     mask = np.abs(image - filtered_image)
#     # Save the images
#     save_images(image, filtered_image, mask, image_name, "low-pass", "mask")
#     # Plot the figure
#     fig, axes = plt.subplots(1, 3, figsize=(12, 4))
#     # Original image
#     axes[0].imshow(image, cmap='gray')
#     axes[0].set_title('Original image')
#     # Filtered image
#     axes[1].imshow(filtered_image, cmap='gray')
#     axes[1].set_title('Filtered image')
#     # Mask of the filter
#     axes[2].imshow(mask, cmap='gray')
#     axes[2].set_title('Mask')
#     # Plot parameters
#     plt.suptitle("Low-pass filter", fontsize=16, color='black', ha='center')
#     plt.tight_layout()
#     # Show plot
#     plt.show()

# def wiener_filter(image, image_name):
#     print(" --> Applying Wiener filter'\n")
#     # Generate a fuzzy kernel (convolution)
#     kernel = np.ones((5, 5)) / 25
#     # Apply blur to the image
#     image_blur = convolve2d(image, kernel, mode='same', boundary='symm')
#     image_blur_adjusted = (image_blur * 255).astype(np.uint8)
#     # Apply the Wiener filter to deconvolve the image
#     image_deconv = restoration.wiener(image_blur, kernel, balance=0.1)
#     image_deconv_adjusted = (image_deconv * 255).astype(np.uint8)
#     # Save the images
#     save_images(image, image_deconv_adjusted, image_blur_adjusted, image_name, "Wiener", "blu")
#     # Plot the images
#     fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(12, 4))
#     ax = axes.ravel()
#     # Original image
#     ax[0].imshow(image, cmap='gray')
#     ax[0].set_title("Original image")
#     # Blurred image
#     ax[1].imshow(image_blur, cmap='gray')
#     ax[1].set_title("Blurred image")
#     # Deconvolved image
#     ax[2].imshow(image_deconv, cmap='gray')
#     ax[2].set_title("Deconvolved image (Wiener filter)")
#     # Plot parameters
#     plt.suptitle("Wiener filter", fontsize=16, color='black', ha='center')
#     plt.tight_layout()
#     # Plot show
#     plt.show()

# def laplace_filter(image, image_name):
#     print(" --> Applying Laplace filter'\n")
#     # Apply the laplace filter
#     filtered_image = laplace(image, ksize=15, mask=None)
#     filtered_image = np.uint8(filtered_image * 255)
#     # Create a mask to show the pixels map
#     mask = np.abs(image - filtered_image)
#     # Save the images
#     save_images(image, filtered_image, mask, image_name, "laplace", "mask")
#     # Plot the figure
#     fig, axes = plt.subplots(1, 3, figsize=(12, 4))
#     # Original image
#     axes[0].imshow(image, cmap='gray')
#     axes[0].set_title('Original image')
#     # Filtered image
#     axes[1].imshow(filtered_image, cmap='gray')
#     axes[1].set_title('Filtered image')
#     # Mask of the filter
#     axes[2].imshow(mask, cmap='gray')
#     axes[2].set_title('Mask')
#     # Plot parameters
#     plt.suptitle("Laplace filter", fontsize=16, color='black', ha='center')
#     plt.tight_layout()
#     # Show plot
#     plt.show()

# def save_images(image_1, image_2, image_3, image_name, filter, mask):
#     # Save the images
#     io.imsave(f'assets/{image_name}/{image_name}.png', image_1)
#     io.imsave(f'assets/{image_name}/{filter}_filtered_{image_name}.png', image_2)
#     io.imsave(f'assets/{image_name}/{filter}_{mask}_{image_name}.png', image_3)

   
