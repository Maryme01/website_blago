# Импортируем Flask — фреймворк (инструмент), который помогает создавать сайты на Python
from flask import Flask
import plotly.graph_objects as go
import plotly.offline as pyo

# Создаём "приложение" (объект сайта)
app = Flask(__name__)  # __name__ — нужно, чтобы Flask понял, где находится наш код

# -------------------------------
# 🔹 Главная страница сайта
# -------------------------------
@app.route('/')  # когда пользователь заходит на адрес /
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>💚 Добрые сердца — Благотворительный проект</title>
        <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            body {
                background-color: #344E41;  /* 🔹 Тёмный шалфейный фон */
                font-family: 'Quicksand', Arial, sans-serif;
                color: #E0E0E0;
                margin: 0;
                padding: 0;
            }
            header {
                background-color: #3A5A40;  /* 🔹 Шапка сайта */
                color: #F5F5F5;             /* Белый текст */
                text-align: center;
                padding: 20px 20px 10px 20px; /* уменьшаем нижний padding */
            }
            h1 { margin: 0 0 10px 0; font-size: 56px; }  /* 🔹 Название сайта увеличено */
            main {
                padding: 20px;
                display: grid;
                grid-template-columns: repeat(3, 1fr);  /* 🔹 Сетка 3х2 */
                gap: 20px;
                justify-items: center;
            }
            .category {
                background-color: #6C8E63;       /* 🔹 Фон карточки */
                border: 1px solid #2E4F4F;       /* 🔹 Контур карточки */
                border-radius: 15px;
                padding: 25px;
                width: 230px;
                text-align: center;
                transition: all 0.4s ease;        /* 🔹 Плавная анимация */
                font-size: 20px;                  /* 🔹 Шрифт текста на карточке */
                font-weight: 700;
                color: #1C1C1C;                   /* 🔹 Тёмный текст */
                box-shadow: 0 4px 6px rgba(0,0,0,0.3); /* 🔹 Тень */
            }
            .category:hover {
                background-color: #547D4B;        /* 🔹 При наведении */
                transform: scale(1.05);           /* 🔹 Лёгкое увеличение */
                color: #1C1C1C;                   /* 🔹 Текст остаётся тёмным */
                cursor: pointer;
            }
            .category a { color: inherit; text-decoration: none; display:block; }
            footer {
                background-color: #344E41;        /* 🔹 Футер */
                color: #E0E0E0;
                text-align: center;
                padding: 15px;
                margin-top: 20px;
            }
            nav {
                background-color: #2E3B2F;        /* 🔹 Меню навигации */
                display:flex;
                justify-content:center;
                gap:25px;
                padding:15px 0;
            }
            nav a {
                color: white;
                text-decoration: none;
                font-weight: 700;
                padding: 8px 15px;
                font-size: 20px;
                border-radius: 5px;
                transition: background 0.3s ease, transform 0.3s ease; /* 🔹 Плавность */
            }  
            nav a:hover { 
                background-color: #276748;        /* 🔹 При наведении */
                transform: scale(1.05);           /* 🔹 Лёгкое увеличение */
            }
        </style>
    </head>
    <body>
        <header>
            <h1>💚 Добрые сердца</h1>
            <p>Каталог благотворительных организаций</p>
        </header>
        <nav>
            <a href="/">Основная</a>
            <a href="/statistics">Статистика</a>
            <a href="/about">О нас</a>
        </nav>
        <main>
            <div class="category"><a href="/people">👫 Людям</a></div>
            <div class="category"><a href="/animals">🐾 Животным</a></div>
            <div class="category"><a href="/ecology">🌱 Экология</a></div>
            <div class="category"><a href="/education">🎓 Образование</a></div>
            <div class="category"><a href="/emergency">🚨 Чрезвычайные ситуации</a></div>
            <div class="category"><a href="/volunteers">🤝 Волонтёрство</a></div>
        </main>
        <footer>
            <p>© 2025 Добрые сердца. Все права защищены.</p>
        </footer>
    </body>
    </html>
    '''

# -------------------------------
# 🔹 Категория "Людям" с подкатегориями
# -------------------------------
@app.route('/people')
def people():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Помощь людям</title>
        <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            body { font-family:'Quicksand', Arial, sans-serif; margin:0; padding:0; background:#344E41; color:#E0E0E0; }
            header { background:#3A5A40; color:white; padding:20px; text-align:center; }
            h1 { margin:0; font-size:48px; }
            main { display:grid; grid-template-columns:repeat(3,1fr); gap:20px; padding:20px; justify-items:center; }
            .category { background-color:#6C8E63; border:1px solid #2E4F4F; border-radius:15px; padding:25px; width:230px; text-align:center; transition:all 0.4s ease; font-size:20px; font-weight:700; color:#1C1C1C; box-shadow:0 4px 6px rgba(0,0,0,0.3);}
            .category:hover { background-color:#547D4B; transform:scale(1.05); color:#1C1C1C; cursor:pointer; }
            .category a { color:inherit; text-decoration:none; display:block; }
            a.back { display:block; margin-top:20px; color:#E0E0E0; text-decoration:none; font-weight:bold; text-align:center; }
            a.back:hover { text-decoration:underline; }
        </style>
    </head>
    <body>
        <header>
            <h1>Помощь людям</h1>
            <p>Выберите подкатегорию</p>
        </header>
        <main>
            <div class="category"><a href="/children">Детям</a></div>
            <div class="category"><a href="/elderly">Пожилым людям</a></div>
            <div class="category"><a href="/sick_children">Больным детям</a></div>
            <div class="category"><a href="/sick_adults">Больным взрослым</a></div>
            <div class="category"><a href="/families">Семьям в трудной ситуации</a></div>
        </main>
        <style>
        .back {
            display: block;           /* Чтобы заняло всю ширину */
            text-align: center;       /* Центрируем текст */
            margin: 20px auto;        /* Отступ сверху/снизу */
            color: white;             /* Белый цвет */
            font-weight: bold;        /* Жирный текст */
            font-size: 20px;          /* Размер текста */
            text-decoration: none;    /* Без подчеркивания */
            transition: color 0.3s ease;
        }
        .back:hover {
            color: #A8E6A2;           /* Светло-зелёный при наведении */
        }
        </style>
        <a href="/" class="back">← Вернуться на основную</a>
    </body>
    </html>
    '''

# 🔹 Подкатегории Людям
@app.route('/children')
def children_donations():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Помощь детям</title>
        <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            body { font-family:'Quicksand', Arial, sans-serif; margin:0; padding:0; background:#344E41; color:#E0E0E0; }
            header { background:#3A5A40; color:white; padding:20px; text-align:center; }
            h1 { margin:0; font-size:48px; }
            main { display:flex; flex-wrap:wrap; gap:20px; justify-content:center; padding:20px; }
            .donation-card {
                background-color:#6C8E63;
                border:1px solid #2E4F4F;
                border-radius:15px;
                width:300px;
                display:flex;
                flex-direction:column;
                overflow:hidden;
                box-shadow:0 4px 6px rgba(0,0,0,0.3);
                transition: transform 0.3s ease;
            }
            .donation-card:hover { transform: scale(1.03); }
            .donation-card img { width:100%; height:200px; object-fit:cover; }
            .donation-card h2 { margin:10px; font-size:24px; text-align:center; }
            .donation-card p { margin:0 10px 10px 10px; font-size:16px; line-height:1.4; }
            .donation-card a.donate {
                display:block;
                margin:10px;
                padding:10px;
                background-color:#7FB77E; /* чуть светлее */
                color:#1C1C1C;
                text-align:center;
                font-weight:bold;
                border-radius:8px;
                text-decoration:none;
                transition: background 0.3s ease;
            }
            .donation-card a.donate:hover { background-color:#95C18F; }
            .back-text {
                text-align:center;
                margin:20px;
                color:white;
                font-weight:bold;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Помощь детям</h1>
        </header>
        <main>
            <div class="donation-card">
                <img src="/static/images/child2.jpg" alt="Иван, 7 лет">
                <h2>Иван, 7 лет</h2>
                <p>Иван живет в детском доме и мечтает о школе с современными учебными материалами. Любая помощь важна!</p>
                <a href="#" class="donate">Помочь</a>
                
            </div>
            <div class="donation-card">
                <img src="/static/images/child1.jpg" alt="Маша, 5 лет">
                <h2>Маша, 5 лет</h2>
                <p>Маша нуждается в медицинской поддержке и игрушках для развития. Ваш вклад сделает её жизнь ярче.</p>
                <a href="#" class="donate">Помочь</a>
            </div>
        </main>
        <a href="/people" class="back">← Вернуться назад</a>

        <style>
        .back {
            display: block;           /* Чтобы заняло всю ширину */
            text-align: center;       /* Центрируем текст */
            margin: 20px auto;        /* Отступ сверху/снизу */
            color: white;             /* Белый цвет */
            font-weight: bold;        /* Жирный текст */
            font-size: 20px;          /* Размер текста */
            text-decoration: none;    /* Без подчеркивания */
            transition: color 0.3s ease;
        }
        .back:hover {
            color: #A8E6A2;           /* Светло-зелёный при наведении */
        }
        </style>
        </div>
    </body>
    </html>
    '''

@app.route('/elderly')
def elderly():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Пожилым людям</title>
        <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            body { font-family:'Quicksand', Arial, sans-serif; margin:0; padding:0; background:#344E41; color:#E0E0E0; }
            header { background:#3A5A40; color:white; padding:20px; text-align:center; }
            h1 { margin:0; font-size:48px; }
            main { display:flex; flex-wrap:wrap; gap:20px; justify-content:center; padding:20px; }
            .donation-card { background-color:#6C8E63; border:1px solid #2E4F4F; border-radius:15px; width:300px; display:flex; flex-direction:column; overflow:hidden; box-shadow:0 4px 6px rgba(0,0,0,0.3); transition: transform 0.3s ease; }
            .donation-card:hover { transform: scale(1.03); }
            .donation-card img { width:100%; height:200px; object-fit:cover; }
            .donation-card h2 { margin:10px; font-size:24px; text-align:center; }
            .donation-card p { margin:0 10px 10px 10px; font-size:16px; line-height:1.4; }
            .donation-card a.donate { display:block; margin:10px; padding:10px; background-color:#7FB77E; color:#1C1C1C; text-align:center; font-weight:bold; border-radius:8px; text-decoration:none; transition: background 0.3s ease; }
            .donation-card a.donate:hover { background-color:#95C18F; }
            .back { display:block; text-align:center; margin:20px auto; color:white; font-weight:bold; font-size:20px; text-decoration:none; transition: color 0.3s ease;}
            .back:hover { color:#A8E6A2; }
        </style>
    </head>
    <body>
        <header><h1>Пожилым людям</h1></header>
        <main>
            <div class="donation-card">
                <img src="/static/images/elderly2.jpeg" alt="Вера, 72 года">
                <h2>Вера, 72 года</h2>
                <p>Вера живёт одна и нуждается в регулярной поддержке для покупки лекарств и продуктов.</p>
                <a href="#" class="donate">Помочь</a>
            </div>
            <div class="donation-card">
                <img src="/static/images/elderly1.jpeg" alt="Пётр, 78 лет">
                <h2>Пётр, 78 лет</h2>
                <p>Пётр ветеран, нуждается в бытовой помощи и медицинских расходниках.</p>
                <a href="#" class="donate">Помочь</a>
            </div>
        </main>
        <a href="/people" class="back">← Вернуться назад</a>
    </body>
    </html>
    '''

@app.route('/sick_children')
def sick_children():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Больным детям</title>
        <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            body { font-family:'Quicksand', Arial, sans-serif; margin:0; padding:0; background:#344E41; color:#E0E0E0; }
            header { background:#3A5A40; color:white; padding:20px; text-align:center; }
            h1 { margin:0; font-size:48px; }
            main { display:flex; flex-wrap:wrap; gap:20px; justify-content:center; padding:20px; }
            .donation-card { background-color:#6C8E63; border:1px solid #2E4F4F; border-radius:15px; width:300px; display:flex; flex-direction:column; overflow:hidden; box-shadow:0 4px 6px rgba(0,0,0,0.3); transition: transform 0.3s ease; }
            .donation-card:hover { transform: scale(1.03); }
            .donation-card img { width:100%; height:200px; object-fit:cover; }
            .donation-card h2 { margin:10px; font-size:24px; text-align:center; }
            .donation-card p { margin:0 10px 10px 10px; font-size:16px; line-height:1.4; }
            .donation-card a.donate { display:block; margin:10px; padding:10px; background-color:#7FB77E; color:#1C1C1C; text-align:center; font-weight:bold; border-radius:8px; text-decoration:none; transition: background 0.3s ease; }
            .donation-card a.donate:hover { background-color:#95C18F; }
            .back { display:block; text-align:center; margin:20px auto; color:white; font-weight:bold; font-size:20px; text-decoration:none; transition: color 0.3s ease;}
            .back:hover { color:#A8E6A2; }
        </style>
    </head>
    <body>
        <header><h1>Больным детям</h1></header>
        <main>
            <div class="donation-card">
                <img src="/static/images/sick_child1.jpeg" alt="Ярослава, 9 лет">
                <h2>Маша, 8 лет</h2>
                <p>Маша борется с лейкемией, нужны лекарства и поддержка для лечения.</p>
                <a href="#" class="donate">Помочь</a>
            </div>
            <div class="donation-card">
                <img src="/static/images/sick_child2.jpeg" alt="Денис, 7 лет">
                <h2>Денис, 5 лет</h2>
                <p>Денис страдает от редкого заболевания и нуждается в реабилитации и терапии.</p>
                <a href="#" class="donate">Помочь</a>
            </div>
        </main>
        <a href="/people" class="back">← Вернуться назад</a>
    </body>
    </html>
    '''

@app.route('/sick_adults')
def sick_adults():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Больным взрослым</title>
        <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            body { font-family:'Quicksand', Arial, sans-serif; margin:0; padding:0; background:#344E41; color:#E0E0E0; }
            header { background:#3A5A40; color:white; padding:20px; text-align:center; }
            h1 { margin:0; font-size:48px; }
            main { display:flex; flex-wrap:wrap; gap:20px; justify-content:center; padding:20px; }
            .donation-card { background-color:#6C8E63; border:1px solid #2E4F4F; border-radius:15px; width:300px; display:flex; flex-direction:column; overflow:hidden; box-shadow:0 4px 6px rgba(0,0,0,0.3); transition: transform 0.3s ease; }
            .donation-card:hover { transform: scale(1.03); }
            .donation-card img { width:100%; height:200px; object-fit:cover; }
            .donation-card h2 { margin:10px; font-size:24px; text-align:center; }
            .donation-card p { margin:0 10px 10px 10px; font-size:16px; line-height:1.4; }
            .donation-card a.donate { display:block; margin:10px; padding:10px; background-color:#7FB77E; color:#1C1C1C; text-align:center; font-weight:bold; border-radius:8px; text-decoration:none; transition: background 0.3s ease; }
            .donation-card a.donate:hover { background-color:#95C18F; }
            .back { display:block; text-align:center; margin:20px auto; color:white; font-weight:bold; font-size:20px; text-decoration:none; transition: color 0.3s ease;}
            .back:hover { color:#A8E6A2; }
        </style>
    </head>
    <body>
        <header><h1>Больным взрослым</h1></header>
        <main>
            <div class="donation-card">
                <img src="/static/images/sick_adults1.jfif" alt="Алексей, 45 лет">
                <h2>Алексей, 45 лет</h2>
                <p>Алексей после операции нуждается в реабилитации и медицинских расходных материалах.</p>
                <a href="#" class="donate">Помочь</a>
            </div>
            <div class="donation-card">
                <img src="/static/images/sick_adults2.jfif" alt="Марина, 38 лет">
                <h2>Марина, 38 лет</h2>
                <p>Марина борется с хроническим заболеванием. Любая поддержка важна для её лечения.</p>
                <a href="#" class="donate">Помочь</a>
            </div>
        </main>
        <a href="/people" class="back">← Вернуться назад</a>
    </body>
    </html>
    '''

@app.route('/families')
def families():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Семьям в трудной ситуации</title>
        <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            body { font-family:'Quicksand', Arial, sans-serif; margin:0; padding:0; background:#344E41; color:#E0E0E0; }
            header { background:#3A5A40; color:white; padding:20px; text-align:center; }
            h1 { margin:0; font-size:48px; }
            main { display:flex; flex-wrap:wrap; gap:20px; justify-content:center; padding:20px; }
            .donation-card { background-color:#6C8E63; border:1px solid #2E4F4F; border-radius:15px; width:300px; display:flex; flex-direction:column; overflow:hidden; box-shadow:0 4px 6px rgba(0,0,0,0.3); transition: transform 0.3s ease; }
            .donation-card:hover { transform: scale(1.03); }
            .donation-card img { width:100%; height:200px; object-fit:cover; }
            .donation-card h2 { margin:10px; font-size:24px; text-align:center; }
            .donation-card p { margin:0 10px 10px 10px; font-size:16px; line-height:1.4; }
            .donation-card a.donate { display:block; margin:10px; padding:10px; background-color:#7FB77E; color:#1C1C1C; text-align:center; font-weight:bold; border-radius:8px; text-decoration:none; transition: background 0.3s ease; }
            .donation-card a.donate:hover { background-color:#95C18F; }
            .back { display:block; text-align:center; margin:20px auto; color:white; font-weight:bold; font-size:20px; text-decoration:none; transition: color 0.3s ease;}
            .back:hover { color:#A8E6A2; }
        </style>
    </head>
    <body>
        <header><h1>Семьям в трудной ситуации</h1></header>
        <main>
            <div class="donation-card">
                <img src="/static/images/family1.jfif" alt="Семья Ивановых">
                <h2>Семья Ивановых</h2>
                <p>Многодетная семья нуждается в помощи с продуктами и одеждой для детей.</p>
                <a href="#" class="donate">Помочь</a>
            </div>
            <div class="donation-card">
                <img src="/static/images/family2.jfif" alt="Семья Петровых">
                <h2>Семья Петровых</h2>
                <p>Семья пострадала от пожара и нуждается в восстановлении жилья и поддержке.</p>
                <a href="#" class="donate">Помочь</a>
            </div>
        </main>
        <a href="/people" class="back">← Вернуться назад</a>
    </body>
    </html>
    '''

# -------------------------------
# 🔹 Категория "Животным" с подкатегориями
# -------------------------------
@app.route('/animals')
def animals():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Животным</title>
        <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            body { font-family:'Quicksand', Arial, sans-serif; margin:0; padding:0; background:#344E41; color:#E0E0E0; }
            header { background:#3A5A40; color:white; padding:20px; text-align:center; }
            h1 { margin:0; font-size:48px; }
            main { display:grid; grid-template-columns:repeat(3,1fr); gap:20px; padding:20px; justify-items:center; }
            .category { background-color:#6C8E63; border:1px solid #2E4F4F; border-radius:15px; padding:25px; width:230px; text-align:center; transition:all 0.4s ease; font-size:20px; font-weight:700; color:#1C1C1C; box-shadow:0 4px 6px rgba(0,0,0,0.3);}
            .category:hover { background-color:#547D4B; transform:scale(1.05); color:#1C1C1C; cursor:pointer; }
            .category a { color:inherit; text-decoration:none; display:block; }
            a.back { display:block; margin-top:20px; color:#E0E0E0; text-decoration:none; font-weight:bold; text-align:center; }
            a.back:hover { text-decoration:underline; }
        </style>
    </head>
    <body>
        <header>
            <h1>Животным</h1>
            <p>Выберите подкатегорию</p>
        </header>
        <main>
            <div class="category"><a href="/homeless_animals">Бездомные</a></div>
            <div class="category"><a href="/wild_animals">Дикие</a></div>
            <div class="category"><a href="/shelters">Приюты</a></div>
            <div class="category"><a href="/animal_rescue">Спасение</a></div>
            <div class="category"><a href="/animal_conservation">Сохранение видов</a></div>
        </main>
        <style>
        .back {
            display: block;           /* Чтобы заняло всю ширину */
            text-align: center;       /* Центрируем текст */
            margin: 20px auto;        /* Отступ сверху/снизу */
            color: white;             /* Белый цвет */
            font-weight: bold;        /* Жирный текст */
            font-size: 20px;          /* Размер текста */
            text-decoration: none;    /* Без подчеркивания */
            transition: color 0.3s ease;
        }
        .back:hover {
            color: #A8E6A2;           /* Светло-зелёный при наведении */
        }
        </style>
        <a href="/" class="back">← Вернуться на основную</a>
    </body>
    </html>
    '''

# -------------------------------
# 🔹 Подкатегория "Бездомные животные"
# -------------------------------
@app.route('/homeless_animals')
def homeless_animals():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Бездомные животные</title>
        <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            body { font-family:'Quicksand', Arial, sans-serif; margin:0; padding:0; background:#344E41; color:#E0E0E0; }
            header { background:#3A5A40; color:white; padding:20px; text-align:center; }
            h1 { margin:0; font-size:48px; }
            main { display:flex; flex-wrap:wrap; gap:20px; justify-content:center; padding:20px; }
            .donation-card { background-color:#6C8E63; border:1px solid #2E4F4F; border-radius:15px; width:300px; display:flex; flex-direction:column; overflow:hidden; box-shadow:0 4px 6px rgba(0,0,0,0.3); transition: transform 0.3s ease; }
            .donation-card:hover { transform: scale(1.03); }
            .donation-card img { width:100%; height:200px; object-fit:cover; }
            .donation-card h2 { margin:10px; font-size:24px; text-align:center; }
            .donation-card p { margin:0 10px 10px 10px; font-size:16px; line-height:1.4; }
            .donation-card a.donate { display:block; margin:10px; padding:10px; background-color:#7FB77E; color:#1C1C1C; text-align:center; font-weight:bold; border-radius:8px; text-decoration:none; transition: background 0.3s ease; }
            .donation-card a.donate:hover { background-color:#95C18F; }
            .back { display:block; text-align:center; margin:20px auto; color:white; font-weight:bold; font-size:20px; text-decoration:none; transition: color 0.3s ease; }
            .back:hover { color:#A8E6A2; }
        </style>
    </head>
    <body>
        <header><h1>Бездомные животные</h1></header>
        <main>
            <div class="donation-card">
                <img src="/static/images/homeless1.jpg" alt="Пёсик Бим">
                <h2>Пёсик Бим</h2>
                <p>Бим живёт на улице и ищет добрые руки. Любая помощь поможет ему найти дом!</p>
                <a href="#" class="donate">Помочь</a>
            </div>
            <div class="donation-card">
                <img src="/static/images/homeless2.jpg" alt="Кошка Мурка">
                <h2>Кошка Мурка</h2>
                <p>Мурка потерялась и нуждается в питании и уходе. Поддержите её!</p>
                <a href="#" class="donate">Помочь</a>
            </div>
        </main>
        <a href="/animals" class="back">← Вернуться назад</a>
    </body>
    </html>
    '''

# -------------------------------
# 🔹 Подкатегория "Дикие животные"
# -------------------------------
@app.route('/wild_animals')
def wild_animals():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Дикие животные</title>
        <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            body { font-family:'Quicksand', Arial, sans-serif; margin:0; padding:0; background:#344E41; color:#E0E0E0; }
            header { background:#3A5A40; color:white; padding:20px; text-align:center; }
            h1 { margin:0; font-size:48px; }
            main { display:flex; flex-wrap:wrap; gap:20px; justify-content:center; padding:20px; }
            .donation-card { background-color:#6C8E63; border:1px solid #2E4F4F; border-radius:15px; width:300px; display:flex; flex-direction:column; overflow:hidden; box-shadow:0 4px 6px rgba(0,0,0,0.3); transition: transform 0.3s ease; }
            .donation-card:hover { transform: scale(1.03); }
            .donation-card img { width:100%; height:200px; object-fit:cover; }
            .donation-card h2 { margin:10px; font-size:24px; text-align:center; }
            .donation-card p { margin:0 10px 10px 10px; font-size:16px; line-height:1.4; }
            .donation-card a.donate { display:block; margin:10px; padding:10px; background-color:#7FB77E; color:#1C1C1C; text-align:center; font-weight:bold; border-radius:8px; text-decoration:none; transition: background 0.3s ease; }
            .donation-card a.donate:hover { background-color:#95C18F; }
            .back { display:block; text-align:center; margin:20px auto; color:white; font-weight:bold; font-size:20px; text-decoration:none; transition: color 0.3s ease; }
            .back:hover { color:#A8E6A2; }
        </style>
    </head>
    <body>
        <header><h1>Дикие животные</h1></header>
        <main>
            <div class="donation-card">
                <img src="/static/images/wild1.jpg" alt="Олень">
                <h2>Олень</h2>
                <p>Молодой олень пострадал в лесном пожаре и нуждается в заботе и восстановлении.</p>
                <a href="#" class="donate">Помочь</a>
            </div>
            <div class="donation-card">
                <img src="/static/images/wild2.jfif" alt="Лиса Фаина">
                <h2>Лиса Фаина</h2>
                <p>Лиса ранена после ДТП и требует лечения и реабилитации.</p>
                <a href="#" class="donate">Помочь</a>
            </div>
        </main>
        <a href="/animals" class="back">← Вернуться назад</a>
    </body>
    </html>
    '''

# -------------------------------
# 🔹 Подкатегория "Приюты"
# -------------------------------
@app.route('/shelters')
def shelters():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Приюты</title>
        <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            body { font-family:'Quicksand', Arial, sans-serif; margin:0; padding:0; background:#344E41; color:#E0E0E0; }
            header { background:#3A5A40; color:white; padding:20px; text-align:center; }
            h1 { margin:0; font-size:48px; }
            main { display:flex; flex-wrap:wrap; gap:20px; justify-content:center; padding:20px; }
            .donation-card { background-color:#6C8E63; border:1px solid #2E4F4F; border-radius:15px; width:300px; display:flex; flex-direction:column; overflow:hidden; box-shadow:0 4px 6px rgba(0,0,0,0.3); transition: transform 0.3s ease; }
            .donation-card:hover { transform: scale(1.03); }
            .donation-card img { width:100%; height:200px; object-fit:cover; }
            .donation-card h2 { margin:10px; font-size:24px; text-align:center; }
            .donation-card p { margin:0 10px 10px 10px; font-size:16px; line-height:1.4; }
            .donation-card a.donate { display:block; margin:10px; padding:10px; background-color:#7FB77E; color:#1C1C1C; text-align:center; font-weight:bold; border-radius:8px; text-decoration:none; transition: background 0.3s ease; }
            .donation-card a.donate:hover { background-color:#95C18F; }
            .back { display:block; text-align:center; margin:20px auto; color:white; font-weight:bold; font-size:20px; text-decoration:none; transition: color 0.3s ease; }
            .back:hover { color:#A8E6A2; }
        </style>
    </head>
    <body>
        <header><h1>Приюты</h1></header>
        <main>
            <div class="donation-card">
                <img src="/static/images/shelters1.jpg" alt="Приют Дружок">
                <h2>Приют Дружок</h2>
                <p>Приют нуждается в кормах и медикаментах для животных. Любая помощь важна!</p>
                <a href="#" class="donate">Помочь</a>
            </div>
            <div class="donation-card">
                <img src="/static/images/shelter2.jfif" alt="Приют Лапка">
                <h2>Приют Лапка</h2>
                <p>Поддержите приют для бездомных животных: корма, игрушки, лечение.</p>
                <a href="#" class="donate">Помочь</a>
            </div>
        </main>
        <a href="/animals" class="back">← Вернуться назад</a>
    </body>
    </html>
    '''

# -------------------------------
# 🔹 Подкатегория "Спасение животных"
# -------------------------------
@app.route('/animal_rescue')
def animal_rescue():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Спасение животных</title>
        <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            body { font-family:'Quicksand', Arial, sans-serif; margin:0; padding:0; background:#344E41; color:#E0E0E0; }
            header { background:#3A5A40; color:white; padding:20px; text-align:center; }
            h1 { margin:0; font-size:48px; }
            main { display:flex; flex-wrap:wrap; gap:20px; justify-content:center; padding:20px; }
            .donation-card { background-color:#6C8E63; border:1px solid #2E4F4F; border-radius:15px; width:300px; display:flex; flex-direction:column; overflow:hidden; box-shadow:0 4px 6px rgba(0,0,0,0.3); transition: transform 0.3s ease; }
            .donation-card:hover { transform: scale(1.03); }
            .donation-card img { width:100%; height:200px; object-fit:cover; }
            .donation-card h2 { margin:10px; font-size:24px; text-align:center; }
            .donation-card p { margin:0 10px 10px 10px; font-size:16px; line-height:1.4; }
            .donation-card a.donate { display:block; margin:10px; padding:10px; background-color:#7FB77E; color:#1C1C1C; text-align:center; font-weight:bold; border-radius:8px; text-decoration:none; transition: background 0.3s ease; }
            .donation-card a.donate:hover { background-color:#95C18F; }
            .back { display:block; text-align:center; margin:20px auto; color:white; font-weight:bold; font-size:20px; text-decoration:none; transition: color 0.3s ease; }
            .back:hover { color:#A8E6A2; }
        </style>
    </head>
    <body>
        <header><h1>Спасение животных</h1></header>
        <main>
            <div class="donation-card">
                <img src="/static/images/rescue1.jpg" alt="Спасённая сова">
                <h2>Сова</h2>
                <p>Сова была спасена после травмы. Нужна помощь в лечении и восстановлении.</p>
                <a href="#" class="donate">Помочь</a>
            </div>
            <div class="donation-card">
                <img src="/static/images/rescue2.jpg" alt="Щенок после спасения">
                <h2>Щенок</h2>
                <p>Щенок найден на улице после дождя. Поддержите его лечение и заботу.</p>
                <a href="#" class="donate">Помочь</a>
            </div>
        </main>
        <a href="/animals" class="back">← Вернуться назад</a>
    </body>
    </html>
    '''
# -------------------------------
# 🔹 Подкатегория "Сохранение животных"
# -------------------------------
@app.route('/animal_conservation')
def animal_conservation():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Сохранение животных</title>
        <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            body { font-family:'Quicksand', Arial, sans-serif; margin:0; padding:0; background:#344E41; color:#E0E0E0; }
            header { background:#3A5A40; color:white; padding:20px; text-align:center; }
            h1 { margin:0; font-size:48px; }
            main { display:flex; flex-wrap:wrap; gap:20px; justify-content:center; padding:20px; }
            .donation-card { background-color:#6C8E63; border:1px solid #2E4F4F; border-radius:15px; width:300px; display:flex; flex-direction:column; overflow:hidden; box-shadow:0 4px 6px rgba(0,0,0,0.3); transition: transform 0.3s ease; }
            .donation-card:hover { transform: scale(1.03); }
            .donation-card img { width:100%; height:200px; object-fit:cover; }
            .donation-card h2 { margin:10px; font-size:24px; text-align:center; }
            .donation-card p { margin:0 10px 10px 10px; font-size:16px; line-height:1.4; }
            .donation-card a.donate { display:block; margin:10px; padding:10px; background-color:#7FB77E; color:#1C1C1C; text-align:center; font-weight:bold; border-radius:8px; text-decoration:none; transition: background 0.3s ease; }
            .donation-card a.donate:hover { background-color:#95C18F; }
            .back { display:block; text-align:center; margin:20px auto; color:white; font-weight:bold; font-size:20px; text-decoration:none; transition: color 0.3s ease; }
            .back:hover { color:#A8E6A2; }
        </style>
    </head>
    <body>
        <header><h1>Сохранение животных</h1></header>
        <main>
            <div class="donation-card">
                <img src="/static/images/animal_conservation1.jpg" alt="Тигр">
                <h2>Тигр</h2>
                <p>Помогите сохранить редких животных в дикой природе. Ваша помощь важна!</p>
                <a href="#" class="donate">Помочь</a>
            </div>
            <div class="donation-card">
                <img src="/static/images/animal_conservation2.jpg" alt="Слон">
                <h2>Слон</h2>
                <p>Проект по сохранению слонов нуждается в поддержке волонтёров и пожертвований.</p>
                <a href="#" class="donate">Помочь</a>
            </div>
        </main>
        <a href="/animals" class="back">← Вернуться назад</a>
    </body>
    </html>
    '''


# -------------------------------
# 🔹 Категория "Экология" с подкатегориями
# -------------------------------
@app.route('/ecology')
def ecology():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Экология</title>
        <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            body { font-family:'Quicksand', Arial, sans-serif; margin:0; padding:0; background:#344E41; color:#E0E0E0; }
            header { background:#3A5A40; color:white; padding:20px; text-align:center; }
            h1 { margin:0; font-size:48px; }
            main { display:grid; grid-template-columns:repeat(3,1fr); gap:20px; padding:20px; justify-items:center; }
            .category { background-color:#6C8E63; border:1px solid #2E4F4F; border-radius:15px; padding:25px; width:230px; text-align:center; transition:all 0.4s ease; font-size:20px; font-weight:700; color:#1C1C1C; box-shadow:0 4px 6px rgba(0,0,0,0.3);}
            .category:hover { background-color:#547D4B; transform:scale(1.05); color:#1C1C1C; cursor:pointer; }
            .category a { color:inherit; text-decoration:none; display:block; }
            a.back { display:block; margin-top:20px; color:#E0E0E0; text-decoration:none; font-weight:bold; text-align:center; }
            a.back:hover { text-decoration:underline; }
        </style>
    </head>
    <body>
        <header>
            <h1>Экология</h1>
            <p>Выберите подкатегорию</p>
        </header>
        <main>
            <div class="category"><a href="/tree_planting">Посадка деревьев</a></div>
            <div class="category"><a href="/territory_cleaning">Уборка территорий</a></div>
            <div class="category"><a href="/waste_recycling">Переработка отходов</a></div>
            <div class="category"><a href="/nature_protection">Защита природы</a></div>
        </main>
        <style>
        .back {
            display: block;           /* Чтобы заняло всю ширину */
            text-align: center;       /* Центрируем текст */
            margin: 20px auto;        /* Отступ сверху/снизу */
            color: white;             /* Белый цвет */
            font-weight: bold;        /* Жирный текст */
            font-size: 20px;          /* Размер текста */
            text-decoration: none;    /* Без подчеркивания */
            transition: color 0.3s ease;
        }
        .back:hover {
            color: #A8E6A2;           /* Светло-зелёный при наведении */
        }
        </style>
        <a href="/" class="back">← Вернуться на основную</a>
    </body>
    </html>
    '''

# 🔹 Подкатегории Экологии
# -------------------------------
# -------------------------------
# 🔹 Категория "Экология"
# -------------------------------

# 🌳 Посадка деревьев
@app.route('/tree_planting')
def tree_planting_cards():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Посадка деревьев</title>
        <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            body { font-family:'Quicksand', Arial, sans-serif; margin:0; padding:0; background:#344E41; color:#E0E0E0; }
            header { background:#3A5A40; color:white; padding:20px; text-align:center; }
            h1 { margin:0; font-size:48px; }
            main { display:flex; flex-wrap:wrap; gap:20px; justify-content:center; padding:20px; }
            .donation-card { background-color:#6C8E63; border:1px solid #2E4F4F; border-radius:15px; width:300px; display:flex; flex-direction:column; overflow:hidden; box-shadow:0 4px 6px rgba(0,0,0,0.3); transition: transform 0.3s ease; }
            .donation-card:hover { transform: scale(1.03); }
            .donation-card img { width:100%; height:200px; object-fit:cover; }
            .donation-card h2 { margin:10px; font-size:24px; text-align:center; }
            .donation-card p { margin:0 10px 10px 10px; font-size:16px; line-height:1.4; }
            .donation-card a.donate { display:block; margin:10px; padding:10px; background-color:#7FB77E; color:#1C1C1C; text-align:center; font-weight:bold; border-radius:8px; text-decoration:none; transition: background 0.3s ease; }
            .donation-card a.donate:hover { background-color:#95C18F; }
            .back { display:block; text-align:center; margin:20px auto; color:white; font-weight:bold; font-size:20px; text-decoration:none; transition: color 0.3s ease; }
            .back:hover { color:#A8E6A2; }
        </style>
    </head>
    <body>
        <header><h1>Посадка деревьев</h1></header>
        <main>
            <div class="donation-card">
                <img src="/static/images/planting1.jpg" alt="Саженцы">
                <h2>Саженцы для леса</h2>
                <p>Поосадка деревьев в городских парках и лесах.</p>
                <a href="#" class="donate">Помочь</a>
            </div>
            <div class="donation-card">
                <img src="/static/images/planting2.jpg" alt="Волонтёры">
                <h2>Волонтёры на закупке</h2>
                <p>Закупка деревьев, растений в местные парки, районы, леса.</p>
                <a href="#" class="donate">Помочь</a>
            </div>
        </main>
        <a href="/ecology" class="back">← Вернуться назад</a>
    </body>
    </html>
    '''

# 🧹 Уборка территорий
@app.route('/territory_cleaning')
def territory_cleaning_cards():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Уборка территорий</title>
        <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            body { font-family:'Quicksand', Arial, sans-serif; margin:0; padding:0; background:#344E41; color:#E0E0E0; }
            header { background:#3A5A40; color:white; padding:20px; text-align:center; }
            h1 { margin:0; font-size:48px; }
            main { display:flex; flex-wrap:wrap; gap:20px; justify-content:center; padding:20px; }
            .donation-card { background-color:#6C8E63; border:1px solid #2E4F4F; border-radius:15px; width:300px; display:flex; flex-direction:column; overflow:hidden; box-shadow:0 4px 6px rgba(0,0,0,0.3); transition: transform 0.3s ease; }
            .donation-card:hover { transform: scale(1.03); }
            .donation-card img { width:100%; height:200px; object-fit:cover; }
            .donation-card h2 { margin:10px; font-size:24px; text-align:center; }
            .donation-card p { margin:0 10px 10px 10px; font-size:16px; line-height:1.4; }
            .donation-card a.donate { display:block; margin:10px; padding:10px; background-color:#7FB77E; color:#1C1C1C; text-align:center; font-weight:bold; border-radius:8px; text-decoration:none; transition: background 0.3s ease; }
            .donation-card a.donate:hover { background-color:#95C18F; }
            .back { display:block; text-align:center; margin:20px auto; color:white; font-weight:bold; font-size:20px; text-decoration:none; transition: color 0.3s ease; }
            .back:hover { color:#A8E6A2; }
        </style>
    </head>
    <body>
        <header><h1>Уборка территорий</h1></header>
        <main>
            <div class="donation-card">
                <img src="/static/images/clean1.jpg" alt="Уборка парков">
                <h2>Уборка парков</h2>
                <p>Помощь в очистке парковых зон от мусора.</p>
                <a href="#" class="donate">Помочь</a>
            </div>
            <div class="donation-card">
                <img src="/static/images/clean2.jpg" alt="Пляжи">
                <h2>Очищение пляжей</h2>
                <p>Помощь в организации мероприятий по очистке пляжей и рек.</p>
                <a href="#" class="donate">Помочь</a>
            </div>
        </main>
        <a href="/ecology" class="back">← Вернуться назад</a>
    </body>
    </html>
    '''

# ♻️ Переработка отходов
@app.route('/waste_recycling')
def waste_recycling_cards():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Переработка отходов</title>
        <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            body { font-family:'Quicksand', Arial, sans-serif; margin:0; padding:0; background:#344E41; color:#E0E0E0; }
            header { background:#3A5A40; color:white; padding:20px; text-align:center; }
            h1 { margin:0; font-size:48px; }
            main { display:flex; flex-wrap:wrap; gap:20px; justify-content:center; padding:20px; }
            .donation-card { background-color:#6C8E63; border:1px solid #2E4F4F; border-radius:15px; width:300px; display:flex; flex-direction:column; overflow:hidden; box-shadow:0 4px 6px rgba(0,0,0,0.3); transition: transform 0.3s ease; }
            .donation-card:hover { transform: scale(1.03); }
            .donation-card img { width:100%; height:200px; object-fit:cover; }
            .donation-card h2 { margin:10px; font-size:24px; text-align:center; }
            .donation-card p { margin:0 10px 10px 10px; font-size:16px; line-height:1.4; }
            .donation-card a.donate { display:block; margin:10px; padding:10px; background-color:#7FB77E; color:#1C1C1C; text-align:center; font-weight:bold; border-radius:8px; text-decoration:none; transition: background 0.3s ease; }
            .donation-card a.donate:hover { background-color:#95C18F; }
            .back { display:block; text-align:center; margin:20px auto; color:white; font-weight:bold; font-size:20px; text-decoration:none; transition: color 0.3s ease; }
            .back:hover { color:#A8E6A2; }
        </style>
    </head>
    <body>
        <header><h1>Переработка отходов</h1></header>
        <main>
            <div class="donation-card">
                <img src="/static/images/recycle1.jpg" alt="Сортировка мусора">
                <h2>Сортировка отходов</h2>
                <p>Помощь в проектах по сортировке и переработке пластиковых и бумажных отходов.</p>
                <a href="#" class="donate">Помочь</a>
            </div>
            <div class="donation-card">
                <img src="/static/images/recycle2.jpg" alt="Мастер-классы">
                <h2>Обучение переработке</h2>
                <p>Помощь обучающих программ по сортировке и переработке вторсырья.</p>
                <a href="#" class="donate">Помочь</a>
            </div>
        </main>
        <a href="/ecology" class="back">← Вернуться назад</a>
    </body>
    </html>
    '''

# 🌱 Защита природы
@app.route('/nature_protection')
def nature_protection_cards():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Защита природы</title>
        <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            body { font-family:'Quicksand', Arial, sans-serif; margin:0; padding:0; background:#344E41; color:#E0E0E0; }
            header { background:#3A5A40; color:white; padding:20px; text-align:center; }
            h1 { margin:0; font-size:48px; }
            main { display:flex; flex-wrap:wrap; gap:20px; justify-content:center; padding:20px; }
            .donation-card { background-color:#6C8E63; border:1px solid #2E4F4F; border-radius:15px; width:300px; display:flex; flex-direction:column; overflow:hidden; box-shadow:0 4px 6px rgba(0,0,0,0.3); transition: transform 0.3s ease; }
            .donation-card:hover { transform: scale(1.03); }
            .donation-card img { width:100%; height:200px; object-fit:cover; }
            .donation-card h2 { margin:10px; font-size:24px; text-align:center; }
            .donation-card p { margin:0 10px 10px 10px; font-size:16px; line-height:1.4; }
            .donation-card a.donate { display:block; margin:10px; padding:10px; background-color:#7FB77E; color:#1C1C1C; text-align:center; font-weight:bold; border-radius:8px; text-decoration:none; transition: background 0.3s ease; }
            .donation-card a.donate:hover { background-color:#95C18F; }
            .back { display:block; text-align:center; margin:20px auto; color:white; font-weight:bold; font-size:20px; text-decoration:none; transition: color 0.3s ease; }
            .back:hover { color:#A8E6A2; }
        </style>
    </head>
    <body>
        <header><h1>Защита природы</h1></header>
        <main>
            <div class="donation-card">
                <img src="/static/images/nature_protection1.jpg" alt="Защита лесов">
                <h2>Сохранение лесов</h2>
                <p>Помощь проектам по сохранению лесов, заповедников и дикой природы.</p>
                <a href="#" class="donate">Помочь</a>
            </div>
            <div class="donation-card">
                <img src="/static/images/nature2.jpg" alt="Природоохранные акции">
                <h2>Эко-акции</h2>
                <p>Участие в акциях и проектах по защите редких животных и растений.</p>
                <a href="#" class="donate">Помочь</a>
            </div>
        </main>
        <a href="/ecology" class="back">← Вернуться назад</a>
    </body>
    </html>
    '''

# -------------------------------
# 🔹 Категория "Образование" с подкатегориями
# -------------------------------
@app.route('/education')
def education():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Образование</title>
        <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            body { font-family:'Quicksand', Arial, sans-serif; margin:0; padding:0; background:#344E41; color:#E0E0E0; }
            header { background:#3A5A40; color:white; padding:20px; text-align:center; }
            h1 { margin:0; font-size:48px; }
            main { display:grid; grid-template-columns:repeat(3,1fr); gap:20px; padding:20px; justify-items:center; }
            .category { background-color:#6C8E63; border:1px solid #2E4F4F; border-radius:15px; padding:25px; width:230px; text-align:center; transition:all 0.4s ease; font-size:20px; font-weight:700; color:#1C1C1C; box-shadow:0 4px 6px rgba(0,0,0,0.3);}
            .category:hover { background-color:#547D4B; transform:scale(1.05); color:#1C1C1C; cursor:pointer; }
            .category a { color:inherit; text-decoration:none; display:block; }
            a.back { display:block; margin-top:20px; color:#E0E0E0; text-decoration:none; font-weight:bold; text-align:center; }
            a.back:hover { text-decoration:underline; }
        </style>
    </head>
    <body>
        <header>
            <h1>Образование</h1>
            <p>Выберите подкатегорию</p>
        </header>
        <main>
            <div class="category"><a href="/scholarships">Стипендии</a></div>
            <div class="category"><a href="/courses_lectures">Курсы и лекции</a></div>
            <div class="category"><a href="/online_learning">Университетское обучение</a></div>
            <div class="category"><a href="/school_support">Поддержка школ</a></div>
            <div class="category"><a href="/student_aid">Помощь студентам</a></div>
        </main>
        <style>
        .back {
            display: block;           /* Чтобы заняло всю ширину */
            text-align: center;       /* Центрируем текст */
            margin: 20px auto;        /* Отступ сверху/снизу */
            color: white;             /* Белый цвет */
            font-weight: bold;        /* Жирный текст */
            font-size: 20px;          /* Размер текста */
            text-decoration: none;    /* Без подчеркивания */
            transition: color 0.3s ease;
        }
        .back:hover {
            color: #A8E6A2;           /* Светло-зелёный при наведении */
        }
        </style>
        <a href="/" class="back">← Вернуться на основную</a>
    </body>
    </html>
    '''

# Подкатегории Образования
# -------------------------------
# 🔹 Подкатегория "Стипендии"
# -------------------------------
@app.route('/scholarships')
def scholarships():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Стипендии</title>
        <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            body { font-family:'Quicksand', Arial, sans-serif; margin:0; padding:0; background:#344E41; color:#E0E0E0; }
            header { background:#3A5A40; color:white; padding:20px; text-align:center; }
            h1 { margin:0; font-size:48px; }
            main { display:flex; flex-wrap:wrap; gap:20px; justify-content:center; padding:20px; }
            .donation-card { background-color:#6C8E63; border:1px solid #2E4F4F; border-radius:15px; width:300px; display:flex; flex-direction:column; overflow:hidden; box-shadow:0 4px 6px rgba(0,0,0,0.3); transition: transform 0.3s ease; }
            .donation-card:hover { transform: scale(1.03); }
            .donation-card img { width:100%; height:200px; object-fit:cover; }
            .donation-card h2 { margin:10px; font-size:24px; text-align:center; }
            .donation-card p { margin:0 10px 10px 10px; font-size:16px; line-height:1.4; }
            .donation-card a.donate { display:block; margin:10px; padding:10px; background-color:#7FB77E; color:#1C1C1C; text-align:center; font-weight:bold; border-radius:8px; text-decoration:none; transition: background 0.3s ease; }
            .donation-card a.donate:hover { background-color:#95C18F; }
            .back { display:block; text-align:center; margin:20px auto; color:white; font-weight:bold; font-size:20px; text-decoration:none; transition: color 0.3s ease; }
            .back:hover { color:#A8E6A2; }
        </style>
    </head>
    <body>
        <header><h1>Стипендии</h1></header>
        <main>
            <div class="donation-card">
                <img src="/static/images/scholarship1.jpg" alt="Стипендия 1">
                <h2>Стипендия для студентов</h2>
                <p>Помогите талантливым студентам получать образование и развиваться профессионально.</p>
                <a href="#" class="donate">Помочь</a>
            </div>
            <div class="donation-card">
                <img src="/static/images/scholarship2.jpg" alt="Стипендия 2">
                <h2>Стипендия школьникам</h2>
                <p>Поддержка успешных школьников, с целью раскрытия их потенциала.</p>
                <a href="#" class="donate">Помочь</a>
            </div>
        </main>
        <a href="/education" class="back">← Вернуться назад</a>
    </body>
    </html>
    '''

# -------------------------------
# 🔹 Подкатегория "Курсы и лекции"
# -------------------------------
@app.route('/courses_lectures')
def courses_lectures():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Курсы и лекции</title>
        <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            body { font-family:'Quicksand', Arial, sans-serif; margin:0; padding:0; background:#344E41; color:#E0E0E0; }
            header { background:#3A5A40; color:white; padding:20px; text-align:center; }
            h1 { margin:0; font-size:48px; }
            main { display:flex; flex-wrap:wrap; gap:20px; justify-content:center; padding:20px; }
            .donation-card { background-color:#6C8E63; border:1px solid #2E4F4F; border-radius:15px; width:300px; display:flex; flex-direction:column; overflow:hidden; box-shadow:0 4px 6px rgba(0,0,0,0.3); transition: transform 0.3s ease; }
            .donation-card:hover { transform: scale(1.03); }
            .donation-card img { width:100%; height:200px; object-fit:cover; }
            .donation-card h2 { margin:10px; font-size:24px; text-align:center; }
            .donation-card p { margin:0 10px 10px 10px; font-size:16px; line-height:1.4; }
            .donation-card a.donate { display:block; margin:10px; padding:10px; background-color:#7FB77E; color:#1C1C1C; text-align:center; font-weight:bold; border-radius:8px; text-decoration:none; transition: background 0.3s ease; }
            .donation-card a.donate:hover { background-color:#95C18F; }
            .back { display:block; text-align:center; margin:20px auto; color:white; font-weight:bold; font-size:20px; text-decoration:none; transition: color 0.3s ease; }
            .back:hover { color:#A8E6A2; }
        </style>
    </head>
    <body>
        <header><h1>Курсы и лекции</h1></header>
        <main>
            <div class="donation-card">
                <img src="/static/images/courses_lectures1.jpg" alt="Курс 1">
                <h2>Онлайн-курсы</h2>
                <p>Поддержите проекты, которые дают доступ к качественным образовательным курсам для всех.</p>
                <a href="#" class="donate">Помочь</a>
            </div>
            <div class="donation-card">
                <img src="/static/images/courses_lectures2.jpg" alt="Лекция 1">
                <h2>Лекции и мастер-классы</h2>
                <p>Помощь в организации образовательных лекций и практических мастер-классов.</p>
                <a href="#" class="donate">Помочь</a>
            </div>
        </main>
        <a href="/education" class="back">← Вернуться назад</a>
    </body>
    </html>
    '''

# -------------------------------
# 🔹 Подкатегория "Университетское обучение"
# -------------------------------
@app.route('/online_learning')
def online_learning():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Университетское обучение</title>
        <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            body { font-family:'Quicksand', Arial, sans-serif; margin:0; padding:0; background:#344E41; color:#E0E0E0; }
            header { background:#3A5A40; color:white; padding:20px; text-align:center; }
            h1 { margin:0; font-size:48px; }
            main { display:flex; flex-wrap:wrap; gap:20px; justify-content:center; padding:20px; }
            .donation-card { background-color:#6C8E63; border:1px solid #2E4F4F; border-radius:15px; width:300px; display:flex; flex-direction:column; overflow:hidden; box-shadow:0 4px 6px rgba(0,0,0,0.3); transition: transform 0.3s ease; }
            .donation-card:hover { transform: scale(1.03); }
            .donation-card img { width:100%; height:200px; object-fit:cover; }
            .donation-card h2 { margin:10px; font-size:24px; text-align:center; }
            .donation-card p { margin:0 10px 10px 10px; font-size:16px; line-height:1.4; }
            .donation-card a.donate { display:block; margin:10px; padding:10px; background-color:#7FB77E; color:#1C1C1C; text-align:center; font-weight:bold; border-radius:8px; text-decoration:none; transition: background 0.3s ease; }
            .donation-card a.donate:hover { background-color:#95C18F; }
            .back { display:block; text-align:center; margin:20px auto; color:white; font-weight:bold; font-size:20px; text-decoration:none; transition: color 0.3s ease; }
            .back:hover { color:#A8E6A2; }
        </style>
    </head>
    <body>
        <header><h1>Университетское обучение</h1></header>
        <main>
            <div class="donation-card">
                <img src="/static/images/online_learning1.jpg" alt="Поддержка студентов на целевом обучении">
                <h2>Целевое обучение</h2>
                <p>Поддержка студентов в рамках программ целевого обучения.</p>
                <a href="#" class="donate">Помочь</a>
            </div>
            <div class="donation-card">
                <img src="/static/images/online_learning2.jpg" alt="Вложения в бюджетные места в вузах">
                <h2>Бюджетные места в вузах</h2>
                <p>Вложения в расширение бюджетных мест для студентов.</p>
                <a href="#" class="donate">Помочь</a>
            </div>
        </main>
        <a href="/education" class="back">← Вернуться назад</a>
    </body>
    </html>
    '''

# -------------------------------
# 🔹 Подкатегория "Поддержка школ"
# -------------------------------
@app.route('/school_support')
def school_support():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Поддержка школ</title>
        <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            body { font-family:'Quicksand', Arial, sans-serif; margin:0; padding:0; background:#344E41; color:#E0E0E0; }
            header { background:#3A5A40; color:white; padding:20px; text-align:center; }
            h1 { margin:0; font-size:48px; }
            main { display:flex; flex-wrap:wrap; gap:20px; justify-content:center; padding:20px; }
            .donation-card { background-color:#6C8E63; border:1px solid #2E4F4F; border-radius:15px; width:300px; display:flex; flex-direction:column; overflow:hidden; box-shadow:0 4px 6px rgba(0,0,0,0.3); transition: transform 0.3s ease; }
            .donation-card:hover { transform: scale(1.03); }
            .donation-card img { width:100%; height:200px; object-fit:cover; }
            .donation-card h2 { margin:10px; font-size:24px; text-align:center; }
            .donation-card p { margin:0 10px 10px 10px; font-size:16px; line-height:1.4; }
            .donation-card a.donate { display:block; margin:10px; padding:10px; background-color:#7FB77E; color:#1C1C1C; text-align:center; font-weight:bold; border-radius:8px; text-decoration:none; transition: background 0.3s ease; }
            .donation-card a.donate:hover { background-color:#95C18F; }
            .back { display:block; text-align:center; margin:20px auto; color:white; font-weight:bold; font-size:20px; text-decoration:none; transition: color 0.3s ease; }
            .back:hover { color:#A8E6A2; }
        </style>
    </head>
    <body>
        <header><h1>Поддержка школ</h1></header>
        <main>
            <div class="donation-card">
                <img src="/static/images/school_support1.jpg" alt="Школа 1">
                <h2>Помощь школам</h2>
                <p>Поддержка школ оборудованием, учебными материалами и проектами для учеников.</p>
                <a href="#" class="donate">Помочь</a>
            </div>
            <div class="donation-card">
                <img src="/static/images/school_support2.jpg" alt="Школа 2">
                <h2>Развитие образовательной инфраструктуры</h2>
                <p>Помощь в улучшении условий обучения и доступности образования.</p>
                <a href="#" class="donate">Помочь</a>
            </div>
        </main>
        <a href="/education" class="back">← Вернуться назад</a>
    </body>
    </html>
    '''

# -------------------------------
# 🔹 Подкатегория "Помощь студентам"
# -------------------------------
@app.route('/student_aid')
def student_aid():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Помощь студентам</title>
        <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            body { font-family:'Quicksand', Arial, sans-serif; margin:0; padding:0; background:#344E41; color:#E0E0E0; }
            header { background:#3A5A40; color:white; padding:20px; text-align:center; }
            h1 { margin:0; font-size:48px; }
            main { display:flex; flex-wrap:wrap; gap:20px; justify-content:center; padding:20px; }
            .donation-card { background-color:#6C8E63; border:1px solid #2E4F4F; border-radius:15px; width:300px; display:flex; flex-direction:column; overflow:hidden; box-shadow:0 4px 6px rgba(0,0,0,0.3); transition: transform 0.3s ease; }
            .donation-card:hover { transform: scale(1.03); }
            .donation-card img { width:100%; height:200px; object-fit:cover; }
            .donation-card h2 { margin:10px; font-size:24px; text-align:center; }
            .donation-card p { margin:0 10px 10px 10px; font-size:16px; line-height:1.4; }
            .donation-card a.donate { display:block; margin:10px; padding:10px; background-color:#7FB77E; color:#1C1C1C; text-align:center; font-weight:bold; border-radius:8px; text-decoration:none; transition: background 0.3s ease; }
            .donation-card a.donate:hover { background-color:#95C18F; }
            .back { display:block; text-align:center; margin:20px auto; color:white; font-weight:bold; font-size:20px; text-decoration:none; transition: color 0.3s ease; }
            .back:hover { color:#A8E6A2; }
        </style>
    </head>
    <body>
        <header><h1>Помощь студентам</h1></header>
        <main>
            <div class="donation-card">
                <img src="/static/images/student_aid1.jpg" alt="Студент 1">
                <h2>Финансовая поддержка</h2>
                <p>Помощь студентам с оплатой обучения и приобретением учебников.</p>
                <a href="#" class="donate">Помочь</a>
            </div>
            <div class="donation-card">
                <img src="/static/images/student_aid2.jpg" alt="Студент 2">
                <h2>Стипендии и гранты</h2>
                <p>Поддержка талантливых студентов для реализации их проектов и исследований.</p>
                <a href="#" class="donate">Помочь</a>
            </div>
        </main>
        <a href="/education" class="back">← Вернуться назад</a>
    </body>
    </html>
    '''


# -------------------------------
# 🔹 Категория "Чрезвычайные ситуации" с подкатегориями
# -------------------------------
@app.route('/emergency')
def emergency():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Чрезвычайные ситуации</title>
        <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            body { font-family:'Quicksand', Arial, sans-serif; margin:0; padding:0; background:#344E41; color:#E0E0E0; }
            header { background:#3A5A40; color:white; padding:20px; text-align:center; }
            h1 { margin:0; font-size:48px; }
            main { display:grid; grid-template-columns:repeat(3,1fr); gap:20px; padding:20px; justify-items:center; }
            .category { background-color:#6C8E63; border:1px solid #2E4F4F; border-radius:15px; padding:25px; width:230px; text-align:center; transition:all 0.4s ease; font-size:20px; font-weight:700; color:#1C1C1C; box-shadow:0 4px 6px rgba(0,0,0,0.3);}
            .category:hover { background-color:#547D4B; transform:scale(1.05); color:#1C1C1C; cursor:pointer; }
            .category a { color:inherit; text-decoration:none; display:block; }
            a.back { display:block; margin-top:20px; color:#E0E0E0; text-decoration:none; font-weight:bold; text-align:center; }
            a.back:hover { text-decoration:underline; }
        </style>
    </head>
    <body>
        <header>
            <h1>Чрезвычайные ситуации</h1>
            <p>Выберите подкатегорию</p>
        </header>
        <main>
            <div class="category"><a href="/fires">Пожары</a></div>
            <div class="category"><a href="/earthquakes">Землетрясения</a></div>
            <div class="category"><a href="/refugees">Беженцы</a></div>
            <div class="category"><a href="/medical_aid">Медицинская помощь</a></div>
        </main>
        <style>
        .back {
            display: block;           /* Чтобы заняло всю ширину */
            text-align: center;       /* Центрируем текст */
            margin: 20px auto;        /* Отступ сверху/снизу */
            color: white;             /* Белый цвет */
            font-weight: bold;        /* Жирный текст */
            font-size: 20px;          /* Размер текста */
            text-decoration: none;    /* Без подчеркивания */
            transition: color 0.3s ease;
        }
        .back:hover {
            color: #A8E6A2;           /* Светло-зелёный при наведении */
        }
        </style>
        <a href="/" class="back">← Вернуться на основную</a>
    </body>
    </html>
    '''

# Подкатегории ЧС
# -------------------------------
# 🔹 Подкатегории Чрезвычайных ситуаций с карточками
# -------------------------------
@app.route('/fires')
def fires_cards():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Пожары</title>
        <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            body { font-family:'Quicksand', Arial, sans-serif; margin:0; padding:0; background:#344E41; color:#E0E0E0; }
            header { background:#3A5A40; color:white; padding:20px; text-align:center; }
            h1 { margin:0; font-size:48px; }
            main { display:flex; flex-wrap:wrap; gap:20px; justify-content:center; padding:20px; }
            .donation-card {
                background-color:#6C8E63;
                border:1px solid #2E4F4F;
                border-radius:15px;
                width:300px;
                display:flex;
                flex-direction:column;
                overflow:hidden;
                box-shadow:0 4px 6px rgba(0,0,0,0.3);
                transition: transform 0.3s ease;
            }
            .donation-card:hover { transform: scale(1.03); }
            .donation-card img { width:100%; height:200px; object-fit:cover; }
            .donation-card h2 { margin:10px; font-size:24px; text-align:center; }
            .donation-card p { margin:0 10px 10px 10px; font-size:16px; line-height:1.4; }
            .donation-card a.donate {
                display:block;
                margin:10px;
                padding:10px;
                background-color:#7FB77E;
                color:#1C1C1C;
                text-align:center;
                font-weight:bold;
                border-radius:8px;
                text-decoration:none;
                transition: background 0.3s ease;
            }
            .donation-card a.donate:hover { background-color:#95C18F; }
            .back { display:block; margin:20px auto; color:white; font-weight:bold; font-size:20px; text-align:center; text-decoration:none; transition: color 0.3s ease; }
            .back:hover { color:#A8E6A2; }
        </style>
    </head>
    <body>
        <header>
            <h1>Пожары</h1>
        </header>
        <main>
            <div class="donation-card">
                <img src="/static/images/fires1.jpg" alt="Пожар 1">
                <h2>Помощь пострадавшим от пожаров</h2>
                <p>Сбор средств на восстановление домов и обеспечение безопасности людей в зонах пожаров.</p>
                <a href="#" class="donate">Помочь</a>
            </div>
            <div class="donation-card">
                <img src="/static/images/fires2.jpg" alt="Пожар 2">
                <h2>Эвакуация и поддержка</h2>
                <p>Помощь в эвакуации, временное жильё и необходимые вещи для пострадавших.</p>
                <a href="#" class="donate">Помочь</a>
            </div>
        </main>
        <a href="/emergency" class="back">← Вернуться назад</a>
    </body>
    </html>
    '''

@app.route('/earthquakes')
def earthquakes_cards():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Землетрясения</title>
        <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            body { font-family:'Quicksand', Arial, sans-serif; margin:0; padding:0; background:#344E41; color:#E0E0E0; }
            header { background:#3A5A40; color:white; padding:20px; text-align:center; }
            h1 { margin:0; font-size:48px; }
            main { display:flex; flex-wrap:wrap; gap:20px; justify-content:center; padding:20px; }
            .donation-card {
                background-color:#6C8E63;
                border:1px solid #2E4F4F;
                border-radius:15px;
                width:300px;
                display:flex;
                flex-direction:column;
                overflow:hidden;
                box-shadow:0 4px 6px rgba(0,0,0,0.3);
                transition: transform 0.3s ease;
            }
            .donation-card:hover { transform: scale(1.03); }
            .donation-card img { width:100%; height:200px; object-fit:cover; }
            .donation-card h2 { margin:10px; font-size:24px; text-align:center; }
            .donation-card p { margin:0 10px 10px 10px; font-size:16px; line-height:1.4; }
            .donation-card a.donate {
                display:block;
                margin:10px;
                padding:10px;
                background-color:#7FB77E;
                color:#1C1C1C;
                text-align:center;
                font-weight:bold;
                border-radius:8px;
                text-decoration:none;
                transition: background 0.3s ease;
            }
            .donation-card a.donate:hover { background-color:#95C18F; }
            .back { display:block; margin:20px auto; color:white; font-weight:bold; font-size:20px; text-align:center; text-decoration:none; transition: color 0.3s ease; }
            .back:hover { color:#A8E6A2; }
        </style>
    </head>
    <body>
        <header>
            <h1>Землетрясения</h1>
        </header>
        <main>
            <div class="donation-card">
                <img src="/static/images/quake1.jpg" alt="Землетрясение 1">
                <h2>Помощь пострадавшим от землетрясений на Сахалине</h2>
                <p>Финансовая поддержка для пострадавших, восстановление инфраструктуры и жилья.</p>
                <a href="#" class="donate">Помочь</a>
            </div>
            <div class="donation-card">
                <img src="/static/images/quake2.jpg" alt="Землетрясение 2">
                <h2>Помощь пострадавшим от землетрясений на Камчатке</h2>
                <p>Финансовая поддержка для пострадавших, восстановление инфраструктуры и жилья.</p>
                <a href="#" class="donate">Помочь</a>
            </div>
        </main>
        <a href="/emergency" class="back">← Вернуться назад</a>
    </body>
    </html>
    '''

@app.route('/refugees')
def refugees_cards():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Беженцы</title>
        <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            body { font-family:'Quicksand', Arial, sans-serif; margin:0; padding:0; background:#344E41; color:#E0E0E0; }
            header { background:#3A5A40; color:white; padding:20px; text-align:center; }
            h1 { margin:0; font-size:48px; }
            main { display:flex; flex-wrap:wrap; gap:20px; justify-content:center; padding:20px; }
            .donation-card {
                background-color:#6C8E63;
                border:1px solid #2E4F4F;
                border-radius:15px;
                width:300px;
                display:flex;
                flex-direction:column;
                overflow:hidden;
                box-shadow:0 4px 6px rgba(0,0,0,0.3);
                transition: transform 0.3s ease;
            }
            .donation-card:hover { transform: scale(1.03); }
            .donation-card img { width:100%; height:200px; object-fit:cover; }
            .donation-card h2 { margin:10px; font-size:24px; text-align:center; }
            .donation-card p { margin:0 10px 10px 10px; font-size:16px; line-height:1.4; }
            .donation-card a.donate {
                display:block;
                margin:10px;
                padding:10px;
                background-color:#7FB77E;
                color:#1C1C1C;
                text-align:center;
                font-weight:bold;
                border-radius:8px;
                text-decoration:none;
                transition: background 0.3s ease;
            }
            .donation-card a.donate:hover { background-color:#95C18F; }
            .back { display:block; margin:20px auto; color:white; font-weight:bold; font-size:20px; text-align:center; text-decoration:none; transition: color 0.3s ease; }
            .back:hover { color:#A8E6A2; }
        </style>
    </head>
    <body>
        <header>
            <h1>Беженцы</h1>
        </header>
        <main>
            <div class="donation-card">
                <img src="/static/images/refugee1.jpg" alt="Беженцы">
                <h2>Поддержка семей беженцев</h2>
                <p>Сбор средств на питание, временное жильё и медицинскую помощь беженцам.</p>
                <a href="#" class="donate">Помочь</a>
            </div>
            <div class="donation-card">
                <img src="/static/images/refugee2.jpg" alt="Беженцы">
                <h2>Поддержка беженцев при природных катастрофах</h2>
                <p>Сбор средств на питание, временное жильё и медицинскую помощь беженцам.</p>
                <a href="#" class="donate">Помочь</a>
            </div>
        </main>
        <a href="/emergency" class="back">← Вернуться назад</a>
    </body>
    </html>
    '''

@app.route('/medical_aid')
def medical_aid_cards():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Медицинская помощь</title>
        <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            body { font-family:'Quicksand', Arial, sans-serif; margin:0; padding:0; background:#344E41; color:#E0E0E0; }
            header { background:#3A5A40; color:white; padding:20px; text-align:center; }
            h1 { margin:0; font-size:48px; }
            main { display:flex; flex-wrap:wrap; gap:20px; justify-content:center; padding:20px; }
            .donation-card {
                background-color:#6C8E63;
                border:1px solid #2E4F4F;
                border-radius:15px;
                width:300px;
                display:flex;
                flex-direction:column;
                overflow:hidden;
                box-shadow:0 4px 6px rgba(0,0,0,0.3);
                transition: transform 0.3s ease;
            }
            .donation-card:hover { transform: scale(1.03); }
            .donation-card img { width:100%; height:200px; object-fit:cover; }
            .donation-card h2 { margin:10px; font-size:24px; text-align:center; }
            .donation-card p { margin:0 10px 10px 10px; font-size:16px; line-height:1.4; }
            .donation-card a.donate {
                display:block;
                margin:10px;
                padding:10px;
                background-color:#7FB77E;
                color:#1C1C1C;
                text-align:center;
                font-weight:bold;
                border-radius:8px;
                text-decoration:none;
                transition: background 0.3s ease;
            }
            .donation-card a.donate:hover { background-color:#95C18F; }
            .back { display:block; margin:20px auto; color:white; font-weight:bold; font-size:20px; text-align:center; text-decoration:none; transition: color 0.3s ease; }
            .back:hover { color:#A8E6A2; }
        </style>
    </head>
    <body>
        <header>
            <h1>Медицинская помощь</h1>
        </header>
        <main>
            <div class="donation-card">
                <img src="/static/images/medical1.jpg" alt="Медицинская помощь">
                <h2>Сбор на поддержку медучреждений</h2>
                <p>Финансовая поддержка на лекарства, оборудование и лечение пострадавших.</p>
                <a href="#" class="donate">Помочь</a>
            </div>
            <div class="donation-card">
                <img src="/static/images/medical2.jpg" alt="Медицинская помощь">
                <h2>Сбор на медицинские нужды (мед. материалы)</h2>
                <p>Финансовая поддержка на лекарства, оборудование и лечение пострадавших.</p>
                <a href="#" class="donate">Помочь</a>
            </div>
        </main>
        <a href="/emergency" class="back">← Вернуться назад</a>
    </body>
    </html>
    '''


# -------------------------------
# 🔹 Категория "Волонтёрство" с подкатегориями
# -------------------------------
@app.route('/volunteers')
def volunteers():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Волонтёрство</title>
        <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            body { font-family:'Quicksand', Arial, sans-serif; margin:0; padding:0; background:#344E41; color:#E0E0E0; }
            header { background:#3A5A40; color:white; padding:20px; text-align:center; }
            h1 { margin:0; font-size:48px; }
            main { display:grid; grid-template-columns:repeat(3,1fr); gap:20px; padding:20px; justify-items:center; }
            .category { background-color:#6C8E63; border:1px solid #2E4F4F; border-radius:15px; padding:25px; width:230px; text-align:center; transition:all 0.4s ease; font-size:20px; font-weight:700; color:#1C1C1C; box-shadow:0 4px 6px rgba(0,0,0,0.3);}
            .category:hover { background-color:#547D4B; transform:scale(1.05); color:#1C1C1C; cursor:pointer; }
            .category a { color:inherit; text-decoration:none; display:block; }
            a.back { display:block; margin-top:20px; color:#E0E0E0; text-decoration:none; font-weight:bold; text-align:center; }
            a.back:hover { text-decoration:underline; }
        </style>
    </head>
    <body>
        <header>
            <h1>Волонтёрство</h1>
            <p>Выберите подкатегорию</p>
        </header>
        <main>
            <div class="category"><a href="/animal_care">Уход за животными</a></div>
            <div class="category"><a href="/shelter_help">Помощь в приютах</a></div>
            <div class="category"><a href="/event_volunteers">Волонтёры на мероприятиях</a></div>
            <div class="category"><a href="/social_initiatives">Социальные инициативы</a></div>
        </main>
        <style>
        .back {
            display: block;           /* Чтобы заняло всю ширину */
            text-align: center;       /* Центрируем текст */
            margin: 20px auto;        /* Отступ сверху/снизу */
            color: white;             /* Белый цвет */
            font-weight: bold;        /* Жирный текст */
            font-size: 20px;          /* Размер текста */
            text-decoration: none;    /* Без подчеркивания */
            transition: color 0.3s ease;
        }
        .back:hover {
            color: #A8E6A2;           /* Светло-зелёный при наведении */
        }
        </style>
        <a href="/" class="back">← Вернуться на основную</a>
    </body>
    </html>
    '''

# Подкатегории Волонтёрства
@app.route('/shelter_help')
def shelter_help():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Помощь в приютах</title>
        <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            body { font-family:'Quicksand', Arial, sans-serif; margin:0; padding:0; background:#344E41; color:#E0E0E0; }
            header { background:#3A5A40; color:white; padding:20px; text-align:center; }
            h1 { margin:0; font-size:48px; }
            main { display:flex; flex-wrap:wrap; gap:20px; justify-content:center; padding:20px; }
            .donation-card {
                background-color:#6C8E63;
                border:1px solid #2E4F4F;
                border-radius:15px;
                width:300px;
                display:flex;
                flex-direction:column;
                overflow:hidden;
                box-shadow:0 4px 6px rgba(0,0,0,0.3);
                transition: transform 0.3s ease;
            }
            .donation-card a.donate:hover { background-color:#95C18F; }
            .donation-card:hover { transform: scale(1.03); }
            .donation-card img { width:100%; height:200px; object-fit:cover; }
            .donation-card h2 { margin:10px; font-size:24px; text-align:center; }
            .donation-card p { margin:0 10px 10px; font-size:16px; }
            .donation-card a.donate {
                display:block; margin:10px; padding:10px;
                background-color:#7FB77E; color:#1C1C1C;
                text-align:center; font-weight:bold;
                border-radius:8px; text-decoration:none;
            }
            .back { display:block; margin:20px auto; color:white; font-weight:bold; font-size:20px; text-align:center; text-decoration:none; transition: color 0.3s ease; }
            .back:hover { color:#A8E6A2; }
        </style>
    </head>

    <body>
        <header><h1>Помощь в приютах</h1></header>
        <main>

            <div class="donation-card">
                <img src="/static/images/shelterhelp1.jpg">
                <h2>Уборка помещений</h2>
                <p>Санитарная помощь приюту, поддержка чистоты.</p>
                <a href="#" class="donate">Принять участие</a>
            </div>

            <div class="donation-card">
                <img src="/static/images/shelterhelp2.jpg">
                <h2>Доставка вещей</h2>
                <p>Помощь с доставкой корма, медикаментов и подстилок.</p>
                <a href="#" class="donate">Принять участие</a>
            </div>

        </main>

        <a href="/volunteers" class="back">← Вернуться назад</a>
    </body>
    </html>
    '''

@app.route('/animal_care')
def animal_care():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Уход за животными</title>
        <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            body { font-family:'Quicksand', Arial, sans-serif; margin:0; padding:0; background:#344E41; color:#E0E0E0; }
            header { background:#3A5A40; color:white; padding:20px; text-align:center; }
            h1 { margin:0; font-size:48px; }
            main { display:flex; flex-wrap:wrap; gap:20px; justify-content:center; padding:20px; }
            .donation-card {
                background-color:#6C8E63;
                border:1px solid #2E4F4F;
                border-radius:15px;
                width:300px;
                display:flex;
                flex-direction:column;
                overflow:hidden;
                box-shadow:0 4px 6px rgba(0,0,0,0.3);
                transition: transform 0.3s ease;
            }
            .donation-card a.donate:hover { background-color:#95C18F; }
            .donation-card:hover { transform: scale(1.03); }
            .donation-card img { width:100%; height:200px; object-fit:cover; }
            .donation-card h2 { margin:10px; font-size:24px; text-align:center; }
            .donation-card p { margin:0 10px 10px; font-size:16px; }
            .donation-card a.donate {
                display:block; margin:10px; padding:10px;
                background-color:#7FB77E; color:#1C1C1C;
                text-align:center; font-weight:bold;
                border-radius:8px; text-decoration:none;
            }
            .back { display:block; margin:20px auto; color:white; font-weight:bold; font-size:20px; text-align:center; text-decoration:none; transition: color 0.3s ease; }
            .back:hover { color:#A8E6A2; }
        </style>
    </head>

    <body>
        <header><h1>Уход за животными</h1></header>
        <main>

            <div class="donation-card">
                <img src="/static/images/animalcare1.jpg">
                <h2>Кормление животных</h2>
                <p>Помощь приютам в ежедневном уходе и кормлении.</p>
                <a href="#" class="donate">Принять участие</a>
            </div>

            <div class="donation-card">
                <img src="/static/images/animalcare2.jpg">
                <h2>Выгул собак</h2>
                <p>Прогулки, социализация и поддержка персонала приюта.</p>
                <a href="#" class="donate">Принять участие</a>
            </div>

        </main>

        <a href="/volunteers" class="back">← Вернуться назад</a>
    </body>
    </html>
    '''
@app.route('/event_volunteers')
def event_volunteers():
    return '''
    <!DOCTYPE html>
    <html>
     <head>
        <meta charset="utf-8">
        <title>Социальные инициативы</title>
        <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            body { font-family:'Quicksand', Arial, sans-serif; margin:0; padding:0; background:#344E41; color:#E0E0E0; }
            header { background:#3A5A40; color:white; padding:20px; text-align:center; }
            h1 { margin:0; font-size:48px; }
            main { display:flex; flex-wrap:wrap; gap:20px; justify-content:center; padding:20px; }
            .donation-card {
                background-color:#6C8E63;
                border:1px solid #2E4F4F;
                border-radius:15px;
                width:300px;
                display:flex;
                flex-direction:column;
                overflow:hidden;
                box-shadow:0 4px 6px rgba(0,0,0,0.3);
                transition: transform 0.3s ease;
            }
            .donation-card a.donate:hover { background-color:#95C18F; }
            .donation-card:hover { transform: scale(1.03); }
            .donation-card img { width:100%; height:200px; object-fit:cover; }
            .donation-card h2 { margin:10px; font-size:24px; text-align:center; }
            .donation-card p { margin:0 10px 10px; font-size:16px; }
            .donation-card a.donate {
                display:block; margin:10px; padding:10px;
                background-color:#7FB77E; color:#1C1C1C;
                text-align:center; font-weight:bold;
                border-radius:8px; text-decoration:none;
            }
            .back { display:block; margin:20px auto; color:white; font-weight:bold; font-size:20px; text-align:center; text-decoration:none; transition: color 0.3s ease; }
            .back:hover { color:#A8E6A2; }
        </style>
    </head>

    <body>
        <header><h1>Волонтёрные мероприятия</h1></header>
        <main>

            <div class="donation-card">
                <img src="/static/images/eventvol1.jpg">
                <h2>Городские акции</h2>
                <p>Помощь в организации благотворительных мероприятий.</p>
                <a href="#" class="donate">Принять участие</a>
            </div>

            <div class="donation-card">
                <img src="/static/images/eventvol2.jpg">
                <h2>Сортировка помощи</h2>
                <p>Перебор и упаковка гуманитарных наборов.</p>
                <a href="#" class="donate">Принять участие</a>
            </div>

        </main>

        <a href="/volunteers" class="back">← Вернуться назад</a>
    </body>
    </html>
    '''

@app.route('/social_initiatives')
def social_initiatives():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Социальные инициативы</title>
        <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            body { font-family:'Quicksand', Arial, sans-serif; margin:0; padding:0; background:#344E41; color:#E0E0E0; }
            header { background:#3A5A40; color:white; padding:20px; text-align:center; }
            h1 { margin:0; font-size:48px; }
            main { display:flex; flex-wrap:wrap; gap:20px; justify-content:center; padding:20px; }
            .donation-card {
                background-color:#6C8E63;
                border:1px solid #2E4F4F;
                border-radius:15px;
                width:300px;
                display:flex;
                flex-direction:column;
                overflow:hidden;
                box-shadow:0 4px 6px rgba(0,0,0,0.3);
                transition: transform 0.3s ease;
            }
            .donation-card a.donate:hover { background-color:#95C18F; }
            .donation-card:hover { transform: scale(1.03); }
            .donation-card img { width:100%; height:200px; object-fit:cover; }
            .donation-card h2 { margin:10px; font-size:24px; text-align:center; }
            .donation-card p { margin:0 10px 10px; font-size:16px; }
            .donation-card a.donate {
                display:block; margin:10px; padding:10px;
                background-color:#7FB77E; color:#1C1C1C;
                text-align:center; font-weight:bold;
                border-radius:8px; text-decoration:none;
            }
            .back { display:block; margin:20px auto; color:white; font-weight:bold; font-size:20px; text-align:center; text-decoration:none; transition: color 0.3s ease; }
            .back:hover { color:#A8E6A2; }
        </style>
    </head>

    <body>
        <header><h1>Социальные инициативы</h1></header>
        <main>

            <div class="donation-card">
                <img src="/static/images/social1.jpg">
                <h2>Помощь малоимущим</h2>
                <p>Сбор еды, одежды и средств гигиены.</p>
                <a href="#" class="donate">Принять участие</a>
            </div>

            <div class="donation-card">
                <img src="/static/images/social2.jpg">
                <h2>Поддержка пожилых</h2>
                <p>Сопровождение, помощь по дому и доставке продуктов.</p>
                <a href="#" class="donate">Принять участие</a>
            </div>

        </main>

        <a href="/volunteers" class="back">← Вернуться назад</a>
    </body>
    </html>
    '''

# -------------------------------
# 🔹 Статистика с актуальными нуждами
# -------------------------------
@app.route('/statistics')
def statistics():
    current_needs = {
        "Детям": 15,
        "Пожилым людям": 8,
        "Больным детям": 12,
        "Больным взрослым": 6,
        "Семьям в трудной ситуации": 10,
        "Бездомным животным": 9,
        "Диким животным": 5,
        "Приютам": 7,
        "Спасение животных": 8,
        "Посадка деревьев": 11,
        "Уборка территорий": 6,
        "Переработка отходов": 4,
        "Защита природы": 7,
        "Стипендии": 9,
        "Курсы и лекции": 5,
        "Университетское обучение": 6,
        "Поддержка школ": 4,
        "Помощь студентам": 8,
        "Пожары": 3,
        "Землетрясения": 2,
        "Беженцы": 5,
        "Медицинская помощь": 6,
        "Уход за животными": 4,
        "Помощь в приютах": 5,
        "Волонтёры на мероприятиях": 3,
        "Социальные инициативы": 2
    }

    categories = list(current_needs.keys())
    values = list(current_needs.values())

    fig = go.Figure([go.Bar(x=categories, y=values, marker_color='#4CC790')])
    fig.update_layout(
        title='ТОП-актуальных нужд пользователей',
        xaxis_tickangle=-45,
        plot_bgcolor='#344E41',
        paper_bgcolor='#344E41',
        font=dict(color='#E0E0E0', family='Quicksand')
    )

    graph_div = pyo.plot(fig, output_type='div', include_plotlyjs=True)

    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Статистика</title>
        <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            body {{ font-family:'Quicksand', Arial, sans-serif; background:#344E41; color:#E0E0E0; margin:0; padding:0; }}
            header {{ background:#3A5A40; color:white; padding:20px; text-align:center; }}
            h1 {{ margin:0; font-size:48px; }}
            nav {{
                background-color: #2E3B2F;
                display:flex;
                justify-content:center;
                gap:25px;
                padding:15px 0;
            }}
            nav a {{
                color:white;
                text-decoration:none;
                font-weight:700;
                padding:8px 15px;
                font-size:20px;
                border-radius:5px;
                transition: background 0.3s ease, transform 0.3s ease;
            }}
            nav a:hover {{
                background-color:#276748;
                transform: scale(1.05);
            }}
            footer {{ background:#344E41; color:#E0E0E0; text-align:center; padding:15px; margin-top:20px; }}
            .summary {{ padding:20px; font-size:18px; line-height:1.5; }}
        </style>
    </head>
    <body>
        <header>
            <h1>Статистика актуальных нужд</h1>
        </header>
        <nav>
            <a href="/">Основная</a>
            <a href="/statistics">Статистика</a>
            <a href="/about">О нас</a>
        </nav>
        <div class="summary">
            <p>ТОП-3 самых востребованных категорий на данный момент:</p>
            <ol>
                <li>{max(current_needs, key=current_needs.get)}</li>
                <li>{sorted(current_needs, key=current_needs.get, reverse=True)[1]}</li>
                <li>{sorted(current_needs, key=current_needs.get, reverse=True)[2]}</li>
            </ol>
            <p>Данные основаны на актуальных мировых потребностях и запросах пользователей.</p>
        </div>
        {graph_div}
        <footer>
            <p>© 2025 Добрые сердца. Все права защищены.</p>
        </footer>
    </body>
    </html>
    '''
# -------------------------------
# 🔹 Вкладка "О нас"
# -------------------------------
@app.route('/about')
def about():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>О нас</title>
        <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            body { font-family:'Quicksand', Arial, sans-serif; background:#344E41; color:#E0E0E0; margin:0; padding:0; }
            header { background:#3A5A40; color:white; padding:20px; text-align:center; }
            h1 { margin:0; font-size:48px; }
            main { padding:20px; line-height:1.5; font-size:18px; }
            nav { background-color: #2E3B2F; display:flex; justify-content:center; gap:25px; padding:15px 0; }
            nav a { color:white; text-decoration:none; font-weight:700; padding:8px 15px; font-size:20px; border-radius:5px; transition: background 0.3s ease, transform 0.3s ease; }
            nav a:hover { background-color:#276748; transform: scale(1.05); }
            footer { background:#344E41; color:#E0E0E0; text-align:center; padding:15px; margin-top:20px; }
        </style>
    </head>
    <body>
        <header>
            <h1>О нас</h1>
        </header>
        <nav>
            <a href="/">Основная</a>
            <a href="/statistics">Статистика</a>
            <a href="/about">О нас</a>
        </nav>
        <main>
            <p>«Добрые сердца» — это проект, который объединяет людей, желающих помогать. Мы собрали в одном \
                 месте самые важные направления поддержки: помощь людям, животным, экологии, пострадавшим в \
                    чрезвычайных ситуациях и волонтёрские инициативы. Мы создали этот сайт, чтобы сделать \
                         помощь доступной и удобной — каждому, кто готов сделать мир добрее.</p>
            <p>Связаться с нами можно по телефону: +7 (999) 123-45-67</p>
            <p>Электронная почта: info@dobrieserdca.ru</p>
        </main>
        <footer>
            <p>© 2025 Добрые сердца. Все права защищены.</p>
        </footer>
    </body>
    </html>
    '''

# -------------------------------
# 🔹 Запуск сайта
# -------------------------------
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)  # 🔹 Запуск сайта Flask на всех интерфейсах, порт 5000, включен режим отладки