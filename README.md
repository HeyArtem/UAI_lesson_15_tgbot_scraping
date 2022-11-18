# Telegram-bot. <br/>Home work for UAI, lesson 15.


![alt-текст](https://github.com/HeyArtem/dixy_scraping/blob/main/picture_dixy.png "Текст заголовка логотипа 1")



## Тех.детали: 
* _aiogram_
* _async_
* _fsm_
* _ReplyKeyboardMarkup_
* _InlineKeyboardMarkup_
* _dp.message handler_
* _dp.callback query handler_
* _requests_
* _BeautifulSoup_
* _bs4_
* _os_
* _json_ 
* _time_
* _random_
<br/><br/>
<hr>

## Описание:
Телеграм бот, имитирует бота для заказа еды. 
<br/>- Часть ветки по заказу еды, я реализовал на обычных кнопках, часть на Инлайн клавиатуре
<br/>- Написал Машину состояний (Finite-state machine). Мини FSM (Твое Имя, любимое авто, сторона света) и полноценная FSM с выводом итога всего заказа
<br/>- Подключил функцию, которая парсит данные с сайта Dixy и выводит результат в мессенджер (первая страница)
<br/>- Инлайн кнопки с сылками, кнопка заглушка
<br/><br/>
<hr>

## Особенности:
В проекте применял ответ с цитированием сообщения, вывод имени и id пользователя, написал хэндлеры (фильтры обработчики) для работы с callback_query (инлайн клавиатура), message_handler (обычные кнопки). Фильтры equals (фильтр идентичности) и ignore_case, text, bold, italic. Заливал списки в хэндлеры.
<br/><br/>
<hr>

## Что бы запустить проект:
- создать директорию на компьютере
- открыть нужный репозиторий-Code-HTTPS-скопировать ссылку
- $ git clone + ссылка
- перейти в паку с проектом
- $ python3 -m venv venv -создать виртуальное окружение
- $ source venv/bin/activate -активировать виртуальное окружение
- $ pip install -U pip setuptools
- $ pip install -r requirements.txt -установить библиотеки из requirements.txt
- $ code . -открыть проект в VS Code
- Получить токен своего бота (https://t.me/BotFather) (@BotFather)
- Вписать токен бота (.env). 
- запустить app.py 
- Возможно потребуются свежие headers (dixy.py)
<br/><br/>
<hr>

## Примечание:
- При выводе результатов парсинга, столкнулся с проблемой, нельзя упаковать весь результат скрапинга в одно сообщение в связи с ограничением максимального количества символов (до 4 096 символов).  В будущем нужно будет изменить вывод или выгружать в фаил.
> aiogram.utils.exceptions.MessageIsTooLong: Message is too long
<br/>

- В следующем проекте упаковать разные группы хэндлеров в отдельные директории.  Например: (📂 handlers/users/dir_for_eat), а остальные хэндлеры в другую  (📂 handlers/users/dir_another).

- Научится привязывать к блюду стоимость и написать автоматическую калькуляцию.
- Добавить вернутся назад в каждом разделе, совместить это с FSM (что бы покупатель мог сохранить блюда из разных разделов).
- Сделать изменение количества товра, +1 или -1.
- Сделать корзину, просмотр корзины (показано 3 из 9), оформить.
- Можно сделать раздел избранное.
- Добавить картинки
- Попробовать другие способы работы с FSM:
```python 
#option 1
await state.update_data(answer1=answer)

# option 2
await state.update(
{'answer1':answer}
)
# option 3  асинхронный генератор, удобно, если нужно доставать данные и изменять
async with state.proxy()as data:
        data['answer1'] = answer

например:
async with state.proxy()as data:
        data['some_list'].append(1)

# тоже самое, что и
data = await state.get_data()
some_list = data.get("some_list')
some_list.append(1)
await state.update_data(some_list=some_list)
```
