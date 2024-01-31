def total_salary(path):
    total_salary_sum = 0
    total_developers = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                # Розділяємо рядок на ім'я та заробітну плату
                name, salary_str = line.strip().split(',')
                
                # Перетворюємо заробітну плату в число і додаємо до загальної суми
                salary = int(salary_str)
                total_salary_sum += salary
                
                # Збільшуємо кількість розробників
                total_developers += 1

        # Обчислюємо середню заробітну плату (якщо кількість розробників більше 0)
        average_salary = total_salary_sum // total_developers if total_developers > 0 else 0

        return total_salary_sum, average_salary

    except FileNotFoundError:
        print(f"Помилка: Файл '{path}' не знайдено.")
        return None
    except Exception as e:
        print(f"Помилка: {e}")
        return None

# Приклад використання:
result = total_salary("C:\\Projects\\emp.txt")

if result is not None:
    total, average = result
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
