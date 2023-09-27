class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        print("Print the Area of the parent class")


class Triangle(Shape):
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        print("The area of a Triangle :", self.width * self.height)


triangle_1 = Triangle(20, 30)
triangle_1.area()


class Rectangle(Shape):
    def __init__(self, w, h):
        self.width = w
        self.height = h


def area(self):
    print("The area of the Rectangle :", self.width * self.height / 2)


rectangle_1 = Rectangle(12, 10)
rectangle_1.area()
