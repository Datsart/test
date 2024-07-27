FROM ubuntu:latest

WORKDIR /app

COPY ./script.sh .

# Используем ENTRYPOINT в виде строки для запуска команд в /bin/bash -c
ENTRYPOINT ["bash", "./script.sh"]

# CMD оставляем пустым, чтобы переданные команды могли быть выполнены
CMD ["echo 'Welcome to the container! Run your commands here.'"]
