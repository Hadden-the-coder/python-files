class Book:
    def __init__(self,name,author,price,publishing_year):
        self.book_name = name
        self.book_author = author
        self.book_price = price
        self.book_publishing_year = publishing_year
    def add_book(self):
        print("book: "+ self.book_name)
        print("author: "+ (self.book_author))
        print("price: "+ str(self.book_price))
        print("publishing_year: "+ str(self.book_publishing_year))
        print("book added")
book1 = Book("Diary of a Wimpy Kid","jeff Kiney",700, 2007)
book1.add_book()

book2 = Book("Harry potter and the soccerer stone","J.K Rowling",1928,1997)
book2.add_book()