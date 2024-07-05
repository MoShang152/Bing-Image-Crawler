# Bing Image Downloader Project

This project uses the `bing_image_downloader` library to download images from Bing based on a specified search term. The goal is to download a large number of images for a given keyword.

## Requirements

- Python 3.x
- bing_image_downloader

## Installation

1. Install the required library using pip:

   ```bash
   pip install bing_image_downloader
   ```

## Usage

The script downloads images based on the specified search term and saves them to a designated directory.

```python
from bing_image_downloader import downloader

# Define the search term and number of images to download
search_term = "Kazusa"
num_images = 10
output_directory = 'bing_images_test'

# Download images and save them to the specified directory
downloader.download(search_term, limit=num_images, output_dir=output_directory, adult_filter_off=True, force_replace=False, timeout=60)

print(f"Downloaded {num_images} images of '{search_term}' to the directory '{output_directory}'.")
```

## Parameters

- `search_term`: The keyword to search for images on Bing.
- `num_images`: The number of images to download.
- `output_directory`: The directory to save the downloaded images.
- `adult_filter_off`: Boolean to turn off the adult content filter.
- `force_replace`: Boolean to force replacement of existing files.
- `timeout`: Timeout in seconds for each download request.

## Note

Ensure you have a stable internet connection while downloading images, as downloading a large number of images might take some time.

## License

This project is licensed under the MIT License.
