#define class book
class Book:
    #class attribute (shared by all instances)
    library_name = "City libary"

    def __init__(self, title: str, author: str, pages: int ):
        #instance attributes (unique per object)
        self.title = title
        self.author = author
        self.pages = pages
    
    def info(self) -> str:
        return f"'{self.title}' by {self.author} ({self.pages} pages)"
    
    def is_long(self) -> bool:
        return self.pages > 400

    @classmethod
    def from_dict(cls, d: dict) -> "Book":
        return cls(d["title"], d["author"], d["pages"])

    @staticmethod
    def help() -> str:
        return "Book(title, author, pages) - pages should be a positive integer."
    

#create some book instances
b1 = Book("Clean Code", "Robert C. Martin", 464)
b2 = Book.from_dict({"title": "The Pragmatic Programmer", "author": "Hunt & Thomas", "pages": 352})
b3 = b1.from_dict({"title": "The Pragmatic Programmer", "author": "Hunt & Thomas", "pages": 352})
    
print(Book.library_name) #class attribute
print (b1.library_name)
print (b2.library_name)
print(b1.info(), b1.is_long())
print(b2.info(), b2.is_long())
print(b3.info(), b3.is_long())
print (b1.help())
print (b2.help())
print (b3.help())
print (Book.help())

