import os
import shutil
import settings

def display_menu():
    print("\nМеню файлового менеджера:")
    print("1. Создать папку")
    print("2. Удалить папку")
    print("3. Перейти в папку")
    print("4. Перейти на уровень вверх")
    print("5. Создать файл")
    print("6. Записать текст в файл")
    print("7. Просмотреть содержимое файла")
    print("8. Удалить файл")
    print("9. Скопировать файл")
    print("10. Переместить файл")
    print("11. Переименовать файл")
    print("0. Выйти из программы")

def create_folder():
    folder_name = input("Введите имя папки: ")
    try:
        os.mkdir(os.path.join(settings.WORKING_DIRECTORY, folder_name))
        print(f"Папка {folder_name} успешно создана.")
    except FileExistsError:
        print(f"Папка {folder_name} уже существует.")

def delete_folder():
    folder_name = input("Введите имя папки: ")
    try:
        os.rmdir(os.path.join(settings.WORKING_DIRECTORY, folder_name))
        print(f"Папка {folder_name} успешно удалена.")
    except FileNotFoundError:
        print(f"Папка {folder_name} не найдена.")
    except OSError:
        print(f"Невозможно удалить папку {folder_name}, так как она не пуста.")

def move_to_folder():
    folder_name = input("Введите имя папки: ")
    new_path = os.path.join(settings.WORKING_DIRECTORY, folder_name)
    if os.path.exists(new_path) and os.path.isdir(new_path):
        settings.WORKING_DIRECTORY = new_path
        print(f"Перешли в папку {folder_name}.")
    else:
        print(f"Папка {folder_name} не существует.")

def move_up():
    parent_dir = os.path.dirname(settings.WORKING_DIRECTORY)
    if parent_dir != settings.WORKING_DIRECTORY:
        settings.WORKING_DIRECTORY = parent_dir
        print("Перешли на уровень вверх.")
    else:
        print("Вы уже находитесь в корневой папке.")

def create_file():
    file_name = input("Введите имя файла: ")
    file_path = os.path.join(settings.WORKING_DIRECTORY, file_name)
    try:
        with open(file_path, 'w'):
            pass
        print(f"Файл {file_name} успешно создан.")
    except FileExistsError:
        print(f"Файл {file_name} уже существует.")

def write_to_file():
    file_name = input("Введите имя файла: ")
    text = input("Введите текст для записи: ")
    file_path = os.path.join(settings.WORKING_DIRECTORY, file_name)
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text)
        print(f"Текст успешно записан в файл {file_name}.")
    except FileNotFoundError:
        print(f"Файл {file_name} не найден.")

def view_file():
    file_name = input("Введите имя файла: ")
    file_path = os.path.join(settings.WORKING_DIRECTORY, file_name)
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"Файл {file_name} не найден.")

def delete_file():
    file_name = input("Введите имя файла: ")
    file_path = os.path.join(settings.WORKING_DIRECTORY, file_name)
    try:
        os.remove(file_path)
        print(f"Файл {file_name} успешно удален.")
    except FileNotFoundError:
        print(f"Файл {file_name} не найден.")

def copy_file():
    file_name = input("Введите имя файла: ")
    destination_folder = input("Введите имя папки назначения: ")
    source_file = os.path.join(settings.WORKING_DIRECTORY, file_name)
    destination_path = os.path.join(settings.WORKING_DIRECTORY, destination_folder)
    try:
        shutil.copy(source_file, destination_path)
        print(f"Файл {file_name} успешно скопирован в папку {destination_folder}.")
    except FileNotFoundError:
        print(f"Файл {file_name} не найден.")
    except shutil.Error as e:
        print(f"Ошибка при копировании файла: {e}")

def move_file():
    file_name = input("Введите имя файла: ")
    destination_folder = input("Введите имя папки назначения: ")
    source_file = os.path.join(settings.WORKING_DIRECTORY, file_name)
    destination_path = os.path.join(settings.WORKING_DIRECTORY, destination_folder)
    try:
        shutil.move(source_file, destination_path)
        print(f"Файл {file_name} успешно перемещен в папку {destination_folder}.")
    except FileNotFoundError:
        print(f"Файл {file_name} не найден.")
    except shutil.Error as e:
        print(f"Ошибка при перемещении файла: {e}")

def rename_file():
    old_name = input("Введите текущее имя файла: ")
    new_name = input("Введите новое имя файла: ")
    old_path = os.path.join(settings.WORKING_DIRECTORY, old_name)
    new_path = os.path.join(settings.WORKING_DIRECTORY, new_name)
    try:
        os.rename(old_path, new_path)
        print(f"Файл {old_name} успешно переименован в {new_name}.")
    except FileNotFoundError:
        print(f"Файл {old_name} не найден.")
    except FileExistsError:
        print(f"Файл {new_name} уже существует.")

def main():
    while True:
        display_menu()
        choice = input("Введите номер действия (0-11): ")
        if choice == '0':
            print("Выход из программы.")
            break
        elif choice == '1':
            create_folder()
        elif choice == '2':
            delete_folder()
        elif choice == '3':
            move_to_folder()
        elif choice == '4':
            move_up()
        elif choice == '5':
            create_file()
        elif choice == '6':
            write_to_file()
        elif choice == '7':
            view_file()
        elif choice == '8':
            delete_file()
        elif choice == '9':
            copy_file()
        elif choice == '10':
            move_file()
        elif choice == '11':
            rename_file()
        else:
            print("Неверный выбор. Пожалуйста, введите число от 0 до 11.")

if __name__ == "__main__":
    main()
