# img.py

from PIL import Image, ImageTk
import io
import os
import cairosvg

def load_icon(image_path, size=(50, 50)):
    """
    Load and convert an image (.svg or .png) into a Tkinter-compatible PhotoImage.

    Parameters:
        image_path (str): Path to the image file.
        size (tuple): Desired output size (width, height).

    Returns:
        ImageTk.PhotoImage: A PhotoImage object usable in Tkinter widgets.
    """
    if not os.path.exists(image_path):
        print(f"[img.py] Image not found: {image_path}")
        return None

    try:
        # Convert SVG to PNG in-memory if needed
        if image_path.lower().endswith(".svg"):
            png_data = cairosvg.svg2png(url=image_path)
            image = Image.open(io.BytesIO(png_data))
        else:
            image = Image.open(image_path)

        image = image.resize(size, Image.LANCZOS)
        return ImageTk.PhotoImage(image)

    except Exception as e:
        print(f"[img.py] Error loading image {image_path}: {e}")
        return None
