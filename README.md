# MovieScraper

## Автор
ФИО: Быков Кирилл Витальевич, ИСУ: 471786

## Описание
MovieScraper - это инструмент для извлечения названий фильмов из HTML-документов. Он позволяет парсить данные и обрабатывать их для дальнейшего использования.

## Установка
Установите необходимые зависимости с помощью pip:
```bash
pip install -r requirements.txt

## Примеры использования
from moviescraper.scraper import MovieScraper

scraper = MovieScraper('path_to_html_file.html')
movies = scraper.get_movie_titles()
print(movies)
