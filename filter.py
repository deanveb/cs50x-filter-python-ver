from PIL import Image
from sys import argv

from helper import GrayScale, Sepia, Reflect, Blur

def main():
    if len(argv) != 3:
        raise Exception("Usage: python3 filter.py [filepath] [filter]")
    filepath = argv[1]
    filter_type = argv[2]
    image = Image.open(filepath)
    pixels = image.load()
    width, height = image.size
    print(type(pixels))
    global bitmap
    bitmap = []
    for i in range(width):
        row = []
        for j in range(height):
            # print(j)
            # Append column
            row.append(RGB(pixels[i,j][0], pixels[i,j][1], pixels[i,j][2]))
        # Append row
        bitmap.append(row)
    
    match filter_type:
        case "-g":
            GrayScale(height, width, bitmap)
        case "-s":
            Sepia(height, width, bitmap)
        case "-r":
            Reflect(height, width, bitmap)
        case "-b":
            Blur(height, width, bitmap)

    # Save image
    image = Image.new("RGB", (width, height))

    # Set the pixel data
    for y in range(height):
        for x in range(width):
            image.putpixel((x, y), (bitmap[x][y].Red, bitmap[x][y].Green, bitmap[x][y].Blue))

    # Save the image
    image.save("output.bmp", "BMP")
    image.save("output.png", "PNG")

class RGB:
    Red = 0
    Green = 0
    Blue = 0
    def __init__(self, R, G ,B) -> None:
        self.Red = R
        self.Green = G
        self.Blue = B

main()
