class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        print('Parent class area')


class Rectangle(Shape):
    def __init__(self, w, h):
        self.width = w
        self.height = h

    # class Rectangle has its unique calculation of function area different from parent class, Shape class
    def area(self):
        print('Area of rectangle : ', self.height * self.width)


class Triangle(Shape):
    def __init__(self, w, h):
        self.height = w
        self.width = h

    # class Triangle has its unique calculation of function area different from parent class, Shape class
    def area(self):
        print('Area of a Triangle :', self.height * self.width/2)


rectangle_1 = Rectangle(10, 20)
rectangle_1.area()

triangle_1 = Triangle(20, 30)
triangle_1.area()
