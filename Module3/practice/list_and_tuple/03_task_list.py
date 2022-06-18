# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех элементов.

import random

n = int(input("Количество элементов в списке:"))
numbers = []
count = 0

for _ in range(n):
    numbers.append(random.randint(-10, 10))
print(numbers)

for i in numbers:
    count += i
print(count)
