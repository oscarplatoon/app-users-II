from User import User

class Interface():
    def __init__(self,name):
        self.name = name
        self.users = User.objects('users')
        self.posts = User.objects('post')


    def run(self):
        while True:
            response = input(f'\n\nWhat would you like to do?\n1. Add User\n2. Create Post\n3. Show Users\n4. Show Posts <by user>\n5. Delete Post\n6. Quit\n\n')

            if response == '1':
                User.add_user(self)
                User.save(self,'users',['name','email','drivers_license'],self.users)
            
            elif response =='2':
                User.post(self)
                User.save(self,'post',['drivers_license','title','post'],self.posts)
            
            elif response =='3':
                    print(self.users)

            elif response =='4':
                print(self.posts)
                    
            elif response =='5':
                User.delete_post(self) 
                User.save(self,'post',['drivers_license','title','post'],self.posts)               

            elif response =='6':
                quit()
