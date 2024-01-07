class User:
    def __init__(self, name, email, phone, id, address):
        self.title = name   
        self.qtpage = email
        self.isbn = phone
        self.author = id
        self.location = address

    
    def rentABook(self):
        print('create a rentId')