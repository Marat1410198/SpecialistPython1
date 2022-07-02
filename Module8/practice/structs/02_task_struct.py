# Дан список, заполненный произвольными целыми числами.
# Примечание: для генерации списка используйте функцию написанную на одном из прошлых занятий.
# Получите новый список, элементами которого будут:
#   1. неповторяющиеся(уникальные) элементы исходного списка:
#   например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
#   2. элементы исходного списка, которые не имеют повторений(встречаются только один раз):
#   например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

def gen_list(size, at=-10, to=10):
    import random
    result_list = []
    for _ in range(size):
        result_list.append(random.randint(at, to))
    return result_list

my_list = []
my_list3 = []

my_list = gen_list(10, 1, 10)
my_list2 = list(set(my_list))

for el in my_list:
    if my_list.count(el) == 1:
        my_list3.append(el)

print(my_list)
print(my_list2)
print(my_list3)
