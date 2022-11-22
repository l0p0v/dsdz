# coding=utf-8
single_quoted_string = 'data science'
double_quoted_string = "data science"

tab_string = "\t"  # representa o caractere 'tab'
print(len(tab_string))  # 1

not_tab_string = r"\t"  # representa os caracteres '\' e 't'
print(len(not_tab_string))  # 2

print(multi_line_string := """esta é a primeira linha,
esta é a segunda
e esta é a terceira.""")
