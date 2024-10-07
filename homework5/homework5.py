def get_number():
    # Генератор нечётных чисел в диапазоне 30
    for num in range(30):
        if num % 2 != 0:
            yield num
# Вызов генератора
gen = get_number()
# Получаем первое, пятое и последнее значение
first = None
fifth = None
last = None
for i, val in enumerate(gen, start=1):
    if i == 1:
        first = val
    elif i == 5:
        fifth = val
    last = val  # Последнее значение будет записано при каждом проходе
print(f"Первое значение: {first}")
print(f"Пятое значение: {fifth}")
print(f"Последнее значение: {last}")
