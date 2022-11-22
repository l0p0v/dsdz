# coding=utf-8
x = 0

if x > 2:
    message = "if only 1 were greater than two..."
elif x > 3:
    message = "elif stands for 'else if'"
else:
    message = "when all else fails use else (if you want to)"

parity = "even" if x % 2 == 0 else "odd"

while x < 10:
    print(f"{x} is less than 10")
    x += 1

for x in range(10):
    print(f"{x} is less than 10")

for x in range(10):
    if x == 3:
        continue  # vai para a próxima iteração imediatamente
    if x == 5:
        break  # sai do loop completamente
    print(x)
