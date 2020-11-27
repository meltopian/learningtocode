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

# TODO - sea_level to meters function
for y in range(image_src.height):
    for x in range(image_src.width):
        land_height = image_src.getpixel((x, y))  # Greyscale image so we get 0->255 back from getpixel
        # for x in (1,2,3):

        # for x, y in ((1,'a'),(2,'b'),(3,'c')):

        # for item in ((1,'a'),(2,'b'),(3,'c')):
        #     x = item[0]
        #     y = item[1]


        # for level_tuple in data:
        #     name = level_tuple[0]
        #     height = level_tuple[1]
        #     color = level_tuple[2]
        #     if land_height >= height:
        #         break

        for name, height, color in data:
            if land_height >= height:
                break

        image_des.putpixel((x, y), color)

image_des.show()