import os
library={}
def clear_screen():
    os.system(
        "cls" if os.name=="nt" else "clear"
    )
def book_storage():
    while True:
        clear_screen()
        isbn=input("Enter ISBN : ")
        title=input("Enter the title of the book: ")
        author=input("Enter the name of the composer: ")
        library[isbn]={
            "Title":title,
            "Author":author,
            "Availability":True,
        }
        print(f"Book {[library[isbn]["Title"]]} by {[library[isbn]["Author"]]} added to the catalog with ISBN {[isbn]}")
        repeat =input("Do you want to add a second book? (y/n): ")
        if repeat.lower() !="y":
            break
def borrowing_book():
    while True:
        clear_screen()
        isbn_book=input("Enter the ISBN of the book you are borrowing: ")
        if isbn_book in library:
            if library[isbn_book]["Availability"]:
                library[isbn_book]["Availability"]=False
                print(f"Book {[library[isbn_book]["Title"]]} Successfully borrowed.")
            else:
                print("Sorry, the book was borrowed by.")
        else:
            print("A book that does not exist.")
        repeat=input("Do you want to borrow another book? (y/n): ") 
        if repeat.lower() !="y":
            break
def return_book():
    while True:
        clear_screen()
        isbs_return=input("Enter your ISBN in the book you want to return: ")
        if isbs_return in library:
            if not library[isbs_return]["Availability"]:
                library[isbs_return]["Availability"]=True
                print(f"Book {[library[isbs_return]["Title"]]} Successfully restored.")
            else:
                print("Sorry this book is not borrowed from the beginning.")
        else:
            print("A book is not available in the office.")
        repeat=input("Do you want to return another book? (y/n): ")
        if repeat.lower() !="y":
            break
def view_books():
    while True:
        clear_screen()
        if not library:
            print("The library is empty.")
        else:
            print("Library Catalog:")
            for isbn in library:
                book=library[isbn]
                print(f"ISBN:{isbn}, Title: {book["Title"]}, Author: {book["Author"]}, Availability:{book["Availability"]}")
            repeat=input("Do you want to come back to the main menu? (y/n): ")
            if repeat.lower() =="y":
                break
while True:
    clear_screen()
    print("Menu:")
    print("1- Add a book to the store")
    print("2- Borrowing a book from the store")
    print("3- Return the borrowed book to the store")
    print("4- View all the books in the library")
    print("5- Get out")
    selection=input("Enter your choice according to the operation you want to perform 1-5: ")
    if selection=="1":
        book_storage()
    elif selection=="2":
        borrowing_book()
    elif selection=="3":
        return_book()
    elif selection=="4":
        view_books()
    elif selection=="5":
        clear_screen()
        print("Exited...")
        break
    else:
        print("A choice that is not available in the menu.")
        input("Press Inter to return...")