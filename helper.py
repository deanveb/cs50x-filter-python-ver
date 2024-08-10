def GrayScale(width, height, bitmap):
    for h in range(height):
        for w in range(width):
            bitmap[h][w].Red = 255
            bitmap[h][w].Blue = 255
            bitmap[h][w].Green = 255

# python3 filter.py images/courtyard.bmp -g

def Sepia(width, height, bitmap):
    pass

def Reflect(width, height, bitmap):
    pass

def Blur(width, height, bitmap):
    pass