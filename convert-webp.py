#Here's a Python script that uses the Pillow library to convert all .webp files
#in a directory to .jpeg format, creating copies while preserving the original
#files:


from PIL import Image
import os

def convert_webp_to_jpeg(directory):
    # Ensure the directory exists
    if not os.path.isdir(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return

    # Get all files in the directory
    for filename in os.listdir(directory):
        # Check if the file is a .webp file
        if filename.lower().endswith('.webp'):
            # Construct full file paths
            webp_path = os.path.join(directory, filename)
            # Create the new filename with .jpeg extension
            jpeg_filename = os.path.splitext(filename)[0] + '.jpeg'
            jpeg_path = os.path.join(directory, jpeg_filename)

            try:
                # Open and convert the image
                with Image.open(webp_path) as img:
                    # Convert to RGB (in case the image has an alpha channel)
                    rgb_img = img.convert('RGB')
                    # Save as JPEG with good quality
                    rgb_img.save(jpeg_path, 'JPEG', quality=95)
                print(f"Converted: {filename} -> {jpeg_filename}")
            except Exception as e:
                print(f"Error converting {filename}: {str(e)}")

if __name__ == "__main__":
    # Specify the directory containing .webp files
    # Replace with your directory path or use current directory
    directory_path = "."  # Current directory
    # Or specify a specific path like:
    # directory_path = "/Users/yourusername/Pictures"

    convert_webp_to_jpeg(directory_path)
