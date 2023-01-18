print(f'map generator')


def my_map(func, *args):
    """
    Функція-генератор map
    :param func: some func
    :param args: some values
    :return: some values
    """
    count_item = len(args)
    min_len_obj = float('inf')
    for obj in args:
        if len(obj) < min_len_obj:
            min_len_obj = len(obj)
    for x in range(min_len_obj):
        if count_item > 1:
            temp_res = []
            for item in args:
                temp_res.append(item[x])
            yield func(temp_res)
        else:
            for item in args:
                yield func(item[x])


test1 = list(my_map(int, '1234567890'))
test2 = list(my_map(min, range(10), range(20, 30), range(25, 15, -1)))

print(list(map(int, '1234567890')) == test1)
print(list(map(min, range(10), range(20, 30), range(25, 15, -1))) == test2)


print(f'zip generator')


def my_zip(*args):
    """
    Функція-генератор zip
    :param args: some values
    :return: tuple of some values
    """
    _min = float('inf')
    for item in args:
        if len(item) < _min:
            _min = len(item)
    for index0 in list(range(_min)):
        res_list = []
        for item1 in args:
            res_list.append(item1[index0])
        yield tuple(res_list)


test1 = list(my_zip(range(10), range(15), range(8)))
test2 = list(my_zip(range(10), range(15), []))
test3 = list(my_zip(range(10)))

print(list(zip(range(10), range(15), range(8))) == test1)
print(list(zip(range(10), range(15), [])) == test2)
print(list(zip(range(10))) == test3)


print(f'filter generator')


def my_filter(func=None, *args):
    """
    Функція-генератор filter
    :param func: some func
    :param args: some values
    :return: some values
    """
    if func is None:
        for item in args:
            for i in item:
                if i:
                    yield i
    else:
        for item in args:
            for i in item:
                if func(i):
                    yield i


test1 = list(my_filter(None, [0, 1, '', 2, 3, [], 5, {}, None, 6, False]))
test2 = list(my_filter(lambda a: a % 2 == 0, range(10 + 1)))

print(list(filter(None, [0, 1, '', 2, 3, [], 5, {}, None, 6, False])) == test1)
print(list(filter(lambda a: a % 2 == 0, range(10 + 1))) == test2)


print(f'enumerate generator')


def my_enum(item, index_start=0):
    """
    Функція-генератор enumerate
    :param item: some value
    :param index_start: the value from which the countdown starts
    :return: tuple of some values
    """
    count = index_start
    for i in item:
        yield (count, i)
        count += 1


test = list(my_enum('1234567890', 1))

print(list(enumerate('1234567890', 1)) == test)


print(f'range generator')


def my_range(start, stop=0, step=1):
    """
    Функція-генератор range
    :param start: start value
    :param stop: stop value
    :param step: step
    :return: some value
    """
    if stop == 0:
        stop, start = start, stop
    if step > 0:
        while start < stop:
            yield start
            start += step
    else:
        while start > stop:
            yield start
            start += step


test1 = list(my_range(10))
test2 = list(my_range(10, 20))
test3 = list(my_range(10, 20, 3))
test4 = list(my_range(20, 10, 3))
test5 = list(my_range(20, 10, -3))
test6 = list(my_range(20, 10))

print(list(range(10)) == test1)
print(list(range(10, 20)) == test2)
print(list(range(10, 20, 3)) == test3)
print(list(range(20, 10, 3)) == test4)
print(list(range(20, 10, -3)) == test5)
print(list(range(20, 10)) == test6)