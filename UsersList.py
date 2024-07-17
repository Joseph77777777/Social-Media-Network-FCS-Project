from Structure import User

class Users:
    def __init__(self):
        self.list_of_users={}
    
    def add_new_user(self, userId, fullName, posts=None):
        #Adding a new user to the list.
        #userId: ID for the new user
        #fullName: Name of the new user
        #posts: List of posts made by the user

        if self.userId not in self.list_of_users:
            new_user=User(userId, fullName, posts)
            self.list_of_users[userId]=new_user
        else:
            print("The user "+fullName+"with ID "+userId+" already exist")

    