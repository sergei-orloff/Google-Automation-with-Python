#!/usr/bin/env python3
# process_images.py
# Purpose: Convert TIFF images to JPEG, resize, and rotate them
# Usage: Place in same directory as 'images' folder and run: python3 process_images.py
# Dependencies: Pillow (PIL) - install with: pip install Pillow

# ====== IMPORTS ======
from PIL import Image
import os
from pathlib import Path


# ====== MAIN FUNCTION ======
def process_images(input_folder, output_folder):
    # Create output directory if it doesn't exist
    Path(output_folder).mkdir(parents=True, exist_ok=True)

    # Counter for processed images
    processed_count = 0

    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.tiff'):
            try:
                # Construct full file paths
                input_path = os.path.join(input_folder, filename)
                output_filename = os.path.splitext(filename)[0] + '.jpeg'
                output_path = os.path.join(output_folder, output_filename)

                # Open and process image
                with Image.open(input_path) as img:
                    # Convert RGBA to RGB if necessary
                    if img.mode == 'RGBA':
                        # Create a white background
                        background = Image.new('RGB', img.size, (255, 255, 255))
                        # Paste the image on the background using an alpha channel
                        background.paste(img, mask=img.split()[3])
                        img = background
                    elif img.mode != 'RGB':
                        # Convert any other mode to RGB
                        img = img.convert('RGB')

                    # Rotate 90 degrees clockwise
                    img_rotated = img.rotate(-90, expand=True)

                    # Resize to 128x128
                    img_resized = img_rotated.resize((128, 128),
                                                     Image.Resampling.LANCZOS)

                    # Save as JPEG
                    img_resized.save(output_path, 'JPEG', quality=95)

                processed_count += 1
                print(f"Processed: {filename} -> {output_filename}")

            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")

    return processed_count


# ====== PROGRAM ENTRY POINT ======
def main():
    # Define input and output folders
    input_folder = "images"
    output_folder = "icons"

    # Process the images
    processed_count = process_images(input_folder, output_folder)

    # Print summary
    print(f"\nProcessing complete!")
    print(f"Total images processed: {processed_count}")


if __name__ == "__main__":
    main()
"""
The script to be easily copied and pasted into a nano editor, with line numbers and 
comments to help with navigation.

To use this in nano:

1. Open terminal and create a new file:
        
        ```bash
        nano Mod1_Project_nano.py
        ```

2. Copy and paste the above code

3. Save the file:
- Press `Ctrl + O` to write out
- Press `Enter` to confirm
- Press `Ctrl + X` to exit

4. Make the script executable:
```bash
chmod +x process_images.py
```

5. Run the script:
```bash
./process_images.py
```

Key nano editor tips:
- Use `Ctrl + K` to cut a line
- Use `Ctrl + U` to paste a line
- Use `Ctrl + W` to search for text
- Use `Ctrl + V` to move down one page
- Use `Ctrl + Y` to move up one page

The script has been formatted with:
- Clear section headers for easy navigation
- Consistent indentation (4 spaces)
- Line breaks at logical points
- Comprehensive comments
- Proper shebang line for direct execution

This makes it easier to navigate and edit in nano's simple interface. 
The functionality remains exactly the same as the previous version.
"""