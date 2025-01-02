def read_file(file_path):
    """Читает содержимое файла и возвращает его как строку."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {file_path} не найден.")
    except Exception as e:
        raise Exception(f"Ошибка при чтении файла {file_path}: {e}")
