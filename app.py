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
    <h1>Пожилым людям</h1>
    <p>Подкатегории: одинокие пожилые, ветераны, пенсионеры в нужде</p>
    <a href="/people" class="back">← Вернуться назад</a>
    '''

@app.route('/sick_children')
def sick_children():
    return '''
    <h1>Больным детям</h1>
    <p>Подкатегории: онкобольные, с хроническими заболеваниями, с редкими болезнями</p>
    <a href="/people" class="back">← Вернуться назад</a>
    '''

@app.route('/sick_adults')
def sick_adults():
    return '''
    <h1>Больным взрослым</h1>
    <p>Подкатегории: онкобольные, после операций, с хроническими заболеваниями</p>
    <a href="/people" class="back">← Вернуться назад</a>
    '''

@app.route('/families')
def families():
    return '''
    <h1>Семьям в трудной ситуации</h1>
    <p>Подкатегории: малоимущие семьи, многодетные, пострадавшие от катастроф</p>
    <a href="/people" class="back">← Вернуться назад</a>
    '''

# -------------------------------
# 🔹 Остальные категории с подкатегориями
# -------------------------------

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

# 🔹 Подкатегории Животным
@app.route('/homeless_animals')
def homeless_animals():
    return '<h1>Бездомные животные</h1><a href="/animals" class="back">← Вернуться назад</a>'

@app.route('/wild_animals')
def wild_animals():
    return '<h1>Дикие животные</h1><a href="/animals" class="back">← Вернуться назад</a>'

@app.route('/shelters')
def shelters():
    return '<h1>Приюты</h1><a href="/animals" class="back">← Вернуться назад</a>'

@app.route('/animal_rescue')
def animal_rescue():
    return '<h1>Спасение животных</h1><a href="/animals" class="back">← Вернуться назад</a>'


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
@app.route('/tree_planting')
def tree_planting():
    return '<h1>Посадка деревьев</h1><a href="/ecology" class="back">← Вернуться назад</a>'

@app.route('/territory_cleaning')
def territory_cleaning():
    return '<h1>Уборка территорий</h1><a href="/ecology" class="back">← Вернуться назад</a>'

@app.route('/waste_recycling')
def waste_recycling():
    return '<h1>Переработка отходов</h1><a href="/ecology" class="back">← Вернуться назад</a>'

@app.route('/nature_protection')
def nature_protection():
    return '<h1>Защита природы</h1><a href="/ecology" class="back">← Вернуться назад</a>'


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
            <div class="category"><a href="/online_learning">Онлайн-обучение</a></div>
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
@app.route('/scholarships')
def scholarships():
    return '<h1>Стипендии</h1><a href="/education" class="back">← Вернуться назад</a>'

@app.route('/courses_lectures')
def courses_lectures():
    return '<h1>Курсы и лекции</h1><a href="/education" class="back">← Вернуться назад</a>'

@app.route('/online_learning')
def online_learning():
    return '<h1>Онлайн-обучение</h1><a href="/education" class="back">← Вернуться назад</a>'

@app.route('/school_support')
def school_support():
    return '<h1>Поддержка школ</h1><a href="/education" class="back">← Вернуться назад</a>'

@app.route('/student_aid')
def student_aid():
    return '<h1>Помощь студентам</h1><a href="/education" class="back">← Вернуться назад</a>'


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
@app.route('/fires')
def fires():
    return '<h1>Пожары</h1><a href="/emergency" class="back">← Вернуться назад</a>'

@app.route('/earthquakes')
def earthquakes():
    return '<h1>Землетрясения</h1><a href="/emergency" class="back">← Вернуться назад</a>'

@app.route('/refugees')
def refugees():
    return '<h1>Беженцы</h1><a href="/emergency" class="back">← Вернуться назад</a>'

@app.route('/medical_aid')
def medical_aid():
    return '<h1>Медицинская помощь</h1><a href="/emergency" class="back">← Вернуться назад</a>'


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
@app.route('/animal_care')
def animal_care():
    return '<h1>Уход за животными</h1><a href="/volunteers" class="back">← Вернуться назад</a>'

@app.route('/shelter_help')
def shelter_help():
    return '<h1>Помощь в приютах</h1><a href="/volunteers" class="back">← Вернуться назад</a>'

@app.route('/event_volunteers')
def event_volunteers():
    return '<h1>Волонтёры на мероприятиях</h1><a href="/volunteers" class="back">← Вернуться назад</a>'

@app.route('/social_initiatives')
def social_initiatives():
    return '<h1>Социальные инициативы</h1><a href="/volunteers" class="back">← Вернуться назад</a>'

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
        "Онлайн-обучение": 6,
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
            <p>Мы — команда проекта «Добрые сердца», объединяющая людей и организации для помощи тем, кто в этом нуждается.</p>
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