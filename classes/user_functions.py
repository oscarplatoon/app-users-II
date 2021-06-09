from classes.User import User
from csv import writer
import time
import csv
import os.path

my_path = os.path.abspath(os.path.dirname(__file__))
path_users = os.path.join(my_path, "../data/users.csv")
path_posts = os.path.join(my_path, "../data/posts.csv")

class User_functions():

    def __init__(self):
        self.users = []
        self.runner()

    # User interface
    def runner(self):

        while True:
            mode = input("\nWhat would you like to do?\nOptions:\n1. Enter new user\n2. Show all Users\n3. Create post\n5. Quit\n")

            if mode == '1':
                self.add_user()
            elif mode == '2':
                self.show_users()
            elif mode == '3':
                self.new_post()
            elif mode == '5':
                print("Exiting program")
                time.sleep(1)
                break  

    # Adding a user to the .csv
    def add_user(self):
        name = input('Enter name:\n')
        email_address = input('Enter email address: \n')
        password = input('Enter password: \n')
        self.users.append(User(name, email_address, password))
        with open (path_users, 'a') as csvfile:
            csv_object = writer(csvfile)
            for user in self.users:
                csv_object.writerow([user.name, user.email_address, user.password])

    # Displaying all users
    def show_users(self):
        with open (path_users) as f:
            reader = csv.reader(f)
            for row in reader:
                print(row[0],row[1])
    
    # User posting 
    def new_post(self):
        user_post_list = []
        users_post = input('Your post:\n')
        user_post_list.append(users_post)
        with open (path_posts, 'a') as csvfile:
            csv_object = writer(csvfile)
            csv_object.writerow(user_post_list)
        
        