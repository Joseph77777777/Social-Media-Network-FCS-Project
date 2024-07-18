class User:
    def __init__(self, userId, fullName, posts=None):
        # Initializing a new user.
        # parameter userId: ID for the user
        # parameter fullName: Name of the user
        # parameter posts:  posts made by the user 
        
        self.userId = userId
        self.fullName = fullName
        self.friendsList = []
        self.posts = []
        #self.size_friendsList=0

    def add_friend(self,friend_Id,friend_Name):
        # adding friend to the friend list
        # parameter friend_Id: ID for the new friend
        # parameter friend_Name: Name of the new friend

        friend_exist=False
        for  f  in self.friendsList:#Traversing the list to check if the friend  exist in the list
            if f[0]==friend_Id :
                friend_exist=True
                break
        
        if  friend_exist==False:#if not exist it will be added to the list
            self.friendsList.append((friend_Id,friend_Name))
            #self.size_friendsList+=1
        else:
            print("The friend with ID: "+str(friend_Id)+" is already added")

    def remove_friend(self,friend_Id):
        # removing friend from the friend list
        # parameter friend_Id: ID for the existing friend
        # parameter friend_Name: Name of the existing friend

        friend_exist = False
        for f in self.friendsList:
            if f[0] == friend_Id:
                friend_exist = True
                self.friendsList.remove(f)
                #self.size_friendsList -= 1
                break

        if  friend_exist==False:
            print("The friend with ID: " + str(friend_Id) + " doesn't exist")
            
    def post_Update(self,new_post):
        # adding new post to the users post
        self.posts.append(new_post)

    def __str__(self) :
        friendsList=" "
        for friend_Id,friend_Name in self.friendsList:
            friendsList+="ID: "+str(friend_Id)+"/"+friend_Name+","
        return "User(" + str(self.userId) + ", " + self.fullName +","+str(self.posts) + ", Friends: [" + friendsList + "])"
    



            




    
        