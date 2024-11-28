def create_html_page(filename, title, cover, source, year,ratio):
    html_content = f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Cмотреть онлайн</title>
    <link rel="stylesheet" href="movies.css">
</head>
<body>

<header>
    <div class="logo">Kinogo</div>
    <nav>
        <a href="index.html">Главная</a>
        <a href="#">Фильмы</a>
        <a href="#">Сериалы</a>
        <a href="#">Новинки</a>
        <a href="#">Контакты</a>
    </nav>
</header>

<div class="movie-banner">
    <h1>{title} | Cмотреть онлайн</h1>
    <p>Смотрите онлайн в хорошем качестве</p>
</div>

<div class="movie-details">
    <div class="movie-poster">
        <img src="{cover}" alt="{title} | Cмотреть онлайн" width="100%">
    </div>
    <div class="movie-info">
        <h2>Год выпуска:{year}</h2>
        <p class="rating">Рейтинг: {ratio} / 10</p>
        <iframe title="{title}" class="videoo" data-src="{source}" data-was-processed="true"></iframe>
    </div>
</div>

<footer>
    <p>&copy; 2024 Kinogo. Все права защищены.</p>
</footer>

</body>
</html>
"""
    if not filename.endswith(".html"):
        filename += ".html"
        
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(html_content)
    print(f'HTML-страница {filename} успешно создана.')

# Пример использования
filename = input("Название страницы: ")
title = input("Тайтл страницы: ")
cover = input("Обложка (ссылка): ")  # Теперь переменная cover
source = input("Источник видео (ссылка): ")
year = int(input("Год выпуска: "))
ratio = input("Оценка: ")
create_html_page(filename, title, cover, source, ratio, year)
