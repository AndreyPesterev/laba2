import random

def play_game():
    options = ["камень", "ножницы", "бумага"]

    # Игрок выбирает опцию
    player_choice = input("Выберите: камень, ножницы или бумага: ").lower()

    # Компьютер случайным образом выбирает опцию
    computer_choice = random.choice(options)

    # Печатаем выборы
    print(f"Вы выбрали: {player_choice}")
    print(f"Компьютер выбрал: {computer_choice}")

    # Определяем победителя
    if player_choice == computer_choice:
        print("Ничья!")
    elif (player_choice == "камень" and computer_choice == "ножницы") or \
         (player_choice == "ножницы" and computer_choice == "бумага") or \
         (player_choice == "бумага" and computer_choice == "камень"):
        print("Вы победили!")
    else:
        print("Вы проиграли!")

# Запуск игры
play_game()
