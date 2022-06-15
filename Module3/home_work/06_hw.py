# Данные о товарах на складе хранятся в словаре
items = [
    {
        "name": "Кроссовки",
        "brand": "adidas",
        "price": 3440
    },
    {
        "name": "Кепка",
        "brand": "reebok",
        "price": 3500
    },
    {
        "name": "Рюкзак",
        "brand": "reebok",
        "price": 4800
    },
    {
        "name": "Шорты",
        "brand": "puma",
        "price": 2500
    },
    {
        "name": "Шорты",
        "brand": "adidas",
        "price": 2750
    },
    {
        "name": "Футболка",
        "brand": "puma",
        "price": 1700
    },
]

brand = []
for i in range(6):
    brand.append(items[i].get("brand"))

# Найдите:
print("Товары на складе представлены брэндами:", *set(brand), sep=" ")

name = []
for i in range(6):
    name.append(items[i].get("name"))

count = 0
total = 0
clothes = ""

for i in name:
    count = name.count(i)
    if count >= total:
        total = count
        clothes = i

print("На складе больше всего товаров: ",clothes)

price = []
for i in range(6):
    price.append(items[i].get("price"))

print("На складе самый дорогой товар: ",items[price.index(max(price))]["name"])
