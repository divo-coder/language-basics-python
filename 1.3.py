#Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = int(input('введите число '))
nn = str(n) + str(n)
nnn = str(n) + str(n) + str(n)
sum = n + int(nn) + int(nnn)
print(sum)3