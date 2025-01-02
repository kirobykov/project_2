class MovieScraperError(Exception):
    """Базовый класс для исключений MovieScraper."""
    pass

class FileNotFoundError(MovieScraperError):
    """Исключение для случая, когда файл не найден."""
    pass
