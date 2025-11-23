from itertools import repeat

while True:
    answer = input("какую вы хотите тониовку: 5 % (1), 10% (2), 15% (3)")
    if answer == "1":
        print("сори нету")
    if answer == "2":
        print("сори тоже")
    if answer == "3":
        print("да без проблем сделаем")
    repeat = input("хотите другой процент тонировки?(да/нет)")
    if repeat.strip().lower() == "нет":
        print("можно вай нот")
        break
