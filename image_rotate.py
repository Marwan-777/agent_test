
# image_rotate.py

import sys
from typing import Union

import numpy as np
from PIL import Image

def rotate_image(image: Union[Image.Image, np.ndarray]) -> Image.Image:
    """
    Rotate the given image (PIL Image or numpy ndarray) 90 degrees clockwise
    and return the rotated image as a PIL Image.
    """
    # If the input is a numpy array, convert it to a PIL Image
    if isinstance(image, np.ndarray):
        image = Image.fromarray(image)
    # Rotate 90° clockwise by passing -90° to PIL's rotate (which is counter-clockwise)
    rotated = image.rotate(-90, expand=True)
    return rotated

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python image_rotate.py <input_image_path> <output_image_path>")
        sys.exit(1)

    input_path, output_path = sys.argv[1], sys.argv[2]

    # Open the input image using PIL
    img = Image.open(input_path)

    # Rotate the image
    rotated_img = rotate_image(img)

    # Save the rotated image
    rotated_img.save(output_path)
    print(f"Rotated image saved to {output_path}")
