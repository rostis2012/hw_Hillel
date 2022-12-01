# Написати три класи для обрахунку периметру та площі трикутника, прямокутника
# або кола. Кожен клас повинен мати 4 обовзякові методи
import sys
import math
class Circle:
    def __init__(self, r):
        self.radius = float(r)

    # This method should return type of object:
    # Triangle, Rectangle, Circle
    def get_type(self):
        return self.__class__.__name__

    # This method should return sides of object
    # Triangle -> a=X b=X c=X
    # Rectangle -> a=X b=X
    # Circle -> r=X
    def get_sides(self):
        return f'{self.__class__.__name__} -> r = {self.radius}'

    # This method should return perimeter of object
    def get_perimeter(self):
        return f'Perimeter = {2 * math.pi * self.radius}'

    # This method should return area of object
    def get_area(self):
        return f'Area = {math.pi * (self.radius * self.radius)}'


class Rectangle:
    def __init__(self, *args):
        self.a, self.b = args
        self.a = float(self.a)
        self.b = float(self.b)

    def get_type(self):
        return self.__class__.__name__

    def get_sides(self):
        return f'{self.__class__.__name__} -> a = {self.a}, b = {self.b}'

    def get_perimeter(self):
        return f'Perimetr = {(self.a + self.b)*2}'

    def get_area(self):
        return f'Area = {self.a * self.b}'


class Triangle:
    def __init__(self, *args):
        self.a, self.b, self.c = args
        self.a = float(self.a)
        self.b = float(self.b)
        self.c = float(self.c)

    def get_type(self):
        return self.__class__.__name__

    def get_sides(self):
        return f'{self.__class__.__name__} -> a = {self.a}, b = {self.b}, c = {self.c}'

    def get_perimeter(self):
        return f'Perimetr = {self.a + self.b + self.c}'

    def get_area(self):
        p_p = (self.a + self.b + self.c) / 2
        sq = math.sqrt((p_p * ((p_p - self.a) * (p_p - self.b) * (p_p - self.c))))
        return f'Area = {sq}'


def get_class(raw_input):
    count = len(raw_input.split())
    if count <= 3:
        if count == 1:
            if float(raw_input):
                return Circle(raw_input)
            return None
        elif count == 2:
            a, b = raw_input.split()
            a = float(a)
            b = float(b)
            if a and b:
                return Rectangle(a, b)
            return None
        else:
            a, b, c = raw_input.split()
            a = float(a)
            b = float(b)
            c = float(c)
            if a and b and c and a < c + b and b < a + c and c < a + b:
                return Triangle(a, b, c)
            else:
                return None
    else:
        return None


if __name__ == '__main__':
    raw_input = input('Enter values:')
    object = get_class(raw_input)
    if object:
        print(object.get_type())
        print(object.get_sides())
        print(object.get_perimeter())
        print(object.get_area())
    else:
        print(f'Entered wrong values, object cannot be created!', file=sys.stderr)
