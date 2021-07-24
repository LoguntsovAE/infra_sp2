# Финальный проект 18-го спринта

## Описание:
___
### Суть проекта: запуск docker-compose
## Технологии:
- Python
- Django
- DRF
- PostreSQL
- Nginx
- Docker

## Как запустить проект
___
1. Склонировать репозиторий
2. Собрать и запустить образ
```sh
docker-compose up -b --build
```
3. Подготовить миграции
```sh
docker-compose exec web python manage.py makemigration
```
4. Выполнить миграции
```sh
docker-compose exec web python manage.py migrate
```
5. Собрать статику
```sh
docker-compose exec web python manage.py collectstatic
```
6. Создать суперпользователя
```sh
docker-compose exec web python manage.py createsuperuser
```
7. Загрузить в базу тестовые данные
```sh
docker-compose exec web python manage.py loaddata fixtures.json
```