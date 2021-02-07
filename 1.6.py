distance = int(input('Введите результат пробежки в первый день, км: '))
target = int(input('Введите значение цели, км: '))
i = 1
while distance < target:
    print(i, "день :", round(distance, 2), "км")
    distance = distance * 1.1
    i = i + 1
print(i, "день :", round(distance, 2), "км")
print("Вы достигнете желаемый результат на", i, "день.")