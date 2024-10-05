# Используем базовый образ с Python
FROM ubuntu:24.10

# Создаем рабочую директорию
WORKDIR /app

COPY script.sh script.sh
RUN chmod +x script.sh
ENTRYPOINT ["bash", "script.sh"]
CMD ["tail", "-f"]