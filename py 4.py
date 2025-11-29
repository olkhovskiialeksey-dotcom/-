class Person:
    def __init__(self, name, attempt=2, knowledge=0):
        self.name = name
        self.attempt = attempt
        self.knowledge = knowledge
        self.reward_given = False

    def decrease_attempt(self, amount):
        self.attempt -= amount
        print(f"Количество попыток уменьшилось на {amount}. Осталось {self.attempt}")

    def increase_knowledge(self, amount):
        self.knowledge += amount
        print(f"ваш баланс увеличился на {amount}00000 рублей.")

    def give_reward(self):
        if not self.reward_given and self.knowledge >= 1:
            print(f"Поздравляем, {name}! вы выйграли миллион")
            self.reward_given = True
            exit()

def millioner():
    try:
        while person.attempt > 0:
            print("Хорошо, ответьте на вопрос!")
            answer = input("сколько костей в организме: 210(1), 206(2), 192(3)?")

            if not answer.isdigit() or int(answer) not in [1, 2, 3]:
                raise ValueError("Необходимо ввести целое число от 1 до 3!")

            if answer == '2':
                print("правильно!")
                person.increase_knowledge(1)
                gistology()
            elif answer == '1':
                print("Нет!")
                person.decrease_attempt(1)
            elif answer == '3':
                print("Нет!")
                person.decrease_attempt(1)

            repeat = input("Вы уверены в своем выборе?(да/нет):")
            if repeat.strip().lower() != 'нет':
                print("окей!")
                break
        else:
            print("извините вы проиграли, повезет завтра!")
    except Exception as err:
        print(f"Произошла ошибка: {err}")

def anatomy():
    try:
        print("вопрос из анатомии")
        answer = input("сколько пар черепных нервов:12(1), 5(2), 6(3)?")

        if not answer.isdigit() or int(answer) not in [1, 2, 3]:
            raise ValueError("Необходимо ввести целое число от 1 до 3!")

        if answer == '1':
            print("верно!")
            person.increase_knowledge(1)
            person.give_reward()
        else:
            print("неправильно.")
            person.decrease_attempt(1)
    except Exception as err:
        print(f"Произошла ошибка: {err}")

def millioner_2():
    try:
        while person.attempt > 0:
            print("Хорошо, ответьте на вопрос!")
            answer = input("сколько хромосом у человека: 45(1), 47(2), 46(3)?")

            if not answer.isdigit() or int(answer) not in [1, 2, 3]:
                raise ValueError("Необходимо ввести целое число от 1 до 3!")

            if answer == '3':
                print("правильно")
                person.increase_knowledge(1)
                anatomy()
            elif answer == '1':
                print("не верно")
                person.decrease_attempt(1)
            elif answer == '2':
                print("не верно")
                person.decrease_attempt(1)

            repeat = input("вы уверены в своем выборе?(да/нет):")
            if repeat.strip().lower() != 'нет':
                print("В другой раз")
                break
        else:
            print("что то вы заседелись почитайте ка атлас анатомии!")
    except Exception as err:
        print(f"Произошла ошибка: {err}")

def gistology():
    try:
        print("вопрос по гистологии")
        answer = input("сколько слоев в сетчатке: 10(1), 11(2), 13(3)?")

        if not answer.isdigit() or int(answer) not in [1, 2, 3]:
            raise ValueError("Необходимо ввести целое число от 1 до 3!")

        if answer == '2':
            print("правильно")
            person.increase_knowledge(1)
            person.give_reward()
        else:
            print("Неверно.")
            person.decrease_attempt(1)
    except Exception as err:
        print(f"Произошла ошибка: {err}")

print("Приветствуем в игре кто хочет стать миллинером!")
name = input("Введите ваше имя:")
person = Person(name)

enter = input("Желаете присоединиться (да/нет)?")

if 'да' == enter:
    print(f"Добро пожаловать, {name}!")

    answer = input("за какую сумму вы будете бороться? от нее зависит сложность: 5000(1), 500 000(2), 5 000 000(3)?")

    if not answer.isdigit() or int(answer) not in [1, 2, 3,]:
        raise ValueError("Необходимо ввести целое число от 1 до 3!")

    if answer == '1':
        millioner()
    elif answer == '2':
        millioner_2()
    elif answer == '3':
        print("столько бабла нету!")

elif 'нет' == enter:
    print("тогда иди домой!")