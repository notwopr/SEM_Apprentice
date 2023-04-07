from PIL import Image

def bmp_to_png_pil(source, destination):
    # open the BMP image
    with Image.open(source) as img:
        # convert to PNG format
        img.save(destination, 'PNG')