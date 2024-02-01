def get_cats_info(path):
    # створюємо пустий словник
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                # Розділяємо рядок на айді, ім'я та вік
                id, name, age = line.strip().split(',')
                # додаємо в словник
                cats_info.append({"id": id, "name": name, "age": age})
        return cats_info

    # обробка помилок
    except FileNotFoundError:
        print(f"Помилка: Файл '{path}' не знайдено.")
        return None
    except Exception as e:
        print(f"Помилка: {e}")
        return None
    

cats_info = get_cats_info("C:\\Projects\\cats.txt")
if cats_info is not None:
    for cat in cats_info:
        print(f"ID: {cat['id']}, Name: {cat['name']}, Age: {cat['age']}")