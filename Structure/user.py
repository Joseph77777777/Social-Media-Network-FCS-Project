class User:
    def __init__(self, userId, fullName, posts=None,interests=None):
        """  
        Initializing a new user.
        parameters:
                userId: ID for the user
                fullName: Name of the user
                posts: posts made by the user 
                interests : Interests of the user
         """
        self.userId = userId
        self.fullName = fullName
        self.friendsList = []
        self.posts = []
        self.interests=[]
        
    

    def add_friend(self,friend_Id,friend_Name,weight):
        """
         Adding friend to the friend list
         parameters:
                    friend_Id: ID for the new friend
                    friend_Name: Name of the new friend
                    weight : Weight of the relationship.
        """
        friend_exist=False
        #Traversing the list to check if the friend  exist in the list
        for  f  in self.friendsList:
            if f[0]==friend_Id :
                friend_exist=True
                break
        #If not exist it will be added to the list
        if  friend_exist==False:
            self.friendsList.append((friend_Id,friend_Name,weight))
            
        else:
            print("The friend with ID: "+str(friend_Id)+" is already added")

    def remove_friend(self,friend_Id):
        """
        removing a friend from the friends list
            parameter:
                friend_Id: friends Id to be removed
        """
        friend_exist = False
        #Checking if the friend exist in the list of friend
        for f in self.friendsList:
            if f[0] == friend_Id:
                friend_exist = True
                self.friendsList.remove(f)
                break

        if  friend_exist==False:
            print("The friend with ID: " + str(friend_Id) + " doesn't exist")
            
    def post_Update(self,new_post):
        """adding new post to the users post
              parameter:
                    new_post:content of the new post
        """
        self.posts.append(new_post)
    
    def interests_Update(self,new_interest):
        """adding new interest to the users interests
                parameter:
                   new_interest: content of the new interest         
        """
        self.interests.append(new_interest)

    def __str__(self) :
        """
        Return a string representing  the user, including their ID, name, posts, interests, and friends.
        """
        friendsList=" "
        for friend_Id,friend_Name in self.friendsList:
            friendsList+="ID: "+str(friend_Id)+"/"+friend_Name+","
        return "User(" + str(self.userId) + ", " + self.fullName +","+str(self.posts) + ","+str(self.interests) +", Friends: [" + friendsList + "])"
    



            




    
        