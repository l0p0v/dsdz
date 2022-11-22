# coding=utf-8
my_list = [1, 2]
my_tuple = (1, 2)
other_tuple = 3, 4
my_list[1] = 3  # 'my_list' agora é [1, 3]

try:
    my_tuple[1] = 3
except TypeError:
    print("cannot modify a tuple")


def sum_and_product(x, y):
    return (x + y), (x * y)


sp = sum_and_product(2, 3)  # é igual a (5, 6)
s, p = sum_and_product(5, 10)  # 's' é 15, 'p' é 50

x, y = 1, 2  # 'x' é 1, 'y' é 2
x, y = y, x  # modo Pythonic de trocar as variáveis; agora 'x' é 2, 'y' é 1
