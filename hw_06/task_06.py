# Task_1
def my_all(a):
    for i in a:
        if not i:
            return False
    return True


print(f'my_all')
print(all([]) == my_all([]))
print(all([True, False]) == my_all([True, False]))
print(all([True, True]) == my_all([True, True]))
print(all([False, False]) == my_all([False, False]))


# Task_2
def my_any(a):
    for i in a:
        if i:
            return True
    return False


print(f'my_any')
print(any([]) == my_any([]))
print(any([True, False]) == my_any([True, False]))
print(any([True, True]) == my_any([True, True]))
print(any([False, False]) == my_any([False, False]))


# Task_3
def my_zip(*args):
    _min = float('inf')
    for item in args:
        if len(item) < _min:
            _min = len(item)
    res = []
    for index0 in list(range(_min)):
        res_list = []
        for item1 in args:
            res_list.append(item1[index0])
        res.append(tuple(res_list), )
    return res


print(f'my_zip')
print(list(zip(range(10), range(15), range(8))) == my_zip(range(10), range(15), range(8)))
print(list(zip(range(10), range(15), [])) == my_zip(range(10), range(15), []))
print(list(zip(range(10))) == my_zip(range(10)))


# Task_4
def my_sum(arg):
    sum = 0
    for i in range(len(arg)):
        sum += arg[i]
    return sum


print(f'my_range')
print(sum(range(10)) == my_sum(range(10)))
print(sum([]) == my_sum([]))


# Task_5
def my_filter(func=None, *args):
    res = []
    if func is None:
        for item in args:
            for i in item:
                # print(i)
                if bool(i):
                    res.append(i)
        return res
    else:
        for item in args:
            for i in item:
                if func(i):
                    res.append(i)
        return res


print(f'my_filter')
print(list(filter(None, [0, 1, '', 2, 3, [], 5, {}, None, 6, False])) == my_filter(None,
                                                                                   [0, 1, '', 2, 3, [], 5, {}, None, 6,
                                                                                    False]))
print(list(filter(lambda a: a % 2 == 0, range(10 + 1))) == my_filter(lambda a: a % 2 == 0, range(10 + 1)))


# Task_6
def my_enum(item, index_start=0):
    count = index_start
    res = []
    for i in item:
        res.append((count, i))
        count += 1
    return res


print(f'my_enumerate')
print(list(enumerate('1234567890', 1)) == my_enum('1234567890', 1))


# Task_7
def my_range(start, stop=0, step=1):
    res = []
    if stop == 0:
        stop, start = start, stop
    if step > 0:
        while start < stop:
            res.append(start)
            start += step
        return res
    else:
        while start > stop:
            res.append(start)
            start += step
        return res


print(f'my_range')
print(list(range(10)) == my_range(10))
print(list(range(10, 20)) == my_range(10, 20))
print(list(range(10, 20, 3)) == my_range(10, 20, 3))
print(list(range(20, 10, 3)) == my_range(20, 10, 3))
print(list(range(20, 10, -3)) == my_range(20, 10, -3))
print(list(range(20, 10)) == my_range(20, 10))

# Task_8
print(f'Map')


def my_map(func, *args):
    res = []
    if len(args) == 1:
        for obj in args:
            for item in obj:
                t = func(item)
                res.append(t)
        return res
    for obj in args:
        res.append(list(obj))
    return func(res)


print(list(map(int, '1234567890')) == my_map(int, '1234567890'))
print(list(map(min, range(10), range(20, 30), range(25, 15, -1))) == my_map(min, range(10), range(20, 30),
                                                                            range(25, 15, -1)))
