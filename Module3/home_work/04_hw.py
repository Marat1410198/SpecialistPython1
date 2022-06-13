# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь

import random

n = int(input("Количество элементов в списке:"))
numbers = []
numbers_root = []

for i in range(n):
    numbers.append(random.randint(-100, 100))
print(numbers)

for i in numbers:
    if i >= 0 and i ** 0.5 % 1 == 0:
       numbers_root.append(i)
print(numbers_root)
