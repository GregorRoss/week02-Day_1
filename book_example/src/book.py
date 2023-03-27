class Book:
    def __init__(self, book_title, book_author, year, pulped):
        self.title = book_title
        self.author = book_author
        self.date_of_publication = year
        self.number_pulped = pulped

    def read(self):
        return 'It put me into a coma'
    
