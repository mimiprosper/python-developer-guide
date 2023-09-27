# abstraction show functionalities and hides the internal details or working

from abc import ABC, abstractmethod  # import the abstract class module


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side * self.__side

    def perimeter(self):
        return 4 * self.__side


my_square = Square(5)
print(my_square.area())
print(my_square.perimeter())
