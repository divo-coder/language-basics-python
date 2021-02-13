proceeds = int(input('Введите значение выручки : '))
costs = int(input('Введите значение издержек: '))
if proceeds > costs:
    print('Фирма работает с прибылью')
elif proceeds < costs:
    print('фирма работает с убытками')
else:
    print("компания работает в 0")
ren = (proceeds - costs) / proceeds
print(f'Рентабельность составляет: {ren:.1f}')
n = int(input('Введите количество сотрудников: '))
print(f'Прибыль фирмы в расчете на одного сотрудника: {(proceeds - costs) / n:.0f}')
