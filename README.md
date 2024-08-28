<h1 align="center">Проект UI и API тестов <a href="demoqa.com">demoqa.com</a></h1>

<a href="respublica.ru"> <img src="resources/images/Toolsqa.jpg" width="" height="70"> </a>


<h3 align="center">Python | Pytest | Selene | Requests | Jenkins | Selenoid | Allure | Telegram</h3>
<h3 align="center">
<img height="50" src="resources/images/Python.png"/>      &nbsp;&nbsp;&nbsp;&nbsp;
<img height="50" src="resources/images/Pytest.svg"/>      &nbsp;&nbsp;&nbsp;&nbsp;
<img height="50" src="resources/images/Selene.png"/>      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img height="50" src="resources/images/requests.png"/>      &nbsp;&nbsp;&nbsp;&nbsp;
<img height="50" src="resources/images/jenkins.png"/>     &nbsp;&nbsp;&nbsp;&nbsp;
<img height="50" src="resources/images/Selenoid.svg"/>    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img height="50" src="resources/images/allure.png"/>      &nbsp;&nbsp;&nbsp;&nbsp;
<img height="50" src="resources/images/telegram.png"/>
</h3>

---
> <a target="_blank" href="http://176.123.163.26:8888/job/demoqa_ui_tests/">Ссылка на проект в Jenkins</a>

### Реализованы тесты:
#### UI
##### Elements
- [x] [Text Box] Простая регистрация 
- [x] [Check Box] Выбор корневой ноды
- [x] [Check Box] Выбор конечной ноды
- [x] [Check Box] Выбор снятие флага с корневой ноды
- [x] [Radio Button] Выбор 
- [x] [Radio Button] Переключение выбора
- [x] [Web Tables] Добавление записи
- [x] [Web Tables] Редактирование записи
- [x] [Web Tables] Поиск записи
- [x] [Web Tables] Удаление записи
##### Forms
- [x] Полная регистрация 

#### API
- [x] Успешная авторизация
- [x] Проваленная авторизация
- [x] Авторизация без данных входа
- [x] Авторизация без данных входа
- [x] Успешная генерация токена
- [x] Проваленная генерация токена





## Запуск тестов
### Локально

1. Клонировать репозиторий 
```bash
git clone https://github.com/vinterbris/demoqa-project.git
```
2. В терминале в директории проекта создать и активировать виртуальное окружение
```bash
python -m venv .venv 
source .venv/bin/activate 
```
3. Установить зависимости
```
pip install -r requirements.txt 
```
4. Запустить командой
```bash
pytest
```

#### Получение отчета allure
```bazaar
allure serve
```

### Удалённо
В .env включаем selenoid, указываем доступную на нём версию браузера и его url

```
SELENOID=True
BROWSER_VERSION=127.0
```

## Оповещения в мессенджер

> _Настроена отправка оповещений в телеграм канал. Возможна настройка для Email,Slack, Discord, Skype, Mattermost, Rocket.Chat_

<img src="resources/images/screenshot_telegram.png" width="450" height="">