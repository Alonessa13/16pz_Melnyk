def run_task1():
    # Принцип SRP — Кожен клас відповідає лише за одну задачу

    # Клас описує книгу (тільки дані)
    class Book:
        def __init__(self, title, author):
            self.title = title
            self.author = author

    # Вивід інформації
    class BookPrinter:
        def print_info(self, book):
            print(f"\nНазва книги: {book.title}")
            print(f"Автор: {book.author}")

    # Редагування книги
    class BookEditor:
        def update_title(self, book, new_title):
            book.title = new_title

        def update_author(self, book, new_author):
            book.author = new_author

    # Клас для збереження книги (наприклад, у базу даних чи файл)
    class BookStorage:
        def save(self, book):
            print(f"\nКнига '{book.title}' успішно збережена!")

    # --- Основна логіка ---
    title = input("Введіть назву книги: ")
    author = input("Введіть автора книги: ")
    book = Book(title, author)

    printer = BookPrinter()
    editor = BookEditor()
    storage = BookStorage()

    printer.print_info(book)

    # Оновлення
    new_title = input("\nБажаєте змінити назву? Введіть нову (або натисніть Enter): ")
    if new_title:
        editor.update_title(book, new_title)

    new_author = input("Бажаєте змінити автора? Введіть нового (або натисніть Enter): ")
    if new_author:
        editor.update_author(book, new_author)

    printer.print_info(book)
    storage.save(book)
