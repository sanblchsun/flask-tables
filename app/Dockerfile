# Выкачиваем из dockerhub образ с python версии 3.9
FROM python:3.8
# Устанавливаем рабочую директорию для проекта в контейнере
WORKDIR /app
# Скачиваем/обновляем необходимые библиотеки для проекта 
COPY requirements.txt /app
RUN apt-get update -y
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# |ВАЖНЫЙ МОМЕНТ| копируем содержимое папки, где находится Dockerfile, 
# в рабочую директорию контейнера
COPY . /app
# Устанавливаем порт, который будет использоваться для сервера
EXPOSE 5000
