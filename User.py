import os
import csv

class User():

    def post(self):
        drivers_license = input(f"Enter drivers license:\t")
        title = input(f"Enter title:\t")
        post = input(f"Enter post:\t")
        self.posts.append({
            'drivers_license':drivers_license,
            'title':title,
            'post':post
        })
    
    def delete_post(self):
        drivers_license = input(f'Enter your drivers license:\t')
        delete_post = input(f'Enter title of post to delete:\t')
        
        for x in self.posts:
            if x['drivers_license'] == drivers_license and x['title'] == delete_post:
                self.posts.remove(x)


    def add_user(self):
        name = input('Enter name:\t')
        email = input('Enter email\t')
        drivers_license = input('Enter Drivers License:\t')
        self.users.append({
            'name':name,
            'email':email,
            'drivers_license':drivers_license
        })

    @classmethod
    def objects(cls,save_type):
        data = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, f"data/{save_type}.csv")
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
        return data

    def save(self,save_type,headers_list,data):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, f"data/{save_type}.csv")

        final = []
        for x in data:
            final.append(list(x.values()))

        with open(path, 'w') as csvfile:
            data_csv = csv.writer(csvfile, delimiter=',')
            data_csv.writerow(headers_list)
            data_csv.writerows(final)

