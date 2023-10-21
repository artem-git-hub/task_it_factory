# Проект API для мобильного приложения

Этот проект представляет собой API для мобильного приложения, где полевые сотрудники заказчика могут выполнять визиты в магазины. 


### Требования

- Python 3.10+
- Docker
- Docker Compose

### Для запуска
- **Зависимости** - установятся автоматически в докер контейнере
- **Миграции** - применятся автоматически в контейнере
- **Пример локальных настроек** - все запустится в контейнере с внутренними локальными настройками
- **Тестовые данные автоматически загрузятся в базу данных**

## Инструкция по развертыванию проекта

Для развертывания проекта выполните следующие шаги:

### 1. Клонирование репозитория
Клонируйте репозиторий в желаемую директорию:

```bash
git clone git@github.com:artem-git-hub/task_it_factory.git
cd task_it_factory
```
### 2. Запуск приложения
Запустите проект с помощью Docker Compose:

```bash
sudo docker-compose up --build
```
### 3. Взаимодействие с API
API будет доступно по адресу http://localhost:8000/. Вы можете отправлять запросы на этот адрес для взаимодействия с API.

**Примеры запросов:**  

- GET (для получения списка магазинов по номеру телефона) : по ссылке (можно через браузер) `http://localhost:8000/api/stores/88888888888/`  
88888888888 - номер телефона (этот уже есть в базе) 

- POST (для выполнения посещения) : через утилиту curl
```bash
curl -X POST -H "Content-Type: application/json" -d '{
  "phone_number": "88888888888",
  "store_pk": 2,
  "coordinates": {
    "latitude": 123.456,
    "longitude": 789.012
  }
}' http://localhost:8000/api/create-visit/
```

### 4. Доступ в админ панель
При запуске создан базовый супер пользователь с такими данными:

login: `admin`
password: `dbpassword`

Получить доступ можно по ссылке: `http://localhost:8000/admin/`
