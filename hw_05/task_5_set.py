set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
set_c = {7, 8, 9, 10, 11}


# task_1
def task_1():
    res = set_a | set_b | set_c
    return res


# task_2
def task_2():
    res_a_b = set_a - set_b
    res_b_c = set_b - set_c
    res_a_c = set_a - set_c
    print(f'res_a_b = {res_a_b}')
    print(f'res_b_c = {res_b_c}')
    print(f'res_a_c = {res_a_c}')
    return


# task_3
def task_3():
    res_a_b = set_a & set_b
    res_b_c = set_b & set_c
    res_a_c = set_a & set_c
    print(f'res_a_b = {res_a_b}')
    print(f'res_b_c = {res_b_c}')
    print(f'res_a_c = {res_a_c}')
    return


# task_4
def task_4():
    set_target = {1, 2}
    new_dict = {'set_a': set_a, 'set_b': set_b, 'set_c': set_c}
    for item in new_dict:
        if set_target < new_dict.get(item):
            print(f'set {set_target} є підмножиною {item} {new_dict.get(item)}')
        else:
            print(f'set {set_target} НЕ є підмножиною {item} {new_dict.get(item)}')
    return


# Task_5
def task_5():
    result = task_1().copy()
    res_1 = set()
    res_2 = set()
    for item in result:
        if item % 2:
            res_2.add(item)
        else:
            res_1.add(item)
    print(f'res_1 = {res_1}')
    print(f'res_2 = {res_2}')
    return


print(f'Task #1 \nres= {task_1()}')
print(f'\nTask #2')
task_2()
print(f'\nTask #3')
task_3()
print(f'\nTask #4')
task_4()
print(f'\nTask #5')
task_5()
