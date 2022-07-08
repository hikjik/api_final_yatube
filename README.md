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

## Документация

После запуска проекта документация доступна по [ссылке](http://127.0.0.1:8000/redoc)

## Примеры запросов к API

1. Создание JWT Токена

```
POST /api/v1/jwt/create/
```

Тело запроса:

```json
{
    "username": "leo",
    "password": "string"
}
```

Пример ответа:

```json
{
    "refresh": "string",
    "access": "string"
}
```

2. Получение списка публикаций

```
GET /api/v1/posts
```

Пример ответа:

```json
[
    {
        "id": 1,
        "text": "Test text",
        "author": "leo",
        "image": null,
        "group": 1,
        "pub_date": "2022-07-07T20:38:05.267907Z"
    },
    {
        "id": 2,
        "text": "Test text 2",
        "author": "leo",
        "image": "string",
        "group": 1,
        "pub_date": "2022-07-07T21:18:05.625499Z"
    }
]
```

3. Создание публикации. Анонимные запросы запрещены, требуется указать токен аутентификации в заголовке запроса

```
POST /api/v1/posts
```

Тело запроса:

```json
{
  "text": "Test text 3",
  "group": 1
}
```

Пример ответа:

```json
{
    "id": 3,
    "text": "Test text 3",
    "author": "leo",
    "image": null,
    "group": 1,
    "pub_date": "2022-07-08T14:40:32.909158Z"
}
```
