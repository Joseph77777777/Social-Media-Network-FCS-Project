import networkx as nx
import matplotlib.pyplot as plt
import sys
import os

# Add the top-level directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Structure.user import User
class Users:
    def __init__(self):
        self.list_of_users={}#Creating a dictionary to store users
        self.Network=nx.DiGraph()#Creating a directed graph to represent the Network
        
    
    def add_new_user(self, userId, fullName, posts=None,interests=None):
        #Adding a new user to the list of users.
        #userId: ID for the new user
        #fullName: Name of the new user
        #posts: List of posts made by the user

        if userId not in self.list_of_users:
            new_user=User(userId, fullName, posts,interests)
            self.list_of_users[userId]=new_user
            self.Network.add_node(userId)#Adding a node or vertex(user) to the graph
            
        else:
            print("The user "+fullName+" with ID "+str(userId)+" already exist")
    
    def remove_user(self,userId):
        #Removing a user from the list of users
        if userId  in self.list_of_users:
            del self.list_of_users[userId]
            self.Network.remove_node(userId)#Removing a node or vertex(user) from the Graph
        else:
            print("The user with ID "+str(userId)+" doesnt exist")

    def search_byId(self,userId):
        #Searching a user by ID using linear search algorithm

        for u in self.list_of_users.values():#iterating through all the values in the list_of_users dictionary
            if u.userId==userId:
                print("The user with ID "+str(userId)+" is found")
                return u
                  
        print("The user with ID "+str(userId)+" is not found")
            
    def search_byName(self,fullName):
        #Searching a user by name using linear search algorithm

        for u in self.list_of_users.values():#iterating through all the values in the list_of_users dictionary
            if u.fullName==fullName:
                print("The user with name "+fullName+" is found")
                return u
            
        print("The user with name "+fullName+" is not found")

    def __str__(self):
        #Displaying the list of users
        users_list=""
        for userId,name in self.list_of_users.items():
            users_list+="User ID: "+str(userId)+",Name: "+name.fullName +",Posts: "+str(name.posts) + ",Interests: "+str(name.interests)+"\n"
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
            self.Network.add_edge(logged_in_user.userId,userId) #Adding edge in the graph
            

    def unfollow_User(self,logged_in_user,userId):
        #removing a friend from user and checking if this friend exist in the list of users
        #userId: ID for the new user I want to remove as a friend 
        #logged_in_user : The main user

        if userId not in self.list_of_users:
            print("The user with ID "+str(userId)+" doesnt exist")
        else:
            logged_in_user.remove_friend(userId)
            self.Network.remove_edge(logged_in_user.userId,userId)#Removing edge from the graph

    def update_post_forUser(self,logged_in_user,post):
        if logged_in_user.userId not in self.list_of_users:
            print("User doesnt exist")
        else:
            logged_in_user.post_Update(post)

    
    def update_interests_forUser(self,logged_in_user,interest):
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

        #Network density
        max_number_edges=number_of_users*(number_of_users - 1)#number_of_users are the vertices
        #In a directed graph the maximum number of edges is V*(V-1)
        if max_number_edges>0:
          density=self.Network.number_of_edges() / max_number_edges
        else:
            return
        print("The Network density is: "+str(density))

    
    def BFS(self, start):
        #Explores the social network level by level. 
        # It starts from a given user (root node) and visits all their direct friends first, 
        # then their friends' friends, and so on. 
        
        if start not in self.list_of_users:
            print("The user with ID "+str(start.userId)+ "doesnt exist")

        else:
         visited = set()
         queue = [start]
         bfs_traversal = []

        while queue:
            userId = queue.pop(0)
            if userId not in visited:
                visited.add(userId)
                bfs_traversal.append(userId)
                for friend in self.friendsList[userId]:
                    if friend not in visited:
                        queue.append(friend)
        
        print("BFS Traversal starting from user ID",+ str(start)+ "," + str(bfs_traversal))
        return bfs_traversal
    
    def DFS(self, start):
        # Explores the network by going as deep as possible down one path before backtracking.
        # It starts from a given user and explores each branch of friends fully before moving to the next branch. 
        
        if start not in self.list_of_users:
            print("The user with ID "+str(start.userId)+ "doesnt exist")
            return
        else:
         visited = set()
         stack = [start]
         dfs_traversal = []

        while stack:
            userId = stack.pop()
            if userId not in visited:
                visited.add(userId)
                dfs_traversal.append(userId)
                for friend in self.list_of_users[userId].friendsList:
                    if friend not in visited:
                        stack.append(friend)

        print("BFS Traversal starting from user ID",+ str(start)+ "," + str(dfs_traversal))
        return dfs_traversal

    def Graph_Visualization(self):
        G= nx.DiGraph()#creating a directed graph G using  NetworkX library.

        for user in self.list_of_users.values():#iterating over each user
            G.add_node(user.userId, label=user.fullName)#add node ,each node represent the user
            for friendId, _ in user.friendsList:#For each user, iterate over their friendsList.
                 G.add_edge(user.userId, friendId)#add an edge from the user to each friend.

        pos = nx.spring_layout(G)
        labels = nx.get_node_attributes(G, 'label')

        #Drawing and configuring the Graph
        plt.figure(figsize=(20, 20))
        nx.draw(G, pos, labels=labels, with_labels=True, node_color='Red', node_size=2000, font_size=15, font_color='black', font_weight='bold', edge_color='gray')
        plt.title('Social Network Media')
        plt.show()

         
    def displayMenu():
        return (
        "The menu is :\n"
        "1 - Add User\n"
        "2 - Delete User\n"
        "3 - Average friends and Network density\n"
        "4 - Follow friend\n"
        "5 - Unfollow friend\n"
        "6 - Add new post\n"
        "7 - Add new Interest\n"
        "8 - Show all my friends by name\n"
        "9- Search for friend by name\n"
        "10 - Search for friend by ID\n"
        "11 - Suggest User based on my interest\n"
        "12 - Suggest friends based on mutual interests\n"
        "13 - Print out my Social Network")
    

    

          



    

# U1=Users()
# U1.add_new_user(1,"Joe",[])
# U1.add_new_user(2,"MJ",[])
# U1.add_new_user(3,"Elie",[])
# U1.add_new_user(4,"Michelle",[])

# print(U1)
# print(U1.search_byId(1))
# print()
# J=U1.search_byId(1)
# print(U1.search_byId(3))
# E=U1.search_byId(3)
# # U1.displayMenu()


# #U1.follow_User(J,1)
# U1.follow_User(J,2)
# U1.follow_User(J,3)
# U1.follow_User(J,4)
# U1.follow_User(E,1)

# U1.Network_Statistics()
# U1.Graph_Visualization()



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

  

    