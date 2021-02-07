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