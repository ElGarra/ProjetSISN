import numpy as np
import matplotlib.pyplot as plt
from skimage import io, metrics, img_as_float, filters, data
from .helpers.convo_noise_standalone import add_convolutional_noise
from .helpers.wiener_only import apply_wiener_filter
from .helpers.gaussian_noise import add_gaussian_noise

def normalize_columns(array):
    min_vals = np.min(array, axis=0)
    max_vals = np.max(array, axis=0)
    if max_vals == min_vals:
        normalized_array = array
    else:
        normalized_array = (array - min_vals) / (max_vals - min_vals)
                                                 
    return normalized_array

def average_difference(arr1, arr2):
    if len(arr1) != len(arr2):
        raise ValueError("Arrays must have the same length")
    if len(arr1) == 0:
        return 0  # Return 0 for empty arrays or handle it differently as per your requirement
    diff = [abs(a - b) for a, b in zip(arr1, arr2)]
    average = sum(diff) / len(diff)
    return average



class analyse():
    def __init__(self, img, norm, log):
        self.image = img_as_float(img)
        self.images = [None] * 2
        self.ssim = np.empty((20,4))
        self.mse = np.empty((20,4))
        self.psnr = np.empty((20,4))
        self.nmi = np.empty((20,4))
        self.std_dev = np.linspace(0.01,0.5,20)
        self.normalise = norm
        self.averageImprovement = [None] * 2
        self.log = log
    
    def calculate_values(self):
        for i in range(len(self.std_dev)):
            #calculate data for gaussian convolutional noise and wiener filter
            self.noisy_image = add_convolutional_noise(self.image, self.std_dev[i])
            self.reconstructed_image = np.nan_to_num(apply_wiener_filter(self.noisy_image, self.std_dev[i]))

            #calculate all the mesures with the original and the noisy image
            self.ssim[i][0] = metrics.structural_similarity(self.image, self.noisy_image, multichannel=True, data_range=self.noisy_image.max() - self.noisy_image.min())
            self.mse[i][0] = np.nan_to_num(metrics.mean_squared_error(self.image, self.noisy_image))
            self.psnr[i][0] = np.nan_to_num(metrics.peak_signal_noise_ratio(self.image, self.noisy_image))
            self.nmi[i][0] = np.nan_to_num(metrics.normalized_mutual_information(self.image, self.noisy_image))

            #calculate all the mesures with the original and the reconstructed image
            self.ssim[i][1] = metrics.structural_similarity(self.image, self.reconstructed_image, multichannel=True, data_range=self.noisy_image.max() - self.noisy_image.min())
            self.mse[i][1] = np.nan_to_num(metrics.mean_squared_error(self.image, self.reconstructed_image))
            self.psnr[i][1] = np.nan_to_num(metrics.peak_signal_noise_ratio(self.image, self.reconstructed_image))
            self.nmi[i][1] = np.nan_to_num(metrics.normalized_mutual_information(self.image, self.reconstructed_image))

            #calculate data for gaussian additive noise and median filter
            self.noisy_image = add_gaussian_noise(self.image, self.std_dev[i])
            self.reconstructed_image = np.nan_to_num(filters.median(self.image, footprint=None, out=None, mode='nearest', cval=0.0, behavior='ndimage'))
            #calculate all the mesures with the original and the noisy image
            self.ssim[i][2] = metrics.structural_similarity(self.image, self.noisy_image, multichannel=True, data_range=self.noisy_image.max() - self.noisy_image.min())
            self.mse[i][2] = np.nan_to_num(metrics.mean_squared_error(self.image, self.noisy_image))
            self.psnr[i][2] = np.nan_to_num(metrics.peak_signal_noise_ratio(self.image, self.noisy_image))
            self.nmi[i][2] = np.nan_to_num(metrics.normalized_mutual_information(self.image, self.noisy_image))

            #calculate all the mesures with the original and the reconstructed image
            self.ssim[i][3] = metrics.structural_similarity(self.image, self.reconstructed_image, multichannel=True, data_range=self.noisy_image.max() - self.noisy_image.min())
            self.mse[i][3] = np.nan_to_num(metrics.mean_squared_error(self.image, self.reconstructed_image))
            self.psnr[i][3] = np.nan_to_num(metrics.peak_signal_noise_ratio(self.image, self.reconstructed_image))
            self.nmi[i][3] = np.nan_to_num(metrics.normalized_mutual_information(self.image, self.reconstructed_image))
        
        #average
        self.averageImprovement[0] = average_difference(self.psnr[:,1], self.psnr[:,0])
        self.averageImprovement[1] = average_difference(self.psnr[:,3], self.psnr[:,2])

        #normalise
        if self.normalise == 1:
            for i in range(4):
                self.ssim[:,i] = normalize_columns(self.ssim[:,i])
                self.mse[:,i] = normalize_columns(self.mse[:,i])
                self.psnr[:,i] = normalize_columns(self.psnr[:,i])
                self.nmi[:,i] = normalize_columns(self.nmi[:,i])

        if self.log == 1: 
            self.ssim = np.log10(self.ssim)
            self.mse = np.log10(self.mse)
            self.psnr = np.log10(self.psnr)
            self.nmi = np.log10(self.nmi)

    def plot_graph(self):
        titles = ['Convolutional and Additive Noise recontructed with a Wiener Filter', 
                  'Additive Gaussian Noise reconstructed with Median Filter']
        i=0
        for j in range(2):
            # Create subplots
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
            fig.suptitle(titles[j])

            caption = "Average improvement of the PSNR: "+str(round(self.averageImprovement[j],4))
            plt.text(-0.2, -0.15, caption, ha='center', va='center', transform=plt.gca().transAxes)
            
            # Plot curves on the first subplot
            ax1.plot(self.std_dev, self.ssim[:,i], label='SSIM')
            ax1.plot(self.std_dev, self.mse[:,i], label='MSE')
            ax1.plot(self.std_dev, self.psnr[:,i], label='PSNR')
            ax1.plot(self.std_dev, self.nmi[:,i], label='NMI')

            # Set title and labels for the first subplot
            ax1.set_title('Degraded Image')
            ax1.set_xlabel('Sigma')
            ax1.set_ylabel('Quality log_10(Sigma)')

            # Plot curves on the second subplot
            i += 1
            ax2.plot(self.std_dev, self.ssim[:,i], label='SSIM')
            ax2.plot(self.std_dev, self.mse[:,i], label='MSE')
            ax2.plot(self.std_dev, self.psnr[:,i], label='PSNR')
            ax2.plot(self.std_dev, self.nmi[:,i], label='NMI')

            # Set title and labels for the second subplot
            ax2.set_title('Reconstructed Image')
            ax2.set_xlabel('Sigma')
            ax2.set_ylabel('Quality log_10(Sigma)')

            # Add legend to both subplots
            ax1.legend()
            ax2.legend()

            # Adjust spacing between subplots
            plt.subplots_adjust(wspace=0.4)

            # Show the plot
            plt.show()
            i += 1

    def execute(self):
        self.calculate_values()
        self.plot_graph()
