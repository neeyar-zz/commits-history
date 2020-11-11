Описание:
Сервис, который хранит историю коммитов по публичному репозиторию.



Как это работает:
Данные сохраняются в базу данных и отображаются на отдельной странице.

На странице 127.0.0.1:9090/list (где 127.0.0.1 - IP по умолчанию, а 9090 - сервера) отображаются имеющиеся репозитории, каждая запись по нажатию выводит информацию о данном репозитории и историю коммитов в JSON формате.

Добавление нового репозитория в список происходит на отдельной странице, на которую можно перейти по кнопке "Add a new repository" при условии, что пользователь вошел в систему под Администратором (Логин - "admin", пароль - "avokado"), в противном случае отобразится ошибка 403. 

Авторизация пользователя происходит на 127.0.0.1:9090/admin



Инструкция по использованию:
Для запуска потребуются Python 3, а также библиотеки Django, requests, environ, django-environ.

Сервер запускается командой 'python manage.py runserver' с каталога 'commits'. 


