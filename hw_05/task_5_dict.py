dict_a = {
    'key_1': 'value_1',
    'key_2': 'value_2',
    'key_3': 'value_3',
    'key_4': 'value_4',
    'key_5': 'value_5'
}

dict_b = {
    'key_6': 'value_6',
    'key_7': 'value_7',
    'key_8': 'value_8',
    'key_9': 'value_9',
    'key_10': 'value_10'
}

dict_c = {
    'key_4': 'value_4',
    'key_5': 'value_5',
    'key_6': 'value_6',
    'key_7': 'value_7',
    'key_8': 'value_8'
}


def task_1():
    res = {}
    tuple_dict = (dict_a, dict_b, dict_c)
    for item in tuple_dict:
        res.update(item)
    return res


def task_2():
    print(f'Task #2')
    res = dict(zip(dict_a.keys(), dict_b.values()))
    return res


def task_3():
    print(f'Task #3')
    res = dict(zip(dict_b.values(), dict_a.keys()))
    return res


def task_4(res_task_1):
    print(f'Task #4')
    # res_temp={}
    # res_temp.update(res_task_1) # Как правильнее? Сразу подставить res_task_1 в цикл фор или создавать временный словарь? или цикл при каждой итерации будет вызывать функцию task_1?
    res = {}
    for item, values in res_task_1.items():
        if int(values.split('_')[-1]) % 2:
            res.update({item: values})
    return res


def task_5_1():  # через словарь в словаре
    print(f'Task #5 v1')
    _count_a = 0
    _count_b = 0
    name_dict = {'dict_a': dict_a, 'dict_b': dict_b, 'dict_c': dict_c}
    res = {}
    for key, value in name_dict.get('dict_c').items():
        if name_dict.get('dict_a').get(key, 0) and name_dict.get('dict_a').get(key, 0) == value:
            _count_a += 1
            if res.get('dict_a', 0) == 0:
                res.update({'dict_a': _count_a})
            res['dict_a'] = _count_a
        if name_dict.get('dict_b').get(key, 0) and name_dict.get('dict_b').get(key, 0) == value:
            _count_b += 1
            if res.get('dict_a', 0) == 0:
                res.update({'dict_b': _count_b})
            res['dict_b'] = _count_b
    return res


def task_5_2():  # через set
    print(f'Task #5 v2')
    set_a = set(dict_a.items())
    set_b = set(dict_b.items())
    set_c = set(dict_c.items())
    res = {'dict_a': len(set_a & set_c), 'dict_b': len(set_b & set_c)}
    return res


print(f'Task #1')
print(f'res = {task_1()}\n')
print(f'res = {task_2()}\n')
print(f'res = {task_3()}\n')
print(f'res = {task_4(task_1())}\n')
print(f'res = {task_5_1()}\n')
print(f'res = {task_5_2()}')
