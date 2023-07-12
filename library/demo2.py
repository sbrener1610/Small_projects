import demo as library


while True:
    print("\nLibrary Menu:")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Loan a book")
    print("4. Return a book")
    print("5. Check if a book is in the library")
    print("6. Show all books in the library")
    print("7. Show all borrowed books and their due dates")
    print("8. Show all books by a certain author")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title=input("Title: ")
        author=input("Author: ")
        year=input("Year: ")
        library.add_book(title,author,year)
        print(f"{library.books[-1]} added.")
    elif choice == "2":
        title=input("Title: ")
        for i in library.books:
            if i["title"]==title:
                if i["loaned"]!="NO":
                    print(f"The book is loaned until {i['loaned']}")
                else:
                    confirm=input(f"Sure? Remove {i}? y/n")
                    if confirm.lower()=="y":
                        library.remove_book(library.books.index(i))
                        print(f"{i} deleted.")

    elif choice == "3":
        borrower=input("Borrower: ")
        title=input("Title: ")
        lent=0
        for i in library.books:
            if i["title"]==title and i["loaned"]=="NO":
                confirm=input(f"Sure? Loan {i} to {borrower}? y/n ")
                if confirm.lower()=="y":
                    while True:
                        try:
                            days_=int(input("Days: "))
                            break
                        except ValueError:
                            print("enter a number")
                    library.loan_book(borrower,library.books.index(i),days_)
                    print(f"{i} loaned to {borrower} for {days_} days.")
                    lent=1
                    break
        if not lent:
            print("No book loaned.")
    elif choice == "4":
        borrower=input("Borrower: ")
        title=input("Title: ")
        for i in library.loans[borrower]:
            if library.books[i[0]]["title"]==title:
                confirm=input(f"Return {library.books[i[0]]}? y/n ")
                if confirm.lower()=="y":
                    library.return_book(borrower,i[0])
                    print(f"{borrower} returned {title} by library.books[i[0]]['author'], year {library.books[i[0]]['year']}")
                    break
            print("No book returned.")


    elif choice == "5":
        title=input("Title: ")
        library.is_in_library(title)
    elif choice == "6":
        library.show_library()
    elif choice == "7":
        library.show_loans()
    elif choice == "8":
        author=input("Author: ")
        library.show_books_by_author(author)
    elif choice == "9":
        print("Exiting the program. Have a nice day!")
        break
    else:
        print("Invalid choice. Please choose a number between 1 and 9.")
