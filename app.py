# Импортируем Flask — фреймворк (инструмент), который помогает создавать сайты на Python
from flask import Flask

# Создаём "приложение" (объект сайта)
app = Flask(__name__)  # name — нужно, чтобы Flask понял, где находится наш код


# Главная страница сайта

@app.route('/')
def home():
    # HTML-код, который увидит пользователь при заходе на сайт
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Добрые сердца — Благотворительный проект</title>

        <!-- Стили оформления сайта -->
        <style>
            body {
                background-color: #FFFFFF;     /* Фон — белый */
                font-family: Arial, sans-serif; /* Шрифт текста */
                color: #333333;                 /* Тёмно-серый текст */
                margin: 0;
                padding: 0;
            }

            header {
                background-color: #2E8B57;      /* Изумрудно-зелёная шапка */
                color: white;                   /* Белый текст в шапке */
                text-align: center;
                padding: 20px;
            }

            h1 {
                margin: 0;
                font-size: 32px;
            }

            main {
                padding: 20px;
                text-align: center;
            }

            .category {
                background-color: #F9D949;      /* Золотистый блок */
                border-radius: 10px;
                padding: 15px;
                margin: 10px auto;
                width: 300px;
                transition: 0.3s;
            }

            .category:hover {
                background-color: #2E8B57;      /* При наведении — зелёный */
                color: white;
                cursor: pointer;
            }

            a {
                color: inherit;
                text-decoration: none;
                font-weight: bold;
            }

            footer {
                background-color: #2E8B57;
                color: white;
                text-align: center;
                padding: 10px;
                margin-top: 30px;
            }
        </style>
    </head>

    <body>
        <!-- Верхняя часть сайта -->
        <header>
            <h1> Добрые сердца</h1>
            <p>Каталог благотворительных организаций</p>
        </header>

        <!-- Основной контент -->
        <main>
            <h2>Кому вы хотите помочь?</h2>

            <!-- Категории (переходы на разные страницы) -->
            <div class="category"><a href="/children">Детям</a></div>
            <div class="category"><a href="/elderly">Пожилым людям</a></div>
            <div class="category"><a href="/sick">Больным</a></div>
            <div class="category"><a href="/families">Семьям в трудной ситуации</a></div>
        </main>

        <!-- Нижняя часть сайта -->
        <footer>
            <p>© 2025 Добрые сердца. Все права защищены.</p>
        </footer>
    </body>
    </html>
    '''

# Страницы категорий

@app.route('/children')
def children():
    return '''
    <h1>Помощь детям</h1>
    <p>Здесь будут фонды, которые помогают детям.</p>
    <p><a href="/">← Вернуться на главную</a></p>
    '''

@app.route('/elderly')
def elderly():
    return '''
    <h1>Помощь пожилым людям</h1>
    <p>Здесь будут организации, помогающие пенсионерам и одиноким людям.</p>
    <p><a href="/">← Вернуться на главную</a></p>
    '''

@app.route('/sick')
def sick():
    return '''
    <h1>Помощь больным</h1>
    <p>Здесь можно разместить ссылки на фонды, поддерживающие людей с заболеваниями.</p>
    <p><a href="/">← Вернуться на главную</a></p>
    '''
@app.route('/families')
def families():
    return '''
    <h1>Помощь семьям</h1>
    <p>Здесь собраны организации, поддерживающие многодетные и малообеспеченные семьи.</p>
    <p><a href="/">← Вернуться на главную</a></p>
    '''


# Запуск сайта

if __name__ == '__main__':
    app.run(host = "0.0.0.0",port = 5000,debug=True)
