# Pillow: redimensionando imagens com Python
# Essa biblioteca é o Photoshop do Python 😂
from PIL import Image

from pathlib import Path

ROOT_FOLDER = Path(__file__).parent
ORIGINAL_FILE = ROOT_FOLDER / 'original.jpg'
NEW_IMAGE = ROOT_FOLDER / 'new.jpg'

pil_image = Image.open(ORIGINAL_FILE)

width, height = pil_image.size
exif = pil_image.info['exif']

new_width = 100
new_height = (height * new_width / width).__round__()

new_image = pil_image.resize(size=(new_width, new_height))
new_image.save(
    NEW_IMAGE,
    optimize=True,
    quality= 70,
    # exif = exif
    )
print(new_width, new_height)