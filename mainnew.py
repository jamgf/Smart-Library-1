#number 2 time
import datetime
import os

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

    def display_books(self):
        print("-------------List of books----------------")
        print("Books ID","\t", "Title")
        print("------------------------------------------")

        for key, value in self.books_dict.items():
            print(key, "\t\t", value.get("books_title"),"- [",value.get("Status"),"]")

    def Issue_books(self):
        books_id = input("Enter books ID: ")
        current_date = datetime.datetime.now().strftime("%Y-%m_%d %H:%M:%S")
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]["Status"] == "Available":
                print(f"This book is already issued to {self.books_dict[books_id]['lender_name']} on {self.books_dict[books_id]['Issue_date']}")
                return self.Issue_books()
            elif self.books_dict[books_id]['Status'] == "Available":
                your_name = input("Enter your name: ")
                self.books_dict[books_id]['lender_name'] = your_name
                self.books_dict[books_id]['Issue_date'] = current_date
                self.books_dict[books_id]['Status'] = "Already Issued"
                print("Book Issued Successfully!")
        else:
            print("Book ID not found!")
            return self.Issue_books()
        
program = LMS("list_of_books.txt","Python's Library")
print(program.display_books())