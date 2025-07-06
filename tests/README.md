# Тесты API

## Запуск тестов

### Из папки server:
```bash
pytest -v
```

### Запуск конкретного теста:
```bash
pytest tests/test_auth_login.py::test_user_login -v
```

### Запуск всех тестов с подробным выводом:
```bash
pytest -v -s
```

## Структура тестов

- `conftest.py` - фикстуры и хелперы для всех тестов
- `test_auth_login.py` - тесты авторизации
- `test_auth_register.py` - тесты регистрации
- `test_user_name.py` - тесты изменения имени пользователя
- `test_exist.py` - тесты проверки существования пользователя

## Фикстуры

- `base_url` - базовый URL сервера
- `auth_login_url` - URL для авторизации
- `auth_register_url` - URL для регистрации
- `user_name_url` - URL для изменения имени
- `exist_url` - URL для проверки существования

## Хелперы

- `generate_random_email()` - генерация случайного email
- `generate_random_password()` - генерация случайного пароля
- `generate_random_age()` - генерация случайного возраста
- `generate_random_name()` - генерация случайного имени