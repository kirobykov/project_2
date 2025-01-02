from moviescraper.scraper import MovieScraper

def main():
    html_file_path = 'path_to_html_file.html'  # Укажите путь к вашему HTML файлу
    scraper = MovieScraper(html_file_path)
    try:
        movies = scraper.get_movie_titles()
        print("Названия фильмов:")
        for movie in movies:
            print(movie)
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
