str1 = input("Введите строку: ")
word = []
num = 1
for i in range(str1.count(' ') + 1):
    word = str1.split()
    if len(str(word)) <= 10:
        print(num, word[i])
        num += 1
    else:
        print(num, word[i][0:10])
        num += 1