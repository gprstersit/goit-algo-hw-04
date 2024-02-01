# parse_input приймає рядок вводу користувача user_input і розбиває його на слова за допомогою методу split(). 
# повертає перше слово як команду cmd та решту як список аргументів *args.
# рядок коду cmd = cmd.strip().lower() видаляє зайві пробіли навколо команди та перетворює її на нижній регістр.
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

# перевіряємо чи номер містить знак + і цифри
# далі додаємо до словника з контактами contacts
def add_contact(args, contacts):
    try:
        name, phone = args
        if not all(char.isdigit() or char == '+' for char in phone):
          return "WARNING MESSAGE: Phone number should contain only digits and '+'."
        contacts[name] = phone
        return "Contact added."
    except ValueError:
        print(f"WARNING MESSAGE: Please enter \"Username\" and \"Phone\" separated by space")

# командою ALL виводимо всі записи в словнику у відповідному форматі
def print_all_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        print("All contacts:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")

# змінюємо існуючий запис, або при відсутності виводимо помилку
def change_contact(args, contacts):
    try:
        name, new_phone = args
        if name in contacts:
            contacts[name] = new_phone
            return f"Phone number for {name} changed."
        else:
            return f"Contact with name {name} not found."
    except ValueError:
        print("WARNING MESSAGE: Please enter \"Username\" and \"New Phone\" separated by space")

# виводимо на екран інформацію про запис, або при відсутності виводимо помилку
def get_contact_phone(args, contacts):
    try:
        name, = args
        if name in contacts:
            return f"{name}'s phone number: {contacts[name]}"
        else:
            return f"Contact with name {name} not found."
    except ValueError:
        print("WARNING MESSAGE: Please enter \"Username\" to get the phone number")

# видаляємо інформацію про запис зі словника, або при відсутності виводимо помилку
def delete_contact(args, contacts):
    try:
        name, = args
        if name in contacts:
            del contacts[name]
            return f"Contact {name} deleted."
        else:
            return f"Contact with name {name} not found."
    except ValueError:
        print("WARNING MESSAGE: Please enter \"Username\" to delete the contact")


# основна програма
def main():
    contacts = {}
    # інструкції для використання
    print("Welcome to the assistant bot!\n\
          List of commands:\n\
          add > example: add UserName Number\n\
          change > example: change UserName NEW_Number\n\
          phone > example: phone UserName\n\
          all > example: all (print all numbers)\n\
          delete > example: delete UserName\n\
          for exit > example: close or exit or quit")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "quit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_contact_phone(args, contacts))
        elif command == "all":
            print_all_contacts(contacts)
        elif command == "delete":
            print(delete_contact(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()