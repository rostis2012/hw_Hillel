import sys
import functools
ENABLE_TRACE = True # False

def super_trace(*, file=sys.stdout):
    def trace(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            if ENABLE_TRACE:
                # print(f'Trace=TRUE')
                print(f'*** {inner.__name__}', file=file)
                print(f'Позиционных аргументов = {len(args)}', file=file)
                if len(args):
                    for i in args:
                        print(f'Тип позиционного аргумента = {type(i)}, его значение = {i}', file=file)
                print(f'Именованых аргументов = {len(kwargs)}', file=file)
                if len(kwargs):
                    # print(kwargs)
                    for i in kwargs:
                        print(f'Тип именованного аргумента = {type(kwargs[i])}, его значение {i} = {kwargs[i]}', file=file)
                res = func(*args, **kwargs)
                if res:
                    print(f'Функция возвращает {len(res)} объектов', file=file)
                    for i in res:
                        print(f'объект типа {type(i)} его значение {i}', file=file)
                else:
                    print(f'Функция возвращает NONE', file=file)
            return func(*args, **kwargs)
        return inner
    return trace


@super_trace(file=sys.stderr)
def test1(a, b, c ):
    return [a, b, c], a, str(b), float(c)


@super_trace()
def test2(a, b, *, c, d):
    return [a, b, c, d], a, str(b), float(c), d


@super_trace(file=sys.stderr)
def test3(*, a, b, c, d):
    return [a, b, c, d], a, str(b), float(c), d

@super_trace()
def test4(a, b, *, c, d):
    print([a, b, c, d], a, str(b), float(c), d)


@super_trace()
def test5():
    return [1, 2, 3]



if __name__ == '__main__':
   # test ENABLE_TRACE = False
   ENABLE_TRACE = False
   test1(1, 2, 3)
   test2(1, 2, c=3, d=4)
   test3(a=1, b=2, c=3, d=4)
   test4(1, 2, c=3, d=4)
   test5()

   # test ENABLE_TRACE = True
   ENABLE_TRACE = True
   test1(1, 2, 3)
   test2(1, 2, c=3, d=4)
   test3(a=1, b=2, c=3, d=4)
   test4(1, 2, c=3, d=4)
   test5()
