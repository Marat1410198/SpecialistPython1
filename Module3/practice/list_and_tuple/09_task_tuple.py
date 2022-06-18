# Дано 3 кортежа заполненные произвольными целыми числами.
# Найдите количество элементов, которые встречаются во всех трех кортежах.

numbers1 = (1, 8, 12, 45, 68)
numbers2 = (45, 68, 85, 12)
numbers3 = (85, 12, 68, 88)
my_list = []

for i in numbers1:
    for n in numbers2:
        if i == n:
            my_list.append(n)

count = 0
for i in my_list:
    for n in numbers3:
        if i == n:
            count += 1

print(count)
