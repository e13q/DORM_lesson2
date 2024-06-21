# Пульт охраны банка

Это внутренний репозиторий для сотрудников банка "Сияние". Если вы попали в этот репозиторий случайно, то вы не сможете его запустить, т.к. у вас нет доступа к БД, но можете свободно использовать код вёрстки или посмотреть как реализованы запросы к БД.

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

Также, потребуется наличие файла .env.
В файле .env должны быть указаны:

* Движок бд ```DB_ENGINE``` string
* Адрес бд ```DB_HOST``` string
* Порт бд ```DB_PORT``` int
* Имя бд ```DB_NAME``` string
* Логин пользователя ```DB_USER``` string
* Пароль ```DB_PASSWORD``` string
* Секретный ключ для шифрования паролей ```SECRET_KEY``` string
* Список строк, представляющих имена хостов/доменов, которые может обслуживать этот Django-сайт ```ALLOWED_HOSTS``` list

Если потребуется отладочный режим:
```DEBUG=True```

Запуск скрипта:
```python manage.py runserver 0.0.0.0:8000```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
