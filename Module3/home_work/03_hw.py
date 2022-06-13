# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

import random

n = int(input("Количество элементов в списке:"))
numbers = []
numbers_positive = []

for i in range(n):
    numbers.append(random.randint(-100, 100))
print(numbers)

for i in numbers:
    if i > 0 and i % 2 == 0:
        numbers_positive.append(i)
print(numbers_positive)
