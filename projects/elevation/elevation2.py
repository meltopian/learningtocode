from PIL import Image

IMAGE_FILENAME = './elevationimage.jpg'


#data = ['a', 'b']
#data = {'a':1, 'b':2}
#data = {'a', 'b'}

SEA_LEVEL_BASE = 24
SCALE_FACTOR = 12
CROP_UNITED_KINGDOM = (3850, 700, 4150, 950)


data = (
    # name, height, color
    ('level7', 220, (0, 255, 0)),
    ('level6', 190, (0, 220, 0)),
    ('level1', SEA_LEVEL_BASE, (0, 75, 0)),
    ('sea', 0, (0, 0, 255)),
)

LEVEL_7 = 220
LEVEL_6 = 190
LEVEL_5 = 150
LEVEL_4 = 100
LEVEL_3 = 40
LEVEL_2 = 35
LEVEL_1 = 30


image_src = Image.open(IMAGE_FILENAME)
image_src = image_src.crop(CROP_UNITED_KINGDOM)
image_des = Image.new('RGB', (image_src.width, image_src.height), 0x000000)

sea_level = 0

def land_height_to_color(land_height):
    """
    >>> land_height_to_color(200)
    (0, 220, 0)
    """
    for name, height, color in data:
        if land_height >= height:
            return color

# TODO - sea_level to meters function
for y in range(image_src.height):
    for x in range(image_src.width):
        land_height = image_src.getpixel((x, y))  # Greyscale image so we get 0->255 back from getpixel
        image_des.putpixel((x, y), land_height_to_color(land_height))

image_des.show()