# Пульт охраны банка

Программа подключена к базе данных охраны банка.
На главной странице выходит список охранников, их коды пропусков. При клике на 
имя владельца отобразится страница с списком посещений хранилища охранником,
дата посещения, продолжительность нахождения, подозрительно долое нахождение в
хранилище.
На странице 
    http://0.0.0.0:8000/storage_information/storage_information
выводится список охранников, находящихся в хранилище банка и время их пребывания на 
текущий момент.

## Установка и запуск

Клонируйте репозиторий:

    git clone git@github.com:Flash-kir/django-orm-watching-storage.git

Для установки компонентов выполните:

    pip install -r requirenments.txt

Перед запуском выполните команду:

    cp example.env .env

Настройте переменные окружения в файле .env:

SECRET_KEY='eyJtZXNzYWdlIjoiS' - создание ключа описано в [документации](https://docs.djangoproject.com/en/4.1/topics/signing/).
DB_ENGINE='' - рекомендации по [настройке](https://docs.djangoproject.com/en/4.1/ref/settings/#engine).
DB_HOST='' - рекомендации по [настройке](https://docs.djangoproject.com/en/4.1/ref/settings/#host).
DB_PORT='' - рекомендации по [настройке](https://docs.djangoproject.com/en/4.1/ref/settings/#port).
DB_NAME='' - рекомендации по [настройке](https://docs.djangoproject.com/en/4.1/ref/settings/#name).
DB_USER='' - рекомендации по [настройке](https://docs.djangoproject.com/en/4.1/ref/settings/#user).
DB_PASSWORD='' - рекомендации по [настройке](https://docs.djangoproject.com/en/4.1/ref/settings/#password).
DEBUG=True - рекомендации по [настройке](https://docs.djangoproject.com/en/4.1/ref/settings/#std-setting-DEBUG).
ALLOWED_HOSTS=['127.0.0.1','0.0.0.0'] - рекомендации по [настройке](https://docs.djangoproject.com/en/4.1/ref/settings/#std-setting-ALLOWED_HOSTS).

Для запуска вызовите:

    python manage.py
