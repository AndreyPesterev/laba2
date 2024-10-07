import random

def find_multiples():
    # Генерируем список случайных чисел от 0 до 200, размер списка - 10
    numbers = [random.randint(0, 200) for _ in range(10)]
    # Запрашиваем число X, кратные которому будем искать
    X = int(input("Введите число X: "))
    # Ищем числа, кратные X, используя лямбда-функцию
    multiples = list(filter(lambda num: num % X == 0, numbers))
    # Выводим результаты
    print(f"Сгенерированные числа: {numbers}")
    print(f"Числа, кратные {X}: {multiples}")


find_multiples()
