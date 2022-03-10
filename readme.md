# Тестовое задание для компании "Комтек"

## Запуск проекта

Для запуска проекта требуется docker и docker-compose
1. Склонируйте проект и перейдите в каталог с ним  
```
git clone https://github.com/kiriharu/komtek_test
cd komtek_test
```
2. Запустите контейнер при помощи docker-compose:  
```
docker-compose up -d --build  
```
3. После завершения билда выполните миграции и создайте админ  
```
docker-compose run web python manage.py migrate
docker-compose run web python manage.py createsuperuser
```
4. Если необходимо - импортируйте заранее заготовленные фикстуры
```
docker-compose run web python manage.py loaddata ./dump.yaml
```
5. API доступно по адресу localhost:80

## Описание API

1. Получение списка справочников.  
Пример запроса: GET http://127.0.0.1:8000/api/directories/  
Результат:  
```json
{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 3,
            "name": "Справочник 1",
            "short_name": "СПР1",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent quis erat odio. Suspendisse potenti. Donec non fermentum felis. Vivamus suscipit lorem ac ex fermentum, et fermentum mi fringilla.",
            "versions": [
                {
                    "version": "v1",
                    "start_date": "2022-03-01"
                },
                {
                    "version": "v2",
                    "start_date": "2022-03-09"
                },
                {
                    "version": "v3",
                    "start_date": "2022-03-31"
                }
            ]
        },
        {
            "id": 4,
            "name": "Справочник 2",
            "short_name": "СПР2",
            "description": "Quisque nec eros euismod, molestie purus sed, auctor metus. Ut scelerisque non diam at consectetur. Proin sed erat eget mi viverra convallis.",
            "versions": [
                {
                    "version": "1.0.0",
                    "start_date": "2022-03-31"
                }
            ]
        },
        {
            "id": 5,
            "name": "Справочник 3",
            "short_name": "СПР3",
            "description": "Sed vel eros sed tellus malesuada pharetra ac luctus ligula. Donec felis turpis, rutrum et turpis eget, tempor fermentum libero. Suspendisse aliquam iaculis porttitor. In porttitor lectus ac suscipit pellentesque.",
            "versions": []
        }
    ]
}
```
2. Получение списка справочников, актуальных на указанную дату.  
Пример запроса: GET http://127.0.0.1:8000/api/directories/?start_date=2022-03-10  
Результат:  
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 3,
            "name": "Справочник 1",
            "short_name": "СПР1",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent quis erat odio. Suspendisse potenti. Donec non fermentum felis. Vivamus suscipit lorem ac ex fermentum, et fermentum mi fringilla.",
            "versions": [
                {
                    "version": "v1",
                    "start_date": "2022-03-01"
                },
                {
                    "version": "v2",
                    "start_date": "2022-03-09"
                },
                {
                    "version": "v3",
                    "start_date": "2022-03-31"
                }
            ]
        }
    ]
}
```
3. Получение всех элементов заданного справочника  
Пример запроса: GET http://127.0.0.1:8000/api/directories/3/items  
Результат:  
```json

{
    "count": 7,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 6,
            "parent": null,
            "code": "Имя",
            "value": "Нет имени",
            "version": "v1"
        },
        {
            "id": 7,
            "parent": null,
            "code": "Фамилия",
            "value": "Нет фамилии",
            "version": "v1"
        },
        {
            "id": 8,
            "parent": null,
            "code": "Паспортные данные",
            "value": "Здесь будут паспортные данные",
            "version": "v1"
        },
        {
            "id": 9,
            "parent": null,
            "code": "Имя",
            "value": "Джанго",
            "version": "v2"
        },
        {
            "id": 12,
            "parent": null,
            "code": "Фамилия",
            "value": "Освобожденный",
            "version": "v2"
        },
        {
            "id": 13,
            "parent": null,
            "code": "Паспортные данные",
            "value": "Предоставлены",
            "version": "v2"
        },
        {
            "id": 14,
            "parent": 13,
            "code": "Номер паспорта",
            "value": "12345",
            "version": "v2"
        }
    ]
}
```
4. Получение элементов заданного справочника текущей версии  
Пример запроса: GET http://127.0.0.1:8000/api/directories/3/items?actual=true   
Результат:  
```json
{
    "count": 4,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 9,
            "parent": null,
            "code": "Имя",
            "value": "Джанго",
            "version": "v2"
        },
        {
            "id": 12,
            "parent": null,
            "code": "Фамилия",
            "value": "Освобожденный",
            "version": "v2"
        },
        {
            "id": 13,
            "parent": null,
            "code": "Паспортные данные",
            "value": "Предоставлены",
            "version": "v2"
        },
        {
            "id": 14,
            "parent": 13,
            "code": "Номер паспорта",
            "value": "12345",
            "version": "v2"
        }
    ]
}
```
5. Валидация элементов заданного справочника текущей версии  
Пример запроса: POST http://127.0.0.1:8000/api/directories/3/items/validate?actual=true  
Payload:
```json
{
  "values": [
    {
      "parent": null,
      "code": "Имя",
      "value": "Джанго"
    },
    {
      "parent": 1,
      "code": "unknown",
      "value": "unknown"
    }
  ]
}
```
Результат:  
```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 9,
      "parent": null,
      "code": "Имя",
      "value": "Джанго",
      "version": "v2"
    }
  ]
}
```

6. Получение элементов заданного справочника указанной версии  
Пример запроса: GET http://127.0.0.1:8000/api/directories/3/items?version=v1  
Результат:  
```json
{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 6,
            "parent": null,
            "code": "Имя",
            "value": "Нет имени",
            "version": "v1"
        },
        {
            "id": 7,
            "parent": null,
            "code": "Фамилия",
            "value": "Нет фамилии",
            "version": "v1"
        },
        {
            "id": 8,
            "parent": null,
            "code": "Паспортные данные",
            "value": "Здесь будут паспортные данные",
            "version": "v1"
        }
    ]
}
```
7. Валидация элементов заданного справочника текущей версии  
Пример запроса: POST http://127.0.0.1:8000/api/directories/3/items/validate?version=v1  
Payload:
```json
{
  "values": [
    {
      "parent": null,
      "code": "Имя",
      "value": "Джанго"
    },
    {
      "parent": 1,
      "code": "unknown",
      "value": "unknown"
    },
    {
      "parent": null,
      "code": "Имя",
      "value": "Нет имени"
    }
  ]
}
```
Результат:  
```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 6,
      "parent": null,
      "code": "Имя",
      "value": "Нет имени",
      "version": "v1"
    }
  ]
}
```
## Техническое задание

Разработать сервис терминологии и REST API к нему.

### Описание

Сервис терминологии оперирует ниже перечисленными сущностями.



Сущность "Справочник" содержит следующие атрибуты:

- идентификатор справочника (глобальный и не зависит от версии)
- наименование
- короткое наименование
- описание
- версия (тип: строка,  не может быть пустойуникальная в пределах одного справочника)
- дата начала действия справочника этой версии



Сущность "Элемент справочника"

- идентификатор
- родительский идентификатор
- код элемента (тип: строка, не может быть пустой)
- значение элемента (тип: строка, не может быть пустой)



API должно предоставлять следующие методы:

- получение списка справочников.
- получение списка справочников, актуальных на указанную дату.
- получение элементов заданного справочника текущей версии
- валидация элементов заданного справочника текущей версии
- получение элементов заданного справочника указанной версии
- валидация элемента заданного справочника по указанной версии

В API должен быть предусмотрен постраничный вывод результата (данные должны возвращаться частями по 10 элементов).

К сервису должна иметься GUI административной части, с помощью которой можно добавлять новые справочники, новые версии справочников, указывать дату начала действия и наполнять справочники элементами.

Некоторые подробности намеренно не указаны. Оставляем их на ваше усмотрение.

### Технологии

* Python >= 3.8

### Критерии оценки

* Выполнение требований ТЗ.
* Читаемость программного кода (отступы, разделители и т.д.).
* Адекватность выбора подхода: технологий, конструкций языка.
* Наличие в коде программы комментариев и их содержание.
* Невозможность внесения некорректных данных пользователем.
* Наличие ошибок в программе (не ожиданное поведение, не корректные выходные данные), в том числе возникающих при непредусмотренных действиях пользователей.
* Удобство использования (логичность элементов API и GUI-интерфейса).
* Наличие описания разработанного API с примерами.

### Размещение

* Проект должен быть размещён на GitHub или аналогичном сервисе.
