# coding=utf-8
integer_list = [1, 2, 3]
heterogeneous = ["string", 0.1, True]
list_of_lists = [integer_list, heterogeneous]

list_length = len(integer_list)  # é igual a 3
list_sum = sum(integer_list)  # é igual a 6

x = list(range(10))  # é a lista [0, 1, ..., 9]
zero = x[0]  # é igual a 0, as listas são indexadas a partir de 0
one = x[1]  # é igual a 1
nine = x[-1]  # é igual a 9, 'Pythonic' para o último elemento
eight = x[-2]  # é igual a 8, 'Pythonic' para o penúltimo elemento
x[0] = -1  # agora x é [-1, 1, 2, 3, ..., 9]

first_three = x[:3]  # [-1, 1, 2]
three_to_end = x[3:]  # [3, 4, ..., 9]
one_to_four = x[1:5]  # [1, 2, 3, 4]
last_three = x[-3:]  # [7, 8, 9]
without_first_and_last = x[1:-1]  # [1, 2, ..., 8]
copy_of_x = x[:]  # [-1, 1, 2, ..., 9]

print(1 in [1, 2, 3])  # Verdadeiro
print(0 in [1, 2, 3])  # Falso

x = [1, 2, 3]
x.extend([4, 5, 6])  # 'x' agora é [1, 2, 3, 4, 5, 6]

x = [1, 2, 3]
_ = x + [4, 5, 6]  # '_' agora é [1, 2, 3, 4, 5, 6]: 'x' não mudou

x.append(0)  # 'x' agora é [1, 2, 3, 0]
y = x[-1]  # é igual a 0
z = len(x)  # é igual a 4

x, _ = [1, 2]  # agora 'x' é 1 e '_' é 2

_, t = [1, 2]  # agora 't' é 2, não se preocupou com o primeiro valor
