def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(2)
print_params(1, 3)
print_params(b=25)    # меняет значение b
print_params(c=[1, 2, 3])   # меняет значение c

values_list = [5, 'текст', False]
values_dict = {'a': 8, 'b': 'привет', 'c': True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [5, 'текст']
print_params(*values_list_2, 42)    # распаковывает список, меняет значение c
