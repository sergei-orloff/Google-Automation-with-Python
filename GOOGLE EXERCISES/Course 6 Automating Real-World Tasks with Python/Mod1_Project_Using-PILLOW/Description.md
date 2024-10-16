Task: Scaling and converting images using PIL (Pillow) Python library. 
The images received in the folder "images" are in the wrong format: 
* .tiff format
* Image resolution 192x192 pixels (too large)
* Rotated 90° anti-clockwise
The images should be in this format:
* .jpeg format
* Image resolution 128x128 pixel
* Should be straight

Please write a Python script that uses PIL to perform the following operations:
   * Iterate through each file in the folder "images"
   * For each file:
      * Rotate the image 90° clockwise
      * Resize the image from 192x192 to 128x128
      * Save the image to a new folder in .jpeg format
      * save the updated images in the folder: /Mod1_Project_Using-PILLOW`/icons/`
=========================================================
The Python script using PIL (Pillow) to process images according to the specifications.

This script does everything requested:

1. It looks for .tiff files in the "images" folder
2. For each image, it:
   - Rotates it 90° clockwise (using -90° since PIL's rotate method uses counterclockwise angles)
   - Resizes it to 128x128 pixels using the high-quality LANCZOS resampling method
   - Converts and saves it as a JPEG file in the specified output folder

JPEG format doesn't support transparency (alpha channel), but your TIFF images appear to be in RGBA mode 
(Red, Green, Blue, Alpha). We need to convert the images to RGB mode before saving them as JPEG.

Here's what this does:

First, it checks if the image is in RGBA mode
If it is:

Creates a new white background image in RGB mode
Pastes the original image onto the white background using the alpha channel as a mask
This effectively "flattens" the transparency against a white background


For any other non-RGB mode, it simply converts to RGB mode

This solution:

Preserves the image quality
Handles transparency properly by compositing it with a white background
Ensures the output will be compatible with the JPEG format

Now when you run the script, it should process all your TIFF images successfully, even those with transparency, 
and convert them to JPEG format properly.
To use this script:

1. Make sure you have PIL installed:
```bash
pip install Pillow
```

2. Place the script in the same directory as your "images" folder
3. Run the script

The script includes error handling and will:
- Create the output directory if it doesn't exist
- Skip any files that cause errors during processing
- Print progress updates as it processes each image
- Show a summary when complete

The LANCZOS resampling method is used for the highest quality output when resizing. The JPEG quality is set to 95 to maintain good image quality while keeping file sizes reasonable.
