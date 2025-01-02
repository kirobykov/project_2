class MovieCollection:
    """Класс для управления коллекцией фильмов."""

    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def __iter__(self):
        return iter(self.movies)
