
def printLine(count=20, symbol='*'):
    for i in range(count):
        print(symbol, end='')
    print()

# a = int(input("count = "))
# a = open()
# printLine()
# printLine(45)
# printLine(15, '@')
# printLine(5, '+')
# printLine(35, '=')


# a = 10
#
# def func():
#     global a
#     print("start func")
#     #a = 20
#     print(a)
#     print("end func")
#
#
# func()
# print(a)


import random

result = {"comp":0, "user":0}

def game(user_choice):
    user_choice = str.upper(user_choice)
    comp_choice = random.choice("KNB")
    print(f"Гравець - {user_choice}, Комп'ютер - {comp_choice}")
    if user_choice == comp_choice:
        return "D"
    elif user_choice == "K" and comp_choice == "N" or user_choice == "B" and comp_choice == "K" or user_choice == "N" and comp_choice == "B":
        return "U"
    else:
        return "C"

def print_result(result, winner):
    if winner == "D":
        print("В цьому раунді нічья")
    elif winner == "U":
        print("В цьому раунді переміг гравець")
        result["user"] += 1
    elif winner == "C":
        print("В цьому раунді переміг комп'ютер")
        result["comp"] += 1
    print(f'Гравець - {result["user"]}, Комп\'ютер {result["comp"]}')


for i in range(1, 4):
    print(f" ======= РАУНД № {i} =======")
    user_choice = input("Виберіть K, N, B - ")
    print_result(result, game(user_choice))
    print()