from datetime import datetime

def get_user_birthdate():
    while True:
        birthdate_input = input("Введите дату рождения (дд/мм/гггг): ")
        
        try:
            # Проверка формата даты
            birthdate = datetime.strptime(birthdate_input, "%d/%m/%Y")
            
            # Проверка, что введённая дата не в будущем
            if birthdate > datetime.now():
                print("Дата рождения не может быть в будущем. Попробуйте снова.")
                continue
            
            return birthdate
        except ValueError:
            print("Неверный формат даты. Убедитесь, что дата указана в формате дд/мм/гггг.")

def calculate_age(birthdate):
    today = datetime.now()
    age = today.year - birthdate.year
    
    # Проверка, был ли день рождения в этом году
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1

    return age

def main():
    print("Программа для расчёта возраста.")
    birthdate = get_user_birthdate()
    age = calculate_age(birthdate)
    print(f"Ваш возраст: {age} лет.")

if __name__ == "__main__":
    main()

