from Structure import User

class Users:
    def __init__(self):
        self.list_of_users={}
        self.size=0
    
    def add_new_user(self, userId, fullName, posts=None):
        #Adding a new user to the list.
        #userId: ID for the new user
        #fullName: Name of the new user
        #posts: List of posts made by the user

        if userId not in self.list_of_users:
            new_user=User(userId, fullName, posts)
            self.list_of_users[userId]=new_user
            self.size+=1
        else:
            print("The user "+fullName+"with ID "+userId+" already exist")
    
    def remove_user(self,userId):
        #Removing a user from the list
        if userId  in self.list_of_users:
            del self.list_of_users[userId]
        else:
            print("The user with ID: "+userId+" doesnt exist")
    
    
  

    