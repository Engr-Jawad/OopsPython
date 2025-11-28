class BOOK:
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
    
    def show_book_data(self):
        return f"title of the book is : {self.title}\nauthor of the book is : {self.author}\npages : {self.pages}"
    
if __name__=="__main__":
    b1=BOOK("fundementals of python ", "guido van rossum ",700)
    print(b1.show_book_data())