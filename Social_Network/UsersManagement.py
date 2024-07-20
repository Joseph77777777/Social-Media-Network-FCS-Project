import networkx 
import sys
import os

# Add the top-level directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Structure.user import User
class Users:
    def __init__(self):
        self.list_of_users={}#Creating a dictionary to store users
        
    
    def add_new_user(self, userId, fullName, posts=None):
        #Adding a new user to the list of users.
        #userId: ID for the new user
        #fullName: Name of the new user
        #posts: List of posts made by the user

        if userId not in self.list_of_users:
            new_user=User(userId, fullName, posts)
            self.list_of_users[userId]=new_user
            
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
                if lst[j].fullName<lst[min].fullName:
                    min=j
            if min!= i:
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

    def follow_User(self,logged_in_user,userId):
        #Adding a friend to user and checking if this friend exist in the list of users
        #userId: ID for the new user I want to become friend 
        #logged_in_user : The main user
        if logged_in_user.userId==userId:
            print("You cant add your self")
    
        elif userId not in self.list_of_users:
            print("The user with ID "+str(userId)+" doesnt exist")
        else:
            user_name=self.list_of_users[userId].fullName
            logged_in_user.add_friend(userId,user_name)

    def unfollow_User(self,logged_in_user,userId):
        #removing a friend from user and checking if this friend exist in the list of users
        #userId: ID for the new user I want to remove as a friend 
        #logged_in_user : The main user

        if userId not in self.list_of_users:
            print("The user with ID "+str(userId)+" doesnt exist")
        else:
            logged_in_user.remove_friend(userId)

    def update_post_forUser(self,logged_in_user,post):
        if logged_in_user.userId not in self.list_of_users:
            print("User doesnt exist")
        else:
            logged_in_user.post_Update(post)

    
    def update_intersets_forUser(self,logged_in_user,interest):
        if logged_in_user.userId not in self.list_of_users:
            print("User doesnt exist")
        else:
            logged_in_user.interests_Update(interest)
    
    def Network_Statistics(self):
        #Average number of friends per user
        number_of_users = len(self.list_of_users)
        total_numbers_friends=0
        if number_of_users>0 :
          for user in self.list_of_users.values():
             total_numbers_friends += len(user.friendsList)
        else:
            return

        Average = total_numbers_friends / number_of_users 

        print("The average number of friends per user is : "+str(Average))
    

          



    

U1=Users()
U1.add_new_user(1,"Joe",[])
U1.add_new_user(2,"MJ",[])
U1.add_new_user(3,"Elie",[])
U1.add_new_user(4,"Michelle",[])

print(U1)
# print(U1.search_byId(1))
J=U1.search_byId(1)
#U1.follow_User(J,1)
U1.follow_User(J,2)
U1.follow_User(J,3)

U1.Network_Statistics()


#print(J)



# sorted_users = U1.users_sorted_byName()
# for userId, user in sorted_users.items():
#     print("User ID: "+str(userId)+ ", " +"Name:"+user.fullName)
# U1.remove_friend_fromUser(J,3)
# U1.remove_friend_fromUser(J,2)
# print(J)
# U1.update_post_forUser(J,"my first post")
# print(J)


# # J.add_friend(2,"MjA")
# # print(J)
# # J.add_friend(3,"Michelle")
# # print(J)

  

    