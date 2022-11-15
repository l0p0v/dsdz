for i in list(range(1, 6)):
    print(i)  # primeira linha para o bloco "for i"
    for j in list(range(1, 6)):
        print(j)  # primeira linha para o bloco "for j"
        print(i + j)  # última linha para o bloco "for j"
    print(i)  # última linha para o bloco "for i"
print("done looping")

long_winded_computation = (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 +
                           13 + 14 + 15 + 16 + 17 + 18 + 19 + 20)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
easier_to_read_list_of_lists = [[1, 2, 3],
                                [4, 5, 6],
                                [7, 8, 9]]

two_plus_three = 2 + \
                 3
