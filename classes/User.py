class User:
    
    def __init__(self, name, email_address, password):
        self.name = name
        self.email_address = email_address
        self.password = password
        
    def __str__(self):
        return f"Name: {self.name}, Email Address: {self.email_address}, Password: {self.password}"

    def get_password(self):
        return self.password