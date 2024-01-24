import datetime
class Admistrator:
    def __init__(self, name, email, phone, id, address):
        self.title = name   
        self.qtpage = email
        self.isbn = phone
        self.author = id
        

    
    def add_books(self):
        new_books = input("Enter books title:")
        if new_books == "":
            return self.add_books()
        elif len(new_books) > 25:
            print("Books title length is too long. Title length should be 20 chars")
            return self.add_books()
        else:
            with open(self.list_of_books,"a") as bk:
                bk.writelines(f"{new_books}\n")
                self.books_dict.update({str(int(max(self.books_dict))+1):{'books_title':new_books,'lender_name':'',
                'Issue_date':'', 'Status':'Available'}})
                print(f"This books '{new_books}' has been added successfully")



    def issue_books(self):
        books_id = input("Enter books ID: ")
        current_date = datetime.datetime.now().strftime("%Y-%m_%d %H:%M:%S")
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]["Status"] == "Available":
                print(f"This book is already issued to {self.books_dict[books_id]['lender_name']} on {self.books_dict[books_id]['Issue_date']}")
                return self.issue_books()
            elif self.books_dict[books_id]['Status'] == "Available":
                your_name = input("Enter your name: ")
                self.books_dict[books_id]['lender_name'] = your_name
                self.books_dict[books_id]['Issue_date'] = current_date
                self.books_dict[books_id]['Status'] = "Already Issued"
                print("Book Issued Successfully!")
        else:
            print("Book ID not found!")

            return self.issue_books()
        
    def return_books(self):
        books_id = input('Enter books Id: ')
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]['Status'] == 'Available':
                print('This book is already available in library')
                return return_books()
            elif not self.books_dict[books_id]['Status'] == 'Available':
                self.books_dict[books_id]['lender_name'] = ''
                self.books_dict[books_id]['Issue_date'] = ''
                self.books_dict[books_id]['Status'] = 'Available'
                print('Successfully updated')
            else:
                print('Book ID is not found \n')