# ❗ Завдання #1

# Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.

# Вимоги до завдання:

# Функція приймає один параметр: date — рядок, що представляє дату у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09').
# Функція повертає ціле число, яке вказує на кількість днів від заданої дати до поточної. Якщо задана дата пізніша за поточну, результат має бути від'ємним.
# У розрахунках необхідно враховувати лише дні, ігноруючи час (години, хвилини, секунди).
# Для роботи з датами слід використовувати модуль datetime Python.


# Рекомендації для виконання:

# Імпортуйте модуль datetime.
# Перетворіть рядок дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime.
# Отримайте поточну дату, використовуючи datetime.today().
# Розрахуйте різницю між поточною датою та заданою датою.
# Поверніть різницю у днях як ціле число.


# Критерії оцінювання:

# Коректність роботи функції: функція повинна точно обраховувати кількість днів між датами.
# Обробка винятків: функція має впоратися з неправильним форматом вхідних даних.
# Читабельність коду: код повинен бути чистим і добре документованим.


# Приклад:

# Якщо сьогодні 5 травня 2021 року, виклик get_days_from_today("2021-10-09") повинен повернути 157, оскільки 9 жовтня 2021 року є на 157 днів пізніше від 5 травня 2021 року.


from datetime import datetime

def get_days_from_today(date: str) -> int:
    try:
        
        # Convert the date string to a datetime object
        date = datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError:
        raise ValueError('Please enter date in format "YYYY-MM-DD"')
    
    # Get the current date
    today = datetime.today().date()
    
    # Calculate the difference in days
    year_difference = today.year - date.year

    if (today.month, today.day) < (date.month, date.day):
        year_difference -= 1
    return year_difference

# Prompt the user to enter a date
user_date = input('Enter the date in the format  "YYYY-MM-DD": ')

# Print the result
print(get_days_from_today(user_date))