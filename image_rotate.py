
# image_rotate.py

from PIL import Image

def rotate_image(image: Image.Image) -> Image.Image:
    """
    Rotate the given PIL Image 90 degrees clockwise and return the rotated image.
    """
    # PIL's rotate() method uses counter-clockwise degrees, so we pass -90 for a 90° clockwise rotation.
    # expand=True ensures the output image size is adjusted to hold the full rotated image.
    return image.rotate(-90, expand=True)

if __name__ == '__main__':
    import sys

    if len(sys.argv) != 3:
        print("Usage: python image_rotate.py <input_image_path> <output_image_path>")
        sys.exit(1)

    input_path, output_path = sys.argv[1], sys.argv[2]

    # Open the input image
    img = Image.open(input_path)

    # Rotate it
    rotated_img = rotate_image(img)

    # Save the result
    rotated_img.save(output_path)
    print(f"Rotated image saved to {output_path}")
