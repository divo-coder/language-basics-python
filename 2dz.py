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
"""
my_list = [7, 5, 3, 3, 2]
print(my_list)
num = int(input("Введите число: "))
for i in range(len(my_list)):
    if my_list[i] == num:
        my_list.insert(i + 1, num)
        break
    elif my_list[0] < num:
        my_list.insert(0, num)
        break
    elif my_list[-1] > num:
        my_list.append(num)
        break
    elif my_list[i] > num > my_list[i + 1]:
        my_list.insert(i + 1, num)
        break
print(my_list)
