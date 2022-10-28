# 1. Получить ввод пользователя
# 2. Выбрать свой вариант
# 3. Определить кто победил
# 4. Добавить подсчёт очков
# 5. Проверка неправильного ввода

# камень > ножницы
# ножницы > бумага
# бумага > камень

import random


choices = ("камень", "ножницы", "бумага")
user_win_cases = {
    "камень": "ножницы",
    "ножницы": "бумага",
    "бумага": "камень",
}
user_score = 0
bot_score = 0


def choose_winer(user_choice):
    global user_score, bot_score
    bot_choice = random.choice(choices)
    if user_win_cases[user_choice] == bot_choice:
        print(f"Ты победил! Компьютер выбрал {bot_choice}")
        user_score += 1

    elif user_choice == bot_choice:
        print(f"Ничья! Компьютер выбрал {bot_choice}") 

    else:
        print(f"Ты проиграл! Компьютер выбрал {bot_choice}")
        user_score -= 1
        bot_score += 1

    print(f"твой счет:{user_score}\nсчет бота:{bot_score}")


while True:
    user_choice = input("Камень, ножницы или бумага? ")
    if user_choice == 'выход':
        break
    elif user_choice.lower() in user_win_cases:
        choose_winer(user_choice)
        if user_score < 0 or bot_score > 5:
            print(f'ты проиграл\nсчет бота:{bot_score}')
            break
    else:
        print("неверно")
        