distance = int(input('Введите результат пробежки в первый день, км: '))
target = int(input('Введите значение цели, км: '))
i = 1
while distance < target:
    print(i, "день :", round(distance, 2), "км")
    distance = distance * 1.1
    i = i + 1
print(i, "день :", round(distance, 2), "км")
print("Вы достигнете желаемый результат на", i, "день.")
"""
# допиленное решение
while True:
    distance = int(input('Введите результат пробежки в первый день, км: '))
    target = int(input('Введите значение цели, км: '))
    i = 1
    if target < distance:
        print ("введены некорректные данные")
    else:
        while distance < target:
            print(f"{i} день {distance:.2f} км")
            distance = distance * 1.1
            i = i + 1
        print(f"{i} день {distance:.2f} км")
        print(f"Вы достигнете желаемый результат на {i} день.")
        break
"""
