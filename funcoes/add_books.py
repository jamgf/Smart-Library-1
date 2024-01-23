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