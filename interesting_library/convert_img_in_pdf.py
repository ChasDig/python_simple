import os
import img2pdf

with open("cat.pdf", "wb") as file:
    # Собираем все изображения в папке в один pdf файл:
    file.write(img2pdf.convert([image for image in os.listdir("cat_image") if image.endswith(".jpg")]))
