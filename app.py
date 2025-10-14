# Импортируем Flask — это инструмент для создания сайтов на Python
from flask import Flask

# Создаём "приложение" — как сервер, который будет показывать страницы
app = Flask(__name__)

# Главная страница: когда заходишь на сайт (/)
@app.route('/')
def home():
    # Возвращаем HTML-код — это то, что увидит браузер
    # HTML — язык для структуры страницы (заголовки, текст, картинки)
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Мой сайт на Python</title>
        <!-- CSS-стили: делают сайт красивым (цвета, шрифты) -->
        <style>
            body { 
                background-color: lightblue;  /* Фон страницы — светло-голубой */
                font-family: Arial;  /* Шрифт — простой Arial */
                margin: 20px;  /* Отступы от краёв */
            }
            h1 { 
                color: navy;  /* Заголовок — тёмно-синий */
                text-align: center;  /* По центру */
            }
            p { 
                font-size: 18px;  /* Текст побольше */
            }
            img { 
                display: block;  /* Картинка по центру */
                margin: 0 auto;  /* Авто-отступы */
            }
            a { 
                color: green;  /* Ссылки — зелёные */
                text-decoration: none;  /* Без подчёркивания */
            }
        </style>
    </head>
    <body>
        <h1>Привет! Это мой первый сайт на Python</h1>
        <p>Я школьник и учусь программировать. Flask — это просто и круто!</p>
        <!-- Картинка: замени src на свою ссылку (найди бесплатную картинку в Google) -->
        <img src="https://via.placeholder.com/300x200?text=Моя+Картинка" alt="Моя картинка" width="300">
        <p>Это картинка. Добавь свою!</p>
        <!-- Ссылка на другую страницу -->
        <p><a href="/about">Перейти на страницу "Обо мне"</a></p>
    </body>
    </html>
    '''

# Вторая страница: /about (когда кликаешь на ссылку)
@app.route('/about')
def about():
    # Ещё один HTML, но проще — только текст
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Обо мне</title>
        <style>
            body { background-color: lightgreen; color: darkgreen; }
            h1 { text-align: center; }
        </style>
    </head>
    <body>
        <h1>Обо мне</h1>
        <p>Меня зовут [твоё имя]. Я люблю Python, игры и друзей.</p>
        <p><a href="/">Вернуться на главную</a></p>
    </body>
    </html>
    '''

# Запуск сайта: debug=True показывает ошибки, если что-то не так
if __name__ == '__main__':
    app.run(debug=True)