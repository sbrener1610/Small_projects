import datetime


books = [
    {
        "title":"Title1",
        "author":"Author1",
        "year":1999,
        "loaned":"NO"
    },
    {
        "title":"Title2",
        "author":"Author2",
        "year":2000,
        "loaned":"NO"
    },
    {
        "title":"Title2",
        "author":"Author3",
        "year":2020,
        "loaned":"NO"
    },
    {
        "title":"Title3",
        "author":"Author3",
        "year":2010,
        "loaned":"NO"
    },
    {
        "title":"Cool title",
        "author":"Sucking author",
        "year":2015,
        "loaned":"NO"
    },
    {
        "title":"Cool title",
        "author":"Cool author",
        "year":2007,
        "loaned":"NO"
    },
    {
        "title":"Title7",
        "author":"Author1",
        "year":2003,
        "loaned":"NO"
    }
]
loans = {}

def add_book(title, author, year):
    books.append({
        "title":title,
        "author":author,
        "year":year,
        "loaned":"NO"
    })

def remove_book(id_book):
    books.pop(id_book)
    books.insert(id_book,{"title":"","author":"","year":None,"loaned":"NO"})

def loan_book(borrower,id_book,days_):
    due_date=datetime.datetime.now()+datetime.timedelta(days=days_)
    if not loans.get(borrower):
        loans.update({borrower:[(id_book,due_date)]})
    else: 
        loans[borrower].append((id_book,due_date))
    books[id_book].update({"loaned":due_date})

def return_book(borrower,id_book):
    for i in loans[borrower]:
        if i[0]==id_book: 
            loans[borrower].remove(i)
            books[id_book].update({"loaned":"NO"})

def is_in_library(title):
    for i in books:
        if i.get(title):
            print(f"We have {i} in the library.")

def show_library():
    for i in books:
        if i["title"]:
            print(f"We have {i['title']} by {i['author']}, year {i['year']} in the library.", end="")
            if i["loaned"]!="NO":
                print("(loaned)")
            else:
                print("")
        

def show_loans():
    for i in loans:
        for j in loans[i]:
            print(f"{i} borrowed {books[j[0]]['title']} by {books[j[0]]['author']}, year {books[j[0]]['year']} until {j[1]}")

def show_books_by_author(author):
    for i in books:
        if i["author"]==author:
            print(f"We have {i['title']} by {i['author']}, year {i['year']} in the library.")

