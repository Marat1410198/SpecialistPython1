# Дан файл data/info.txt, в каждой строке которого содержится строка или целое число
# Найдите сумму всех чисел, пропуская все строки содержащие не числовые значения
my_list = []
sum_int = 0
with open("info.txt", "r") as f:
    for line in f:
        my_list += line.split("\n")
    print(my_list)

    for number in my_list:
        try:
            sum_int += int(number)
        except ValueError:
            continue
    print(sum_int)
