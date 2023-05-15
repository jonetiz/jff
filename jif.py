"""
Jon's Image Format (JIF)
(pronounced the way it's spelled, believe it or not, just like how GIF is said with a voiced velar plosive (/ɡ/))

Made this for fun to gain an understanding of image files and compression
"""

from PIL import Image

CHANNELS_GRAYSCALE  = 0b0000
CHANNELS_RED        = 0b0001
CHANNELS_GREEN      = 0b0010
CHANNELS_BLUE       = 0b0100
CHANNELS_ALPHA      = 0b1000

CHANNELS_RGB        = 0b0111
CHANNELS_RGBA       = 0b1111

class JIF:
    def __init__(self, size_x: int, size_y: int, channels: bytes):
        self.header = self.Header(size_x, size_y, channels)
        self.data: list[self.Pixel] = []

    class Header:
        def __init__(self, size_x: int, size_y: int, channels: bytes):
            self.size_x = size_x
            self.size_y = size_y
            self.channels = channels
            self.bits_per_pixel = channels.bit_count() * 8

    class Pixel:
        def __init__(self, data: bytes):
            self.data = data

sz_x = 100
sz_y = 100

asd = JIF(sz_x, sz_y, CHANNELS_RGB)
print(asd.header.channels)
print(asd.header.bits_per_pixel)
print(asd.data)

for i in range(1920):
    asd.data.append(JIF.Pixel(0xFF0000))

img = Image.new(mode="RGB", size=(sz_x, sz_y))

for i, pixel in enumerate(asd.data):
    img.putpixel((i % asd.header.size_x, asd.header.size_x), )

img.show()