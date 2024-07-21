


import json

def load_data(data_file):
    try:
        with open(data_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data(data, data_file):
    with open(data_file, 'w') as f:
        json.dump(data, f, indent=4)
    return data

class Book:
    _id_counter = 1
    def __init__(self, title, author, year, status="в наличии"):
        self.id = Book._id_counter
        Book._id_counter += 1
        self.title = normalize_string(title)
        self.author = normalize_string(author)
        self.year = year
        self.status = status

    def __str__(self):
        return f"Book {self.id}: {self.title} by {self.author}, {self.year} ({self.status})"

    def set_status(self, status):
        if status in ["в наличии", "выдана"]:
            self.status = status
        else:
            raise ValueError("Invalid status")

    def get_status(self):
        return self.status

class Library:
    def __init__(self, library_file=None):
        if library_file:
            self.data = load_data(library_file)
        else:
            self.data = load_data('library_file.json')

    def add_book(self, book):

        if not self.search_book(book.title,book.author,None):
          self.data.append(book.__dict__)
          save_data(self.data, 'library_file.json')
          print(f'Книга "{book.title}" добавлена в библиотеку.')
        else:
          print("Такая книгу уже существует")

    def delete_book(self, book_id):
      results = self.search_book(None,None,(book_id))
      print(results)
      if results:
            for book in results:
                self.data.remove(book)
                save_data(self.data, 'library_file.json')
                print(f'Книга с id {book_id} удалена.')
            return
      else:
        print(f'Книга с id {book_id} не найдена.')

    def view_book(self, book_id):
        results = self.search_book(None,None,(book_id))
        if results:
            for book in results:
                print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Status: {book['status']}")
        else:
            print(f'Книга с id {book_id} не найдена.')

    def view_all_books(self):
        for book in self.data:
            print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Status: {book['status']}")

    def change_status(self, book_id, status):
      results = self.search_book(None,None,(book_id))
      if results:
            for book in results:
                book['status']= status
                print(f'Статус книги с id {book_id} изменен на {status}')
            save_data(self.data, 'library_file.json')
            return
      else:
        print(f'Книга с id {book_id} не найдена.')

    def search_book(self,title,author,book_id):
        results = []
        for book in self.data:
            if title and normalize_string(title) in book['title'] or author and normalize_string(author) in book['author'] or book_id and book_id ==book['id']:
                results.append(book)
        return results


def print_menu():
  print('Меню:')
  print('1. Добавить книгу')
  print('2. Удалить книгу')
  print('3. Поиск книги')
  print('4. Отобразить все книги')
  print('5. Изменить статус книги')
  print('6. Выход')

def normalize_string(s):
    s = ' '.join(s.split())
    s = ''.join(c for c in s if c.isalnum() or c.isspace())
    s = s.lower()
    return s

def main():
  library_1=Library()
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
              book=Book(title, author, year)
              library_1.add_book(book)
      elif choice == '2':
            book_id = input('Введите id книги для удаления: ')
            if not book_id.isdigit():
              print("Ошибка ввода")
            else:
              book_id =int(book_id)
              library_1.delete_book(book_id)
      elif choice == '3':
            title = input('Введите название книги: ')
            author = input('Введите автора книги: ')
            book_id = input('Введите id книги: ')

            if book_id and not book_id.isdigit():
              print("Ошибка ввода")
            else:
              results =  library_1.search_book(title,author,book_id)
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
              book_id =int(book_id)
              status= input('Введите status книги для изменения статуса: ')
              library_1.change_status(book_id,status )
      elif choice == '6':
            break
      else:
            print('Неверный выбор. Попробуйте снова.')

if __name__ == '__main__':
    main()

