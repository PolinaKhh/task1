import os
import shutil
from tkinter import filedialog, messagebox, Tk


def select_folder():
    """
    Открывает диалоговое окно с файлом для выбора папки и считывает путь к папке как строку
    """
    root = Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title="Select folder")
    return folder_path



def create_folders(source_folder):
    """
    Создаю папки с департаментами и названием файлов, проверяю существуют ли уже такие папки
    """
    department_folder = os.path.join(source_folder, "Departments")
    other_folder = os.path.join(source_folder, "Other")
    if not os.path.exists(department_folder):
        os.mkdir(department_folder)
    if not os.path.exists(other_folder):
        os.mkdir(other_folder)


def sort_files(source_folder):
    """
    Сортирую файлы в исходной папке на основе названия их департамента и типа файла
    """
    department_folder = os.path.join(source_folder, "Departments")
    other_folder = os.path.join(source_folder, "Other")

    for filename in os.listdir(source_folder):
        # Игнорирую директории
        if os.path.isdir(os.path.join(source_folder, filename)):
            continue

        # Получаю название департамента из названия файла
        department_name = filename.split("_")[0]

        # Если название департамента не обнаружено, то отправляю этот файл в другое
        if not department_name:
            shutil.move(os.path.join(source_folder, filename), other_folder)
        else:
            # Создаю папку департамента и проверяю существует ли уже такая папка
            department_folder_path = os.path.join(department_folder, department_name)
            if not os.path.exists(department_folder_path):
                os.mkdir(department_folder_path)

            # Перемещаю файл в созданную директорию Имя департамент/тип файла
            file_extension = os.path.splitext(filename)[1]
            file_path = os.path.join(source_folder, filename)
            if file_extension:
                file_extension_folder = os.path.join(department_folder_path, file_extension[1:].upper())
                if not os.path.exists(file_extension_folder):
                    os.mkdir(file_extension_folder)
                shutil.move(file_path, file_extension_folder)
            else:
                shutil.move(file_path, department_folder_path)


if __name__ == "__main__":
    print('Выберете папку, которую необходимо отсортировать')
    source_folder = select_folder()
    print('Создаю папки....')
    create_folders(source_folder)
    print('Сортирую файлы....')
    sort_files(source_folder)

    # Показываю сообщение-уведомление что всё готово
    messagebox.showinfo("Готово!", "Файлы отсортированы по папкам")
