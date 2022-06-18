## "Диагонали символами"

### Задание

Даны сторона квадрата. Вывести его диагонали символами #

### Формат входных данных

Дано целое число n, длина стороны квадрата. 1 < n < 20 

### Формат выходных данных

Вывести диагонали квадрата символами # (см. примеры)

#### Примеры

n = 6 
```
#    #
 #  #
  ##
  ##
 #  #
#    #
```
n = 3
```
# #
 #
# #
```
### Решение задачи

```python
n = int(input("n: "))

space_inside = n - 2
space_left = 0
print('#', '#', sep=' ' * (space_inside))
for i in range(1, n + 1):
    if n // 2 > i:
        space_inside -= 2
        space_left += 1
        print(space_left * " ", end='')
        print('#', '#', sep=' ' * space_inside)
    elif n % 2 != 0 and i == n // 2 + 1:
        print((space_left + 1) * " ", end='')
        print('#')
    elif i >= n // 2 + 1:
        print((space_left) * " ", end='')
        print('#', '#', sep=' ' * (space_inside))
        space_inside += 2
        space_left -= 1
```
