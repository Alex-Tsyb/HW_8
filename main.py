from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    if not users:
        return {}

    # Отримуємо поточну дату
    today = date.today()

    # Визначаємо перший день поточного тижня (понеділок)
    current_week_start = today - timedelta(days=today.weekday())

    # Визначаємо перший день наступного тижня (понеділок)
    next_week_start = current_week_start + timedelta(days=7)

    # Створюємо словник для зберігання днів народжень
    birthdays_per_week = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
        "Saturday": [],
        "Sunday": [],
    }

    # Розподіляємо дні народжень по відповідним дням тижня
    for user in users:
        name = user["name"]
        birthday = user["birthday"]

        # Визначаємо рік дня народження
        birthday_this_year = birthday.replace(year=today.year)

        # Якщо день народження вже минув у цьому році, перевіряємо, чи він наступного тижня
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)

            # Перевірка, чи день народження припадає на вихідний
            if birthday_this_year.weekday() in [5, 6]:  # Saturday or Sunday
                # Переносимо на понеділок
                birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))

        # Визначаємо день тижня для дня народження
        weekday = birthday_this_year.weekday()

        # Перевірка, чи день народження вже минув у цьому тижні або наступному тижні
        if current_week_start <= birthday_this_year < next_week_start:
            # Додаємо ім'я користувача в список відповідного дня тижня
            day_of_week = list(birthdays_per_week.keys())[weekday]

            # Перевірка, чи день народження вже минув у цьому тижні
            if today <= birthday_this_year < next_week_start:
                birthdays_per_week[day_of_week].append(name)

    # Видаляємо ключі, які не мають значень
    birthdays_per_week = {
        day: names for day, names in birthdays_per_week.items() if names
    }

    return birthdays_per_week


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
        # Додайте інших користувачів за потребою
    ]

    result = get_birthdays_per_week(users)

    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
