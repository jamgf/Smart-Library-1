#number 2 time
import datetime
import os
from funcoes import display_books, issue_books, add_books,return_books

class LMS:
    #class to save the books
    def __init__(self,list_of_books, library_name):
        self.list_of_books = "list_of_books.txt"
        self.library_name = library_name
        self.books_dict = {}
        Id = 101
        with open(self.list_of_books) as bk:
            content = bk.readlines()
        for line in content:
            self.books_dict.update({str(Id):{"books_title":line.replace("\n",""),
            "lender_name":"","Issue_date":"","Status":"Available"}})
            Id = Id + 1

    
    
        
    


   

try:
    myLMS = LMS('list_of_books.txt', 'Python')
    press_key_list = {"D": "Display books","I": "Issue books", "A":"Add books",
                      "R":"Return books", "Q":"Quit program"}
    key_press = False
    while not (key_press == "q"):
        print(f"\n---------Welcome to {myLMS.library_name} --------")
        for key,value in press_key_list.items():
            print("Press", key, "To", value)
            key_press = input("Press key: ").lower()
            if key_press == "i":
                print("\nCurrent selection: Issue books")
                myLMS.issue_books()
            elif key_press == "a":
                print("\nCurrent selection: Add books")
                myLMS.add_books()
            elif key_press == "d":
                print("\nCurrent selection: Display books")
                myLMS.display_books()
            elif key_press == "r":
                print("\nCurrent selection: Return books")
                myLMS.return_books()
            elif key_press == "q":
                break
            else:
                continue
except Exception as e:
    print("Something went wrong. Choose again")
program = LMS("list_of_books.txt","Python's Library")
print(program.display_books())