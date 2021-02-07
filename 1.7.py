
proceeds = int(input('Введите значение выручки : '))
costs = int(input('Введите значение издержек: '))
if proceeds > costs:
    print('Фирма работает в плюс')
else:
    print('Выручки нет')
ren = (proceeds - costs) / proceeds
print('Рентабельность составляет: ', ren)
n = int(input('Введите количество сотрудников: '))
print('Прибыль фирмы в расчете на одного сотрудника: ', (proceeds - costs) / n)
