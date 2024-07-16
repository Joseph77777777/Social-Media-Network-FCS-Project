class User:
    def __init__(self, userId, fullName, posts=None):
        # Initializing a new user.
        # parameter userId: ID for the user
        # parameter fullName: Name of the user
        # parameter posts:  posts made by the user 
        
        self.userId = userId
        self.fullName = fullName
        self.friendsList = []
        self.posts = posts
        self.size_friendsList=0

    def add_friend(self,friend_Id,friend_Name):
        # adding friend to the friend list
        # parameter friend_Id: ID for the new friend
        # parameter friend_Name: Name of the new friend

        friend_exist=False
        for  f  in self.friendsList:#Traversing the list to check if the friend index exist in the list
            if f[0]==friend_Id :
                friend_exist=True
                break
        
        if  friend_exist==False:#if not exist it will be added to the list
            self.friendsList.append(friend_Id,friend_Name)
        else:
            print("The friend with ID"+str(friend_Id)+"and name "+friend_Name+"is already added")
            
       



    
        