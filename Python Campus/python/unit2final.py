class Pixel:

    def __init__(self, x=0, y=0, red=0, green=0, blue=0):
        self._x = x
        self._y = y
        self._red = red
        self._green = green
        self._blue = blue

    def set_coords(self, x, y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        average = (red + green + blue)/3
        self._red = average
        self._green = average
        self._blue = average

    def print_pixel_info(self):
        print("X: " + str(self._x) + ", " + "Y: " + str(self._y) + ", " + "Color: " + tuple(str(self._red), str(self._green), str(self._blue) )

def main():
    print("fggd")
    # pixel1 = Pixel(1,2,40,60,50)
    # Pixel.print_pixel_info(pixel1)

main()