# Дан кортеж заполненный целыми числами
# Найдите самый большой элемент кортежа
tup = (2, 4, 6, -4, 12, 0, 5)
total = 0

for i in tup:
    if total < i:
        total = i

print(total)
