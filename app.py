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
        <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;500;700&display=swap" rel="stylesheet">
        <style>
            body {
                background-color: #344E41;     /* Тёмный шалфейный фон */
                font-family: 'Quicksand', Arial, sans-serif;
                color: #E0E0E0;
                margin: 0;
                padding: 0;
            }

            header {
                background-color: #3A5A40;
                color: #F5F5F5;
                text-align: center;
                padding: 20px 20px 10px 20px; /* уменьшаем нижний padding */
            }

            h1 {
                margin: 0 0 5px 0; /* уменьшаем отступ снизу заголовка */
                font-size: 48px;
            }

            main {
                padding: 10px 20px 10px 20px; /* уменьшаем верхний и нижний padding */
                text-align: center;
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                gap: 12px;
            }
            .category {
                background-color: #6C8E63;      /* фон карточки */
                border-radius: 10px;
                padding: 20px;
                margin: 10px auto;
                width: 300px;
                transition: 0.3s;
                border: 1px solid #2E4F4F;      /* контур */
                box-shadow: 0 4px 6px rgba(0,0,0,0.3); /* тень */
                font-size: 20px; /* увеличенный текст на карточках */
            }

            .category:hover {
                background-color: #547D4B;      /* при наведении — зелёный чуть темнее */
                color: #1C1C1C;                /* текст остаётся тёмным */
                cursor: pointer;
                box-shadow: 0 6px 10px rgba(0,0,0,0.5);
            }

            .category a {
                color: #1C1C1C; /* тёмный текст */
                text-decoration: none;
                font-weight: 600;
                display: block;
            }

            a { color: inherit; text-decoration: none; font-weight: bold; }

            footer {
                background-color: #3A5A40;
                color: #F5F5F5;
                text-align: center;
                padding: 8px 10px; /* уменьшаем padding футера */
                margin-top: 15px;  /* уменьшаем расстояние между последней карточкой и футером */
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
            <div class="category"><a href="/people">💚 Людям</a></div>
            <div class="category"><a href="/animals">🐾 Животным</a></div>
            <div class="category"><a href="/ecology">🌱 Экология</a></div>
            <div class="category"><a href="/education">🎓 Образование</a></div>
            <div class="category"><a href="/emergency">🚨 Чрезвычайные ситуации</a></div>
            <div class="category"><a href="/volunteers">🤝 Волонтёрство</a></div>
        </main>

        <!-- Нижняя часть сайта -->
        <footer>
            <p>© 2025 Добрые сердца. Все права защищены.</p>
        </footer>
    </body>
    </html>
    '''

# -------------------------------
# 🔹 Страница категорий "Людям"
# -------------------------------
@app.route('/people')
def people():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Помощь людям</title>
        <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;500;700&display=swap" rel="stylesheet">
        <style>
            body { font-family: 'Quicksand', Arial, sans-serif; margin:0; padding:0; background:#344E41; color:#E0E0E0; }
            header { background:#3A5A40; color:#F5F5F5; padding:20px; text-align:center; }
            h1 { margin:0; font-size:36px; } /* увеличенный заголовок категории */
            main { display:flex; flex-wrap:wrap; justify-content:center; gap:15px; padding:20px; }
            .category { background-color:#6C8E63; border-radius:10px; padding:18px; width:220px; text-align:center; transition:0.3s; border:1px solid #2E4F4F; box-shadow:0 4px 6px rgba(0,0,0,0.3); font-size:18px; }
            .category:hover { background-color:#547D4B; color:#1C1C1C; cursor:pointer; box-shadow:0 6px 10px rgba(0,0,0,0.5); }
            .category a { color:#1C1C1C; text-decoration:none; font-weight:600; display:block; }
            a.back { display:block; margin-top:20px; color:#F5F5F5; text-decoration:none; font-weight:bold; text-align:center; }
            a.back:hover { text-decoration:underline; }
        </style>
    </head>
    <body>
        <header>
            <h1>💚 Людям</h1>
            <p>Выберите подкатегорию</p>
        </header>
        <main>
            <div class="category"><a href="/people/children">Детям</a></div>
            <div class="category"><a href="/people/elderly">Пожилым людям</a></div>
            <div class="category"><a href="/people/sick_children">Больным детям</a></div>
            <div class="category"><a href="/people/sick_adults">Больным взрослым</a></div>
            <div class="category"><a href="/people/families">Семьям в трудной ситуации</a></div>
        </main>
        <a href="/" class="back">← Вернуться на главную</a>
    </body>
    </html>
    '''

# -------------------------------
# 🔹 Страница категорий "Животным"
# -------------------------------
@app.route('/animals')
def animals():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Помощь животным</title>
        <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;500;700&display=swap" rel="stylesheet">
        <style>
            body { font-family: 'Quicksand', Arial, sans-serif; margin:0; padding:0; background:#344E41; color:#E0E0E0; }
            header { background:#3A5A40; color:#F5F5F5; padding:20px; text-align:center; }
            h1 { margin:0; font-size:36px; }
            main { display:flex; flex-wrap:wrap; justify-content:center; gap:15px; padding:20px; }
            .category { background-color:#6C8E63; border-radius:10px; padding:18px; width:220px; text-align:center; transition:0.3s; border:1px solid #2E4F4F; box-shadow:0 4px 6px rgba(0,0,0,0.3); font-size:18px; }
            .category:hover { background-color:#547D4B; color:#1C1C1C; cursor:pointer; box-shadow:0 6px 10px rgba(0,0,0,0.5); }
            .category a { color:#1C1C1C; text-decoration:none; font-weight:600; display:block; }
            a.back { display:block; margin-top:20px; color:#F5F5F5; text-decoration:none; font-weight:bold; text-align:center; }
            a.back:hover { text-decoration:underline; }
        </style>
    </head>
    <body>
        <header>
            <h1>🐾 Животным</h1>
            <p>Выберите подкатегорию</p>
        </header>
        <main>
            <div class="category"><a href="/animals/homeless">Бездомным животным</a></div>
            <div class="category"><a href="/animals/wild">Диким животным</a></div>
            <div class="category"><a href="/animals/shelters">Приютам</a></div>
            <div class="category"><a href="/animals/rescue">Спасение животных</a></div>
        </main>
        <a href="/" class="back">← Вернуться на главную</a>
    </body>
    </html>
    '''

# -------------------------------
# 🔹 Страница категорий "Экология"
# -------------------------------
@app.route('/ecology')
def ecology():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Экология</title>
        <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;500;700&display=swap" rel="stylesheet">
        <style>
            body { font-family: 'Quicksand', Arial, sans-serif; margin:0; padding:0; background:#344E41; color:#E0E0E0; }
            header { background:#3A5A40; color:#F5F5F5; padding:20px; text-align:center; }
            h1 { margin:0; font-size:36px; }
            main { display:flex; flex-wrap:wrap; justify-content:center; gap:15px; padding:20px; }
            .category { background-color:#6C8E63; border-radius:10px; padding:18px; width:220px; text-align:center; transition:0.3s; border:1px solid #2E4F4F; box-shadow:0 4px 6px rgba(0,0,0,0.3); font-size:18px; }
            .category:hover { background-color:#547D4B; color:#1C1C1C; cursor:pointer; box-shadow:0 6px 10px rgba(0,0,0,0.5); }
            .category a { color:#1C1C1C; text-decoration:none; font-weight:600; display:block; }
            a.back { display:block; margin-top:20px; color:#F5F5F5; text-decoration:none; font-weight:bold; text-align:center; }
            a.back:hover { text-decoration:underline; }
        </style>
    </head>
    <body>
        <header>
            <h1>🌱 Экология</h1>
            <p>Выберите подкатегорию</p>
        </header>
        <main>
            <div class="category"><a href="/ecology/trees">Посадка деревьев</a></div>
            <div class="category"><a href="/ecology/cleanup">Уборка территорий</a></div>
            <div class="category"><a href="/ecology/recycling">Переработка отходов</a></div>
            <div class="category"><a href="/ecology/protection">Защита природы</a></div>
        </main>
        <a href="/" class="back">← Вернуться на главную</a>
    </body>
    </html>
    '''

# -------------------------------
# 🔹 Страница категорий "Образование"
# -------------------------------
@app.route('/education')
def education():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Образование</title>
        <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;500;700&display=swap" rel="stylesheet">
        <style>
            body { font-family: 'Quicksand', Arial, sans-serif; margin:0; padding:0; background:#344E41; color:#E0E0E0; }
            header { background:#3A5A40; color:#F5F5F5; padding:20px; text-align:center; }
            h1 { margin:0; font-size:36px; }
            main { display:flex; flex-wrap:wrap; justify-content:center; gap:15px; padding:20px; }
            .category { background-color:#6C8E63; border-radius:10px; padding:18px; width:220px; text-align:center; transition:0.3s; border:1px solid #2E4F4F; box-shadow:0 4px 6px rgba(0,0,0,0.3); font-size:18px; }
            .category:hover { background-color:#547D4B; color:#1C1C1C; cursor:pointer; box-shadow:0 6px 10px rgba(0,0,0,0.5); }
            .category a { color:#1C1C1C; text-decoration:none; font-weight:600; display:block; }
            a.back { display:block; margin-top:20px; color:#F5F5F5; text-decoration:none; font-weight:bold; text-align:center; }
            a.back:hover { text-decoration:underline; }
        </style>
    </head>
    <body>
        <header>
            <h1>🎓 Образование</h1>
            <p>Выберите подкатегорию</p>
        </header>
        <main>
            <div class="category"><a href="/education/scholarships">Стипендии</a></div>
            <div class="category"><a href="/education/courses">Курсы и лекции</a></div>
            <div class="category"><a href="/education/online">Онлайн-обучение</a></div>
            <div class="category"><a href="/education/schools">Поддержка школ</a></div>
            <div class="category"><a href="/education/students">Помощь студентам</a></div>
        </main>
        <a href="/" class="back">← Вернуться на главную</a>
    </body>
    </html>
    '''

# -------------------------------
# 🔹 Страница категорий "Чрезвычайные ситуации"
# -------------------------------
@app.route('/emergency')
def emergency():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Чрезвычайные ситуации</title>
        <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;500;700&display=swap" rel="stylesheet">
        <style>
            body { font-family: 'Quicksand', Arial, sans-serif; margin:0; padding:0; background:#344E41; color:#E0E0E0; }
            header { background:#3A5A40; color:#F5F5F5; padding:20px; text-align:center; }
            h1 { margin:0; font-size:36px; }
            main { display:flex; flex-wrap:wrap; justify-content:center; gap:15px; padding:20px; }
            .category { background-color:#6C8E63; border-radius:10px; padding:18px; width:220px; text-align:center; transition:0.3s; border:1px solid #2E4F4F; box-shadow:0 4px 6px rgba(0,0,0,0.3); font-size:18px; }
            .category:hover { background-color:#547D4B; color:#1C1C1C; cursor:pointer; box-shadow:0 6px 10px rgba(0,0,0,0.5); }
            .category a { color:#1C1C1C; text-decoration:none; font-weight:600; display:block; }
            a.back { display:block; margin-top:20px; color:#F5F5F5; text-decoration:none; font-weight:bold; text-align:center; }
            a.back:hover { text-decoration:underline; }
        </style>
    </head>
    <body>
        <header>
            <h1>🚨 Чрезвычайные ситуации</h1>
            <p>Выберите подкатегорию</p>
        </header>
        <main>
            <div class="category"><a href="/emergency/fires">Помощь при пожарах</a></div>
            <div class="category"><a href="/emergency/earthquakes">Помощь при землетрясениях</a></div>
            <div class="category"><a href="/emergency/refugees">Помощь беженцам</a></div>
            <div class="category"><a href="/emergency/medical">Медицинская помощь</a></div>
        </main>
        <a href="/" class="back">← Вернуться на главную</a>
    </body>
    </html>
    '''

# -------------------------------
# 🔹 Страница категорий "Волонтёрство"
# -------------------------------
@app.route('/volunteers')
def volunteers():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Волонтёрство</title>
        <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;500;700&display=swap" rel="stylesheet">
        <style>
            body { font-family: 'Quicksand', Arial, sans-serif; margin:0; padding:0; background:#344E41; color:#E0E0E0; }
            header { background:#3A5A40; color:#F5F5F5; padding:20px; text-align:center; }
            h1 { margin:0; font-size:36px; }
            main { display:flex; flex-wrap:wrap; justify-content:center; gap:15px; padding:20px; }
            .category { background-color:#6C8E63; border-radius:10px; padding:18px; width:220px; text-align:center; transition:0.3s; border:1px solid #2E4F4F; box-shadow:0 4px 6px rgba(0,0,0,0.3); font-size:18px; }
            .category:hover { background-color:#547D4B; color:#1C1C1C; cursor:pointer; box-shadow:0 6px 10px rgba(0,0,0,0.5); }
            .category a { color:#1C1C1C; text-decoration:none; font-weight:600; display:block; }
            a.back { display:block; margin-top:20px; color:#F5F5F5; text-decoration:none; font-weight:bold; text-align:center; }
            a.back:hover { text-decoration:underline; }
        </style>
    </head>
    <body>
        <header>
            <h1>🤝 Волонтёрство</h1>
            <p>Выберите подкатегорию</p>
        </header>
        <main>
            <div class="category"><a href="/volunteers/animal_care">Уход за животными</a></div>
            <div class="category"><a href="/volunteers/shelters">Помощь в приютах</a></div>
            <div class="category"><a href="/volunteers/events">Волонтёры на мероприятиях</a></div>
            <div class="category"><a href="/volunteers/social">Социальные инициативы</a></div>
        </main>
        <a href="/" class="back">← Вернуться на главную</a>
    </body>
    </html>
    '''

# -------------------------------
# 🔹 Запуск сайта
# -------------------------------
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)