from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    # Ініціалізуємо словник для зберігання ім'я користувача за днем тижня
    birthdays_per_week = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
        "Saturday": [],
        "Sunday": [],
    }

    # Отримуємо поточну дату
    today = date.today()

    # Проходимося по кожному користувачеві в списку
    for user in users:
        # Отримуємо день народження користувача
        birthday = user["birthday"]

        # Якщо день народження минув у цьому році, переносимо його на наступний рік
        if birthday.year < today.year:
            birthday = birthday.replace(year=today.year + 1)

        # Перевіряємо, чи день народження входить в наступний тиждень
        if today <= birthday < today + timedelta(days=7):
            # Визначаємо день тижня для дня народження
            day_of_week = birthday.strftime("%A")

            # Перевіряємо, чи день народження випадає на вихідний
            if day_of_week in ["Saturday", "Sunday"]:
                # Якщо так, переносимо його на понеділок
                birthday += timedelta(days=1)
                day_of_week = "Monday"

            # Додаємо ім'я користувача до відповідного дня тижня
            birthdays_per_week[day_of_week].append(user["name"])

    # Видаляємо дні тижня, для яких немає відзначених народжень
    birthdays_per_week = {
        day_name: names for day_name, names in birthdays_per_week.items() if names
    }

    return birthdays_per_week


# Якщо цей файл використовується як вхідний (основна програма)
if __name__ == "__main__":
    # Приклад використання функції зі списком користувачів
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
        # Додайте інших користувачів за потребою
    ]

    # Отримуємо результат виклику функції
    result = get_birthdays_per_week(users)

    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
