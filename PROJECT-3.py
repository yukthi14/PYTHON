class Library:
    
    def __init__(self,listOfBooks):
        self.books=listOfBooks
    def displayAvailableBooks(self):
        print("Books present in this library are:")
        for book in self.books:
        
            print(" - "+book)
    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please handle in care and return within 25 days")  
            self.books.remove(bookName)
            return True    
        else:
            print("Sorry,This book is been issued to someone else.Please wait until the book is returned")
            return False
    def returnBook(self,bookName):
        self.books.append(bookName)
        print("Thanks for returning the book! Hope you enjoyed reading it!")

class student:
   
    
    def requestBook(self):
        self.book=input("Enter the name of the book to borrow :")
        return self.book
    
    def returnBook(self):
        self.book=input("Enter the name of the book you want to return :")
        return self.book

if __name__ == '__main__':
    CentralLibrary=Library(["Data structure","Programming in c","Java","Python","Python core","Computer networking","Database management system","Algorithm"])
    student=student()
    CentralLibrary.displayAvailableBooks()
    while(True):
        welcome=''' ******Welcome to Central Library******
        Please choose an option:
        1.Listing all the books.
        2.Request a book.
        3.Return a book.
        4.Exit the Library.
        '''
        print(welcome)
        a=int(input("Enter a choice:"))
        if a==1:
            CentralLibrary.displayAvailableBooks()
        elif a==2:
            CentralLibrary.borrowBook(student.requestBook())
        elif a==3:
            CentralLibrary.returnBook(student.returnBook())      
        elif a==4:
            print("Thanks for choosing Central Library , have a great day ahead!")
            exit()
        else:
            print("!!Invaild Choice!!")       
       
