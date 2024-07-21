
import json

def load_data(data_file: str) -> list:
    """
    Loads data from a JSON file.

    Args:
        data_file (str): The file path to load data from.

    Returns:
        list: The loaded data.
    """
    try:
        with open(data_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data(data: list, data_file: str) -> list:
    """
    Saves data to a JSON file.

    Args:
        data (list): The data to save.
        data_file (str): The file path to save data to.

    Returns:
        list: The saved data.
    """
    with open(data_file, 'w') as f:
        json.dump(data, f, indent=4)
    return data

class Book:
    """
    Represents a book object.
    """
    _id_counter: int = 1

    def __init__(self, title: str, author: str, year: int, status: str = "в наличии"):
        """
        Initializes a book object.

        Args:
            title (str): The book title.
            author (str): The book author.
            year (int): The book year.
            status (str): The book status.
        """
        self.id: int = Book._id_counter
        Book._id_counter += 1
        self.title: str = normalize_string(title)
        self.author: str = normalize_string(author)
        self.year: int = year
        self.status: str = status

    def __str__(self) -> str:
        """
        Returns a string representation of the book.
        """
        return f"Book {self.id}: {self.title} by {self.author}, {self.year} ({self.status})"

    def set_status(self, status: str) -> None:
        """
        Sets the book status.

        Args:
            status (str): The new book status.
        """
        if status in ["в наличии", "выдана"]:
            self.status = status
        else:
            raise ValueError("Invalid status")

    def get_status(self) -> str:
        """
        Returns the book status.
        """
        return self.status

class Library:
    """
    Represents a library object.
    """
    def __init__(self, library_file: str = None):
        """
        Initializes a library object.

        Args:
            library_file (str): The file path to load data from.
        """
        if library_file:
            self.data: list = load_data(library_file)
        else:
            self.data: list = load_data('library_file.json')

    def change_status(self, book_id: int, status: str) -> None:
        """
        Changes the status of a book.

        Args:
            book_id (int): The book ID to change status.
            status (str): The new book status.
        """
        results = self.search_book(None, None, (book_id))
        if results:
            for book in results:
                book['status'] = status
                print(f'Статус книги с id {book_id} изменен на {status}')
            save_data(self.data, 'library_file.json')
            return
        else:
            print(f'Книга с id {book_id} не найдена.')

    def search_book(self, title: str, author: str, book_id: int) -> list:
        """
        Searches for a book in the library.

        Args:
            title (str): The book title to search.
            author (str): The book author to search.
            book_id (int): The book ID to search.

        Returns:
            list: The search results.
        """
        results = []
        for book in self.data:
            if title and normalize_string(title) in book['title'] or author and normalize_string(author) in book['author'] or book_id and book_id == book['id']:
                results.append(book)
        return results


def print_menu() -> None:
    """
    Prints the menu options.
    """
    print('Меню:')
    print('1. Добавить книгу')
    print('2. Удалить книгу')
    print('3. Поиск книги')
    print('4. Отобразить все книги')
    print('5. Изменить статус книги')
    print('6. Выход')


def normalize_string(s: str) -> str:
    """
    Normalizes a string by removing extra spaces and converting to lowercase.

    Args:
        s (str): The string to normalize.

    Returns:
        str: The normalized string.
    """
    s = '.join(s.split())
    s = ''.join(c for c in s if c.isalnum() or c.isspace())
    s = s.lower()
    return s


def main() -> None:
    """
    The main function of the program.
    """
    library_1 = Library()
    while True:
        print_menu()
        choice = input('Выберите пункт меню: ')
        if choice == '1':
            title = input('Введите название книги: ')
            author = input('Введите автора книги: ')
            year = input('Введите год издания книги: ')
            if not year.isdigit():
                print("Ошибка ввода")
            else:
                book = Book(title, author, year)
                library_1.add_book(book)
        elif choice == '2':
            book_id = input('Введите id книги для удаления: ')
            if not book_id.isdigit():
                print("Ошибка ввода")
            else:
                book_id = int(book_id)
                library_1.delete_book(book_id)
        elif choice == '3':
            title = input('Введите название книги: ')
            author = input('Введите автора книги: ')
            book_id = input('Введите id книги: ')
            if book_id and not book_id.isdigit():
                print("Ошибка ввода")
            else:
                results = library_1.search_book(title, author, book_id)
                if results:
                    for book in results:
                        print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Status: {book['status']}")
                else:
                    print('Книга не найдена.')
        elif choice == '4':
            library_1.view_all_books()
        elif choice == '5':
            book_id = input('Введите id книги для изменения статуса: ')
            if not book_id.isdigit():
                print("Ошибка ввода")
            else:
                book_id = int(book_id)
                status = input('Введите status книги для изменения статуса: ')
                library_1.change_status(book_id, status)
        elif choice == '6':
            break
        else:
            print('Неверный выбор. Попробуйте снова.')

if __name__ == '__main__':
    main()




if __name__ == '__main__':

  s = unittest.TestLoader().loadTestsFromTestCase(TestLibrary)
  unittest.TextTestRunner().run(s)
