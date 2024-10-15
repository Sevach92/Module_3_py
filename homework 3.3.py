def print_params(a = 1, b = 'строка', c = True):
   print(a, b, c)

# Функция с параметрами по умолчанию
print_params(10, 'hello')
print_params( 12345,None, False)
print_params(900)
print_params()
print_params(b=25)
print('Функция работает')
print_params(c = [1,2,3])
print('Функция работает')

# Распаковка параметров
values_list = [586897, 'Распаковка два паковка', True]
values_dict = {'a': 8890, 'b': 'This is wensday my dudes', 'c': None}
print_params(*values_list)
print_params(**values_dict)

#Распаковка + отдельные параметры
values_list_2 = [5690, 'My dudes' ]
print_params(*values_list_2, 42)
print ('Функция работает')