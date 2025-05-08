
# ImageToolkit

## Overview

ImageToolkit is a lightweight, modular Python library providing a suite of common image manipulation utilities. It is designed to seamlessly handle both raw numerical image data (as NumPy arrays) and high-level image objects (as PIL `Image` instances). Whether you’re building preprocessing pipelines for machine learning, performing batch transformations, or experimenting with simple image effects, ImageToolkit offers straightforward, reusable scripts that integrate easily into your projects.

Key features:
- Support for operations on both NumPy arrays and PIL Images  
- Minimal dependencies (`numpy`, `Pillow`)  
- Clear, well-documented modules for rotation, resizing, flipping, and more  
- Designed for batch workflows and interactive use alike  

## Installation

1. Clone the repository  
   ```bash
   git clone https://github.com/yourusername/ImageToolkit.git
   cd ImageToolkit
   ```
2. (Optional) Create and activate a virtual environment  
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies  
   ```bash
   pip install -r requirements.txt
   ```

## Usage Examples

Rotate a NumPy array:
```python
import numpy as np
from image_rotate import rotate_image

# Create a sample image array (H×W×C)
arr = np.random.randint(0, 255, (200, 300, 3), dtype=np.uint8)

# Rotate by 45 degrees, expanding the canvas to fit the result
rotated_arr = rotate_image(arr, angle=45, expand=True)
```

Rotate a PIL Image:
```python
from PIL import Image
from image_rotate import rotate_image

img = Image.open('input.jpg')
rotated_img = rotate_image(img, angle=90, resample=Image.BILINEAR)
rotated_img.save('rotated.jpg')
```

## Module: image_rotate.py

The `image_rotate.py` module provides robust, flexible functionality to rotate images represented either as NumPy arrays or PIL `Image` objects. Below is a detailed breakdown of its features and usage:

### Key Features

- **Universal Input Handling**  
  - Accepts both NumPy arrays (`ndarray`) and PIL `Image` instances.  
  - Automatically detects input type and routes to the appropriate rotation routine.

- **Flexible Rotation Parameters**  
  - `angle` (float): Rotation angle in degrees (counterclockwise).  
  - `expand` (bool): If `True`, expands the output canvas to fully contain the rotated image.  
  - `resample` (int, optional): Interpolation filter for PIL Images (e.g., `Image.NEAREST`, `Image.BILINEAR`, `Image.BICUBIC`).

- **Preserves Image Types**  
  - Returns the same type as input (NumPy array in, NumPy array out; PIL Image in, PIL Image out).  
  - Maintains original image mode (e.g., RGB, RGBA, grayscale).

- **Easy Integration**  
  - One‐line import and call.  
  - Zero configuration needed to get started.

### Function Signature

```python
def rotate_image(
    image: Union[np.ndarray, PIL.Image.Image],
    angle: float,
    expand: bool = False,
    resample: int = None
) -> Union[np.ndarray, PIL.Image.Image]:
    """
    Rotate an image by a specified angle.

    Parameters:
    - image: Input image (NumPy array or PIL Image).
    - angle: Rotation angle in degrees.
    - expand: Whether to expand canvas to fit rotated image.
    - resample: (PIL only) Resampling filter.

    Returns:
    - Rotated image of the same type as input.
    """
```

### Example Usage

```python
from PIL import Image
import numpy as np
from image_rotate import rotate_image

# PIL example
pil_img = Image.open('photo.png')
rot_pil = rotate_image(pil_img, angle=30, expand=True, resample=Image.BICUBIC)
rot_pil.show()

# NumPy example
np_img = np.array(pil_img)
rot_np = rotate_image(np_img, angle=-15)
```

## Additional Modules

- **image_resize.py**: Resize images with aspect‐ratio preservation.  
- **image_flip.py**: Flip images horizontally or vertically.  
- **image_crop.py**: Center or random crop functionality.  

## Contributing

Contributions are welcome! Please open an issue or submit a pull request to discuss changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
