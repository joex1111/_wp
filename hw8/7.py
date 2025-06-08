def dict_to_string(d):
    return ', '.join(f"{key}:{value}" for key, value in d.items());
    d = {'a': 1, 'b': 2};
print(dict_to_string(d));