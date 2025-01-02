class Movie:
    """Класс для представления фильма."""

    def __init__(self, title):
        self.title = title

    def __str__(self):
        return self.title
