def display_books(self):
        print("-------------List of books----------------")
        print("Books ID","\t", "Title")
        print("------------------------------------------")

        for key, value in self.books_dict.items():
            print(key, "\t\t", value.get("books_title"),"- [",value.get("Status"),"]")
