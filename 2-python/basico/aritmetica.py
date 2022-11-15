def double(x):
    """
    Aqui é onde você coloca um docstring (cadeia de caracteres de documentação) opcional
    que explica o que a função faz.
    Por exemplo, esta função multiplica sua entrada por 2
    """
    return x * 2


def apply_to_one(f):
    """
    Chama a função f com 1 como seu argumento
    """
    return f(1)


my_double = double  # refere-se à função definida anteriormente
x = apply_to_one(my_double)  # é igual a 2

y = apply_to_one(lambda z: z + 4)  # é igual a 5

another_double = lambda z: 2 * z  # não faça isso


def another_double2(z): return z * 2  # faça isso


def my_print(message="my default message"): print(message)


my_print("hello")  # exibe 'hello'
my_print()


def subtract(a=0, b=0): return a - b


print(subtract(10, 5))  # retorna 5
print(subtract(0, 5))  # retorna -5
print(subtract(b=5))  # mesmo que o anterior
