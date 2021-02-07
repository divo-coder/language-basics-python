
my_list = [i for i in input('Введите список: ').split()]
for i in range(1, len(my_list), 2):
    my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]
print(' '.join([str(i) for i in my_list]))
"""
"""
seasons_list = ["зима", "весна", "лето", "осень"]
seasons_dict = {1: "зима", 2: "весна", 3: "лето", 4: "осень"}
month = int(input("Введите число месяца "))
if month == 1 or month == 12 or month == 2:
        print(seasons_dict.get(1), " - список")
        print(seasons_list[0], " - словарь")
elif month == 3 or month == 4 or month == 5:
    print(seasons_dict.get(2), " - список")
    print(seasons_list[1], " - словарь")
elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(3), " - список")
    print(seasons_list[2], " - словарь")

elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(4), " - список")
    print(seasons_list[3], " - словарь")
else:
    print("Необходимо ввести число от 1 до 12")

"""
"""
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
