print('Добро ожаловать в детейлинг центр')
choose = input('какую услугу вы бы хотели получить: тонировка (1) , полировка (2), мойка (3)')
if '1' == choose:
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
elif "2" == choose:
    choose = input("какую бы вы хотели: глубокую (1), поверхностную (2)")
    if '1' == choose:
        print("можем селать")
    elif "2" == choose:
        print("можем прям щас, мастер на месте")
elif "3" == choose:
    choose = input("какого вида мойку желаете быструю (1), усиленную (2)")
    if '1' == choose:
        print("сделаем за 15 минут")
    elif "2" == choose:
        print("мастер сейчас занят")
