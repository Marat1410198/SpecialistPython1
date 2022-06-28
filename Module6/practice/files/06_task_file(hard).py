# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы, то их ЗП уменьшается пропорционально,
# а за каждый час переработки они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

def wage (norm_hours, fact_hours, dollar):
    if int(norm_hours) >= int(fact_hours):
        money = int(dollar) / int(norm_hours) * int(fact_hours)
        return round(money,2)
    else:
        money = int(dollar) / int(norm_hours) * ((int(fact_hours) - int(norm_hours)) * 2) + int(dollar)
        return round(money,2)

hours_of_list = []
workers_list = []

with open("data/workers", "r", encoding="UTF-8") as f:
    for line in f:
            workers_list += line.split()

with open("data/hours_of", "r", encoding="UTF-8") as f:
    for line in f:
            hours_of_list += line.split()

    total_list = []

    for i in range(5, len(workers_list)):
        for j in range(5, len(hours_of_list)):
            if workers_list[i] == hours_of_list[j] and workers_list[i - 1] == hours_of_list[j - 1]:
                total_list.append(workers_list[i - 1] + "\t" * 2 + workers_list[i] + "\t" * 2
                + str(wage(workers_list[i + 3], hours_of_list[j + 1], workers_list[i + 1])))
                
with open("data/payroll", "w", encoding="UTF-8") as f:
    f.write("Имя \t\tФамилия \t Зарплата за отр.время\n")
    for el in total_list:
        f.write(str(el) + "\n")
