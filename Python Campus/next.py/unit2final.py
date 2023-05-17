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
        average = (self._red + self._green + self._blue)/3
        self._red = average
        self._green = average
        self._blue = average

    def print_pixel_info(self):
        if self._red == 0 and self._green == 0 and self._blue > 50 :
            print("X: " + str(self._x) + ", " + "Y: " + str(self._y) + ", " + "Color: " + "(" + str(self._red) + ", " + str(self._green) + ", " + str(self._blue) + ")" + " Blue")
        elif self._red == 0 and self._blue == 0 and self._green > 50 :
            print("X: " + str(self._x) + ", " + "Y: " + str(self._y) + ", " + "Color: " + "(" + str(self._red) + ", " + str(self._green) + ", " + str(self._blue) + ")" + " Green")
        elif self._blue == 0 and self._green == 0 and self._red > 50 :
            print("X: " + str(self._x) + ", " + "Y: " + str(self._y) + ", " + "Color: " + "(" + str(self._red) + ", " + str(self._green) + ", " + str(self._blue) + ")" + " Red")
        else:
            print("X: " + str(self._x) + ", " + "Y: " + str(self._y) + ", " + "Color: " + "(" + str(self._red) + ", " + str(self._green) + ", " + str(self._blue) + ")")


def main():
     pixel1 = Pixel(5,6,250,0,0)
     pixel1.print_pixel_info()
     pixel1.set_grayscale()
     pixel1.print_pixel_info()

main()