from Structure import User

class Users:
    def __init__(self):
        self.list_of_users={}#Creating a dictionary to store users
        self.size=0
    
    def add_new_user(self, userId, fullName, posts=None):
        #Adding a new user to the list of users.
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
        #Removing a user from the list of users
        if userId  in self.list_of_users:
            del self.list_of_users[userId]
        else:
            print("The user with ID: "+userId+" doesnt exist")

    def search_byId(self,userId):
        #Searching a user by ID using linear search algorithm

        for u in self.list_of_users.values():#iterating through all the values in the list_of_users dictionary
            if u.userId==userId:
                return u
            else:
                print("The user with ID "+userId+" is not found")
            
    def search_byName(self,fullName):
        #Searching a user by name using linear search algorithm

        for u in self.list_of_users.values():#iterating through all the values in the list_of_users dictionary
            if u.fullName==fullName:
                return u
            else:
                print("The user with name "+fullName+" is not found")

    def __str__(self):
        #Displaying the list of users
        users_list=""
        for userId,name in self.list_of_users.items():
            users_list+=str(userId)+", "+name.fullName +"\n"
        return users_list
    
    def selectionSort(self,lst):
        #Sorting a list using selection sort algorithm
        for i in range(len(lst)-1):
            min=i
            for j in range (i+1,len(lst)):
                if lst[j]<lst[min]:
                    min=j
            lst[i],lst[min]=lst[min],lst[i]
        return lst
    
    def users_sorted_byName(self):
        lst_users = list(self.list_of_users.values())  # Convert dictionary values to a list
        sorted_users = self.selectionSort(lst_users)  # Sort the list using selection sort
        #Convert sorted list to dictionary
        dict_sorted = {}
        for user in sorted_users:
            dict_sorted[user.userId] = user
        return dict_sorted



  

    