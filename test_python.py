
import unittest



class TestLibrary(unittest.TestCase):
    def setUp(self):

        self.library = Library("test.json")

    def test_add_book(self):

        book = Book("Test Book", "Test Author", 2022)
        self.library.add_book(book)
        self.assertIn(book.__dict__, self.library.data)

    def test_delete_book(self):
        book = Book("Test Book", "Test Author", 2022)
        self.library.add_book(book)
        self.library.delete_book(book.id)
        self.assertNotIn(book.__dict__, self.library.data)


    def test_change_status(self):
        book = Book("Test Book", "Test Author", 2022)
        self.library.add_book(book)
        self.library.change_status(book.id, "выдана")
        self.assertEqual(book.status, "выдана")

    def test_search_book(self):
        book1 = Book("Test Book 20", "Test Author 1", 2022)
        self.library.add_book(book1)
        results = self.library.search_book("Test Book 1","Test Author 1",None)
        self.assertIn(book1.__dict__, results)

    def test_search_book_1(self):
        book1 = Book("Test Book 1", "Test Author 1", 2022)
        self.library.add_book(book1)
        results = self.library.search_book("Test Book 1","Test Author 1",None)
        self.assertIn(book1.__dict__, results)


if __name__ == '__main__':

  s = unittest.TestLoader().loadTestsFromTestCase(TestLibrary)
  unittest.TextTestRunner().run(s)
