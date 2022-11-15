empty_dict = {}  # Pythonic
empty_dict2 = dict()  # menos Pythonic
grades = {"Joel": 80, "Tim": 95}  # dicionário literal

joels_grade = grades["Joel"]  # é igual a 80

try:
    kates_grade = grades["Kate"]
except KeyError:
    print("no grade for Kate!")

joel_has_grade = "Joel" in grades  # Verdadeiro
kate_has_grade = "Kate" in grades  # Falso

joels_grade = grades.get("Joel", 0)  # é igual a 80
kates_grade = grades.get("Kate", 0)  # é igual a 0
no_ones_grade = grades.get("No One")  # padrão para padrão é None

grades["Tim"] = 99  # substitui o valor antigo
grades["Kate"] = 100  # adiciona uma terceira grade
num_students = len(grades)  # é igual a 3

tweet = {
    "user": "joelgrus",
    "text": "Data Science is Awesome",
    "retweet_count": 100,
    "hashtags": ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}

tweet_keys = tweet.keys()  # lista de chaves
tweet_values = tweet.values()  # lista de valores-chave
tweet_items = tweet.items()  # lista de (chave, valor) tuplas

print("user" in tweet_keys)  # Verdadeiro, mas usa 'list in', mais lento
print("user" in tweet)  # mais Pythonic, usa 'dict in', mais rápido
print("joelgrus" in tweet_values)  # Verdadeiro
