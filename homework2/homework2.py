def calculate_age():
    # Запрашиваем у пользователя дату рождения
    birth_day, birth_month, birth_year = map(int, input("Введите дату рождения  формате(день/месяц/год): ").split('/'))
    # Запрашиваем текущую дату
    today_day, today_month, today_year = map(int, input("Введите сегодняшнюю дату в формате (день/месяц/год): ").split('/'))
    # Вычисляем возраст
    age = today_year - birth_year
    # Проверяем, был ли день рождения в этом году
    if (today_month, today_day) < (birth_month, birth_day):
        age -= 1
    return age


age = calculate_age()
print(f"Ваш возраст: {age} лет")
