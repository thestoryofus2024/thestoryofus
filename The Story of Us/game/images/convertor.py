from PIL import Image
from rembg import remove
import io

def convert_jpeg_to_png(input_path, output_path):
    """
    Converts a JPEG image to PNG format.
    """
    with Image.open(input_path) as img:
        img = img.convert("RGBA")  # Ensure transparency for background removal
        img.save(output_path, "PNG")

def remove_background(input_path, output_path):
    """
    Removes the background from the image using rembg.
    """
    with open(input_path, 'rb') as input_file:
        img_data = input_file.read()
    
    # Remove the background
    output_data = remove(img_data)
    
    # Save the result
    with open(output_path, 'wb') as output_file:
        output_file.write(output_data)

def resize_image(input_path, output_path, new_size):
    """
    Resizes the image to the specified size (width, height).
    """
    with Image.open(input_path) as img:
        resized_img = img.resize(new_size)
        resized_img.save(output_path)

def process_image(input_jpeg_path, output_png_path, resized_output_path, size):
    # Step 1: Convert JPEG to PNG
    convert_jpeg_to_png(input_jpeg_path, "temp_image.png")
    print("Image converted to PNG.")
    
    # Step 2: Remove the background
    remove_background("temp_image.png", output_png_path)
    print("Background removed.")
    
    # Step 3: Resize the image
    resize_image(output_png_path, resized_output_path, size)
    print(f"Image resized to {size}.")

if __name__ == "__main__":
    # Input JPEG file
    input_jpeg = "steve.jpeg"
    
    # Output PNG file (after background removal)
    output_png = "steve.png"
    
    # Output resized image
    resized_output = "resized_steve.png"
    
    # Desired size for resizing (width, height)
    new_size = (800, 600)
    
    # Run the processing pipeline
    process_image(input_jpeg, output_png, resized_output, new_size)
