def validate_movie_title(title):
    """Проверяет, что название фильма не пустое и является строкой."""
    if not isinstance(title, str):
        raise ValueError("Название фильма должно быть строкой.")
    if not title.strip():
        raise ValueError("Название фильма не может быть пустым.")
