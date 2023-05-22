# API_YAMDB
REST API проект для сервиса YaMDb — сбор отзывов о фильмах, книгах или музыке.

## Описание
Проект YaMDb собирает отзывы пользователей на произведения.
Произведения делятся на категории: «Книги», «Фильмы», «Музыка».
Список категорий  может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»).

### Стек:
[![Python](https://img.shields.io/badge/-Python-464641?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![HTML5](https://img.shields.io/badge/-HTML5-464646?style=flat-square&logo=html5)](https://en.wikipedia.org/wiki/HTML5)
[![CSS](https://img.shields.io/badge/-CSS-464646?style=flat-square&logo=css3)](https://en.wikipedia.org/wiki/CSS)
[![Docker](https://img.shields.io/badge/Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![Pytest](https://img.shields.io/badge/-Pytest-464646?style=flat-square&logo=pytest)](https://docs.pytest.org/en/6.2.x/)

### Как запустить проект:
Все описанное ниже относится к ОС Linux.

Проверяем наличие Docker:
Прежде чем приступать к работе, убедиться что Docker установлен, для этого ввести команду:
```bash
docker -v
```
Проверить, что установлена последняя версия [Compose](https://docs.docker.com/compose/install/).
Также можно воспользоваться официальной [инструкцией](https://docs.docker.com/engine/install/).


Клонируем репозиторий и переходим в него:
```bash
git clone https://github.com/dmay92/infra_sp2
cd infra_sp2
cd api_yamdb
```

Переходим в папку с файлом docker-compose.yaml:
```bash
cd infra
```


Создаём файл `.env`, согласно примеру `.env.template`.


Запускаем `docker-compose`
   ```bash
   docker-compose up -d
   ```


Выполняем миграции:
```bash
docker-compose exec web python manage.py makemigrations
```
```bash
docker-compose exec web python manage.py migrate
```

Создаем суперпользователя:
```bash
docker-compose exec web python manage.py createsuperuser
```

Собираем статику:
```bash
docker-compose exec web python manage.py collectstatic --no-input
```

Заполняем базу тестовыми данными данными:
```bash
cd api_yamdb && python manage.py loaddata ../infra/fixtures.json
```

Останавливаем контейнеры:
```bash
docker-compose down -v
```

### Документация API YaMDb
Документация доступна по эндпойнту: http://localhost/redoc/