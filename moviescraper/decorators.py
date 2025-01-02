def log_execution(func):
    """Декоратор для логирования выполнения функции."""
    def wrapper(*args, **kwargs):
        print(f"Вызов функции: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Функция {func.__name__} завершила выполнение.")
        return result
    return wrapper
