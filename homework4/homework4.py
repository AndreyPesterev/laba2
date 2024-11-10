import random

def get_multiplier():
    while True:
        try:
            # Запрос числа X и проверка, что оно целое и больше 0
            x = int(input("Введите число (X), на которое нужно искать кратные числа: "))
            if x <= 0:
                print("Число должно быть больше 0. Попробуйте снова.")
                continue
            return x
        except ValueError:
            print("Неверный ввод. Убедитесь, что вы ввели целое число.")

def generate_random_numbers(size=10, range_min=0, range_max=200):
    # Генерация случайного списка чисел
    return [random.randint(range_min, range_max) for _ in range(size)]

def find_multiples(numbers, x):
    # Используем лямбда-функцию для фильтрации чисел, кратных X
    return list(filter(lambda num: num % x == 0, numbers))

def main():
    print("Программа для поиска чисел, кратных заданному числу.")
    
    x = get_multiplier()
    
    # Генерация списка чисел и вывод его пользователю
    random_numbers = generate_random_numbers()
    print(f"Сгенерированные числа: {random_numbers}")
    
    # Поиск чисел, кратных X
    multiples = find_multiples(random_numbers, x)
    
    # Проверка наличия кратных чисел и вывод результатов
    if multiples:
        print(f"Числа, кратные {x}: {multiples}")
    else:
        print(f"Чисел, кратных {x}, не найдено в списке.")

if __name__ == "__main__":
    main()
