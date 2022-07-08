# YaTube REST API 

API для социальной сети YaTube

## Возможности

- Просмотр, создание, изменение, удаление постов
- Просмотр, создание, изменение, удаление коментариев
- Подписка на посты пользователей

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:hikjik/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

## Примеры

После запуска проекта доступна [документация](http://127.0.0.1:8000/redoc) с примерами
