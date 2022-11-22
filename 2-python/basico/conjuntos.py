# coding=utf-8
s = set()
s.add(1)  # 's' agora é {1}
s.add(2)  # 's' agora é {1, 2}
s.add(2)  # 's' ainda é {1, 2}
x = len(s)  # é igual a 2
y = 2 in s  # é igual a True
z = 3 in s  # é igual a False

stopwords_list = ["a", "an", "at"] + ["yet", "you"]
print("zip" in stopwords_list)  # Falso, mas tem que verificar todos os elementos

stopwords_list = set(stopwords_list)
print("zip" in stopwords_list)  # muito mais rápido para verificar

item_list = [1, 2, 3, 1, 2, 3]
num_items = len(item_list)  # 6
item_set = set(item_list)  # {1, 2, 3}
num_distinct_items = len(item_set)  # 3
distinct_item_list = list(item_set)  # [1, 2, 3]
