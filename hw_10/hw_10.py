import sys
import math

class Check_value:
    "Дескриптор перевірки значення, яке повинно бути білше за 0, та існування трикутника"

    def __set_name__(self, owner, name):
        self.name = f'__{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, *args):
        t, = args
        # print(f't={t} args={args} len args={len(args)} type of args ={type(args)} type of t ={type(t)}')
        if not isinstance(t, (float)):
            for i in args:
                for j in i:
                    assert float(j) > 0, 'Помилка! Значення не має дорівнювати 0'
            if len(t) == 3:
                a, b, c = t
                a = float(a)
                b = float(b)
                c = float(c)
                if not (a < c + b and b < a + c and c < a + b):
                    raise CheckTriangleExistence(
                        f'Трикутника зі сторонами a = {a} b = {b} c = {c}  не існує')
        else:
            assert float(t) > 0, 'Помилка! Значення не має дорівнювати 0'
        setattr(instance, self.name, t)


class CheckTriangleExistence(Exception):
    pass


class Figure:
    "Абстрактний клас геометричної фігури"

    def get_perimeter(self, *args):
        raise NotImplementedError

    def get_area(self, *args):
        raise NotImplementedError


class Circle(Figure):
    "Клас Circle, наслідник класу Figure "
    radius = Check_value()

    def __init__(self, value):
        self.radius = float(value)

    def get_type(self):
        return self.__class__.__name__

    def get_sides(self):
        return f'{self.__class__.__name__} -> r = {self.radius}'

    def get_perimeter(self):
        return f'Perimeter = {2 * math.pi * self.radius}'

    def get_area(self):
        return f'Area = {math.pi * (self.radius * self.radius)}'


class Rectangle(Figure):
    "Клас Rectangle, наслідник класу Figure "
    check = Check_value()

    def __init__(self, *args):
        self.check = args
        a_, b_ = args
        self.a = float(a_)
        self.b = float(b_)

    def get_type(self):
        return self.__class__.__name__

    def get_sides(self):
        return f'{self.__class__.__name__} -> a = {self.a}, b = {self.b}'

    def get_perimeter(self):
        return f'Perimetr = {(self.a + self.b) * 2}'

    def get_area(self):
        return f'Area = {self.a * self.b}'


class Triangle(Figure):
    "Клас Triangle, наслідник класу Figure "
    check = Check_value()

    def __init__(self, *args):
        self.check = args
        a_, b_, c_ = args
        self.a = float(a_)
        self.b = float(b_)
        self.c = float(c_)


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


if __name__ == '__main__':
    data_ = input('Enter values:').split()
    count_sides = len(data_)
    obj = None

    def show():
        print(obj.get_type())
        print(obj.get_sides())
        print(obj.get_perimeter())
        print(obj.get_area())

    try:
        if count_sides == 1:
            obj = Circle(*data_)
            show()
        elif count_sides == 2:
            obj = Rectangle(*data_)
            show()
        elif count_sides == 3:
            try:
                obj = Triangle(*data_)
            except CheckTriangleExistence as err:
                print(err, file=sys.stderr)
            else:
                show()
        else:
            print(f'Entered wrong value, object cannot be created!', file=sys.stderr)
    except AssertionError as err:
        print(err, file=sys.stderr)
