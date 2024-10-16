from PIL import Image
import os
from pathlib import Path


def process_images(input_folder, output_folder):
    # Create output directory if it doesn't exist
    Path(output_folder).mkdir(parents=True, exist_ok=True)

    # Counter for processed images
    processed_count = 0

    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):

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
                    # Paste the image on the background using an alpha channel as mask
                    background.paste(img, mask=img.split()[3])  # 3 is the alpha channel
                    img = background
                elif img.mode != 'RGB':
                    # Convert any other mode to RGB
                    img = img.convert('RGB')

                # Rotate 90 degrees clockwise
                img_rotated = img.rotate(-90, expand=True)  # Negative angle for clockwise rotation

                # Resize to 128x128
                img_resized = img_rotated.resize((128, 128), Image.Resampling.LANCZOS)

                # Save as JPEG
                img_resized.save(output_path, 'JPEG', quality=95)

            processed_count += 1
            print(f"Processed: {filename} -> {output_filename}")

        except Exception as e:
            print(f"Error processing {filename}: {str(e)}")

    return processed_count


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
