# Путь к файлу HTML
HTML_FILE = 'movies.html'

def add_movie(cover, title, desc,site):
    movie_html = f'''
        <div class="movie-item">
            <img src="{cover}" alt="Movie 3">
            <h3>{title}</h3>
            <p>{desc}<p>
            <a href="{site}">Смотреть</a>
        </div>
    '''
    return movie_html

def insert_movie_html(movie_html):
    with open(HTML_FILE, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # Вставка нового фильма на 26 строку
    insertion_index = 144  # 26-я строка (индексы в списке начинаются с 0)
    lines.insert(insertion_index, movie_html + '\n')
    
    with open(HTML_FILE, 'w', encoding='utf-8') as file:
        file.writelines(lines)

def main():
    while True:
        print("Добавить новый фильм")
        cover = input("Обложка (ссылка): ")
        title = input("Название фильма: ")
        desc = input("Описание фильма: ")
        site = input("Название сайта(.html): ")
        movie_html = add_movie(cover, title, desc, site)
        insert_movie_html(movie_html)
        
        more = input("Хотите добавить еще один фильм? (да/нет): ")
        if more.lower() != 'да':
            break

if __name__ == '__main__':
    main()

