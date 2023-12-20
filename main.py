import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os


def resize_and_save_images():
    # Открытие окна для выбора файлов
    file_paths = filedialog.askopenfilenames(filetypes=[("", "*")])
    if not file_paths:
        return

    # Открытие окна для выбора папки сохранения
    save_directory = filedialog.askdirectory()
    if not save_directory:
        return

    # Изменение размера и сохранение каждого изображения
    for file_path in file_paths:
        with Image.open(file_path) as img:
            # Проверка размера изображения
            if img.size[0] > 2048 or img.size[1] > 2048:
                # Изменение размера до 2K, если изображение больше
                img_resized = img.resize((2048, 2048), Image.Resampling.LANCZOS)
            else:
                # Использование исходного изображения, если оно меньше 2K
                img_resized = img.copy()

            # Сохранение изображения
            save_path = os.path.join(save_directory, os.path.basename(file_path))
            img_resized.save(save_path)


# Создание окна
root = tk.Tk()
root.title("Image Resizer")

# Добавление кнопки
button = tk.Button(root, text="Выбрать и изменить размер изображений", command=resize_and_save_images)
button.pack(pady=20)

# Запуск цикла обработки событий
root.mainloop()
