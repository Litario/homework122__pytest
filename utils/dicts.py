def get_val(dict, key, default='git'):
    if key in dict:
        return dict[key]
    return default


# d = {1: 'one', 2: 'two'}
# print(get_val(d, 3))
