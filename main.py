import os
from tkinter import Tk, filedialog, Button, Label
from PIL import Image

def convert_tga_to_png(folder_path):
    # Создаем путь к папке для сохранения PNG файлов
    png_folder_path = os.path.join(folder_path, "PNG 8 bit")
    if not os.path.exists(png_folder_path):
        os.makedirs(png_folder_path)

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".tga"):
            file_path = os.path.join(folder_path, filename)
            image = Image.open(file_path).convert("RGBA")  # Открываем исходное изображение

            # Создаем новое изображение с фоном (белым) для замены прозрачности
            background = Image.new("RGB", image.size, (255, 255, 255))
            background.paste(image, mask=image.split()[3])  # 3 означает альфа-канал в RGBA

            # Преобразование в 8-битный формат с палитрой
            image = background.convert("RGB").quantize(method=Image.FASTOCTREE)

            png_filename = filename[:-4] + '.png'
            png_path = os.path.join(png_folder_path, png_filename)
            image.save(png_path, "PNG")
            print(f"Converted and saved: {png_path}")

    # Вывод сообщения об успешной конвертации
    status_label.config(text="Conversion completed. You can select another folder.")

def select_folder():
    folder_path = filedialog.askdirectory()  # Показываем диалог выбора папки
    if folder_path:  # Если папка выбрана
        convert_tga_to_png(folder_path)
    else:
        # Обновляем статус, если пользователь отменил выбор папки
        status_label.config(text="No folder selected. Please select a folder.")

# Создаем главное окно
root = Tk()
root.title("TGA to PNG Converter")

# Создаем кнопку для выбора папки
select_folder_button = Button(root, text="Select Folder and Convert TGA to PNG", command=select_folder)
select_folder_button.pack(pady=20)

# Добавляем метку для отображения статуса операции
status_label = Label(root, text="Select a folder to start conversion.")
status_label.pack(pady=10)

# Запускаем главный цикл приложения
root.mainloop()
