from bs4 import BeautifulSoup
from .exceptions import FileNotFoundError
from .utils.file_utils import read_file
from .utils.validation import validate_movie_title
import os

class MovieScraper:
    def __init__(self, html_file):
        self.html_file = html_file
        self.validate_file()

    def validate_file(self):
        """Проверка существования файла."""
        if not os.path.exists(self.html_file):
            raise FileNotFoundError(f"Файл {self.html_file} не найден.")

    def get_movie_titles(self):
        """Извлечение названий фильмов из HTML."""
        html_content = read_file(self.html_file)
        soup = BeautifulSoup(html_content, 'html.parser')
        movie_divs = soup.find_all('div', class_='name')
        
        titles = []
        for div in movie_divs:
            title = div.get_text().strip()
            validate_movie_title(title)  # Валидация названия фильма
            titles.append(title)
        
        return titles
