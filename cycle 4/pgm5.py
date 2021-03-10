class publisher:
    def title(self):
        print("TITLE OF BOOK")
    def author(self):
        print("AUTHOR OF THE BOOK::*********")

class book(publisher):
    def title1(self):
        print("BOOK NAME is python")
    def price_book(self):
        print("Price of the book::343")

    def no_of_page_book(self):
        print("NO_OF_PAGES:500")

class python(book):
    def price_python(self):
            print("Price of the book::343")

    def no_of_page_python(self):
        print("NO_OF_PAGES:1000")

obj=python()
obj.title()
obj.author()
obj.title1()
obj.price_book()
obj.no_of_page_book()
obj.price_python()
obj.no_of_page_python()

