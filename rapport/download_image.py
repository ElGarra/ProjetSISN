import os
import urllib.request
from skimage import data

def download_image(url, save_path):
    try:
        urllib.request.urlretrieve(url, save_path)
        print("Image downloaded successfully!")
    except Exception as e:
        print(f"Error downloading the image: {e}")

def main():
    # Set the URL of the image you want to download
    image_url = data.camera()

    # Set the path where you want to save the downloaded image
    save_directory = "./"
    os.makedirs(save_directory, exist_ok=True)  # Create the directory if it doesn't exist
    save_path = os.path.join(save_directory, "downloaded_image.jpg")

    # Download the image
    download_image(image_url, save_path)

if __name__ == "__main__":
    main()
