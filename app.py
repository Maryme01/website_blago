# Импортируем Flask — фреймворк (инструмент), который помогает создавать сайты на Python
from flask import Flask

# Создаём "приложение" (объект сайта)
app = Flask(__name__)  # __name__ — нужно, чтобы Flask понял, где находится наш код


# -------------------------------
# 🔹 Главная страница сайта
# -------------------------------
@app.route('/')  # когда пользователь заходит на адрес /
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
            <h1>💚 Добрые сердца</h1>
            <p>Каталог благотворительных организаций</p>
        </header>

        <!-- Основной контент: категории -->
        <main>
            <div class="category"><a href="/people">Людям</a></div>
            <div class="category"><a href="/animals">Животным</a></div>
            <div class="category"><a href="/ecology">Экология</a></div>
            <div class="category"><a href="/education">Образование</a></div>
            <div class="category"><a href="/emergency">Чрезвычайные ситуации</a></div>
            <div class="category"><a href="/volunteers">Волонтёрство</a></div>
        </main>

        <!-- Нижняя часть сайта -->
        <footer>
            <p>© 2025 Добрые сердца. Все права защищены.</p>
        </footer>
    </body>
    </html>
    '''

# -------------------------------
# 🔹 Страница категорий "Людям" — подкатегории
# -------------------------------
@app.route('/people')
def people():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Помощь людям</title>
        <style>
            body { font-family: Arial, sans-serif; margin:0; padding:0; background:#F9F9F9; color:#333; }
            header { background:#2E8B57; color:white; padding:20px; text-align:center; }
            h1 { margin:0; }
            main { display:flex; flex-wrap:wrap; justify-content:center; gap:15px; padding:20px; }
            .category { background-color:#F9D949; border-radius:10px; padding:20px; width:200px; text-align:center; transition:0.3s; }
            .category:hover { background-color:#2E8B57; color:white; cursor:pointer; }
            .category a { color:inherit; text-decoration:none; font-weight:bold; display:block; }
            a.back { display:block; margin-top:20px; color:#2E8B57; text-decoration:none; font-weight:bold; text-align:center; }
            a.back:hover { text-decoration:underline; }
        </style>
    </head>
    <body>
        <header>
            <h1>Помощь людям</h1>
            <p>Выберите подкатегорию</p>
        </header>

        <!-- Основной блок с подкатегориями -->
        <main>
            <div class="category"><a href="/children">Детям</a></div>
            <div class="category"><a href="/elderly">Пожилым</a></div>
            <div class="category"><a href="/sick">Больным</a></div>
            <div class="category"><a href="/families">Семьям в трудной ситуации</a></div>
        </main>

        <!-- Ссылка на возврат на главную -->
        <a href="/" class="back">← Вернуться на главную</a>
    </body>
    </html>
    '''

# -------------------------------
# 🔹 Страницы подкатегорий
# -------------------------------
@app.route('/people')
def people_page():
    return '<h1>Помощь людям</h1><p>Выберите подкатегорию</p><p><a href="/">← Вернуться на главную</a></p>'

@app.route('/animals')
def animals_page():
    return '<h1>Помощь животным</h1><p>Здесь будут организации, помогающие животным.</p><p><a href="/">← Вернуться на главную</a></p>'

@app.route('/ecology')
def ecology_page():
    return '<h1>Экология</h1><p>Ссылки на экологические инициативы.</p><p><a href="/">← Вернуться на главную</a></p>'

@app.route('/education')
def education_page():
    return '<h1>Образование</h1><p>Образовательные проекты и стипендии.</p><p><a href="/">← Вернуться на главную</a></p>'

@app.route('/emergency')
def emergency_page():
    return '<h1>Чрезвычайные ситуации</h1><p>Сбор помощи при катастрофах.</p><p><a href="/">← Вернуться на главную</a></p>'

@app.route('/volunteers')
def volunteers_page():
    return '<h1>Волонтёрство</h1><p>Ссылки на волонтёрские организации.</p><p><a href="/">← Вернуться на главную</a></p>'

# -------------------------------
# 🔹 Запуск сайта
# -------------------------------
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
