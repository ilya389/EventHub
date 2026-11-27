# EventHub

Веб-приложение для просмотра мероприятий и регистрации на них. 
Проект выполнен в рамках учебной практики.

## Стек технологий
* Python 3.12+
* Django 6.1.3
* SQLite (база данных по умолчанию)
* HTML, CSS

## Как запустить проект локально

1. Склонируйте репозиторий:
   `git clone <ссылка_на_ваш_репозиторий>`
2. Перейдите в папку с проектом:
   `cd EventHub`
3. Создайте виртуальное окружение:
   `python -m venv venv`
4. Активируйте его в Windows(git bash), Windows(git bash) соответственно:
   `source venv/Scripts/activate`, `venv\Scripts\activate`
5. Установите зависимости:
   `pip install -r requirements.txt`
6. Примените миграции (создайте базу данных):
   `python manage.py migrate`
7. Создайте администратора:
   `python manage.py createsuperuser`
8. Запустите локальный сервер:
   `python manage.py runserver`
## Проект выполнен в рамках первой недели практики.
После этого сайт будет доступен по адресу: `http://127.0.0.1:8000/admin/` и `http://127.0.0.1:8000/events/`