# Используем базовый образ с Python
FROM python:3.12-slim

# Создаем рабочую директорию
WORKDIR /app

# Копируем файлы приложения в контейнер
COPY req.txt req.txt
COPY app.py app.py
COPY ./templates templates

# Устанавливаем зависимости для Python
RUN pip3 install -r req.txt

# Устанавливаем curl
RUN apt-get update && \
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/*

# Запускаем приложение
CMD ["python3", "app.py"]
