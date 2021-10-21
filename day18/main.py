import datetime
import sys
import os

class Book():
    def __init__(self, title=None, author=None, idi=None):
        self.title = title
        self.author = author
        if not idi:
            self.iid = self.set_id()
        else:
            self.iid = idi
        self.date = self.set_date()    
        
    def set_id(self):
        with open("forid.txt", "r+") as r:
            re = r.read()
            if not re:
                re = 0
            r.seek(0)
            m = int(re) + 1
            r.write(str(m))        
            return m    
        
    def set_date(self):
        a = datetime.datetime.now().strftime("%d %B, %Y")
        return a

    def add_book(self):
        with open('book.txt','a+') as e:
            e.write(f'Book ID | {self.iid} | -Book Name:{self.title}-Writer Name:{self.author}-Added in:{self.date}\n')        
            
        print("Added Succesfully") 

    def show_all(self):
        with open ('book.txt','r') as r:
            a = r.read().split("-")
        for i in a:
            print(i)     
    
    def show_book(self):
        with open('book.txt','r') as g:
            arr = g.readlines()
            # print(arr)
            for i in arr:
                l = i.split("|")
                # print(l[1])
                if l[1].strip() == show_id:
                    j = "".join(l).split("-")
                    print('************\n')
                    for i in j:
                        print(i)
                    print('************')            

    def remove_book(self):
        with open("book.txt", "r") as r:
            b = r.readlines()        
        with open("book.txt", "w") as r:
            for i in b:
                w = i.split("|")[1].strip()
                if w != self.iid:
                    r.write(i)

a = sys.argv
if a[1] == "add_book":
    title = input("Enter book name:")
    autor = input("Enter writer name:")
    b = Book(title=title, author=autor)
    b.add_book()
    
if a[1] == "show_all":
    b = Book()
    b.show_all()

if a[1] == "remove_book":
    show_id = input("Write Book Id:")
    b = Book(idi=show_id)
    b.remove_book()

if a[1] == "show_book":
    show_id = input("Write Book Id:")
    b = Book(idi=show_id)
    b.show_book()