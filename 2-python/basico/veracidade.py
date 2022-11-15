one_is_less_than_two = 1 < 2  # é igual a True
true_equals_false = True == False  # é igual a False

x = None
print(x == None)  # imprime True, mas não é Pythonic
print(x is None)  # imprime True e é Pythonic

"""
Todos os exemplos a seguir são "Falsos":
    ° False
    ° None
    ° [] (uma list vazia)
    ° {} (um dict vazio)
    ° () (uma tupla vazia)
    ° "" ou ''
    ° set()
    ° 0
    ° 0.0
"""


def some_function_that_returns_a_string():
    from string import ascii_lowercase
    from random import randint, choice

    len_string = randint(0, 9)
    string = "".join([choice(ascii_lowercase) for _ in range(len_string)])
    return string


s = some_function_that_returns_a_string()
if s:
    first_char = s[0]
else:
    first_char = ""

print(all([True, 1, {3}]))  # True
print(all([True, 1, {}]))  # False, {} é falso
print(any([True, 1, {}]))  # True, 1 e 'True' são verdadeiros
print(all([]))  # True, sem elementos falsos na lista
print(any([]))  # False, sem elementos verdadeiros na lista
