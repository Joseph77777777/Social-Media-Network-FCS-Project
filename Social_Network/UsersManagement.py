import networkx as nx
import matplotlib.pyplot as plt
import sys
import os
import math

# Add the top-level directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Structure.user import User
class Users:
    """
    A class to represent a social network of users.

    list_of_users : A dictionary to store user objects with userId as the key.
    Network : nx.DiGraph a directed graph to represent the social network.
    """
    def __init__(self):
        #Creating a dictionary to store users
        self.list_of_users={}

        #Creating a directed graph to represent the Network
        self.Network=nx.DiGraph()
        
        

    def check_user_exist(self,userId, fullName):
        """
         Check if a user with the given userId and fullName exists in the list_of_users.
         In oreder to log in
         Parameters:
              userId:unique ID of the user
              fullName: full name of the user
        """
        if userId not in self.list_of_users:#Checking if the userId exists in the list of users 
            print("User doesnt exist")
        elif(self.search_byId(userId).fullName.lower()==fullName.lower()):# Check if the fullName matches.
            return self.search_byId(userId)
        else:
         print("User doesnt exist")
            

    def add_new_user(self, userId, fullName, posts=None,interests=None):
        """
        Adding a new user to the list of users.
        Parameters:
                  userId: ID for the new user
                  fullName: Name of the new user
                  posts: List of posts made by the user
                  interests: List of posts made by the user
        """
         # Checking if the userId is in the list of users
        if userId not in self.list_of_users:
            #Creating a new user object
            new_user=User(userId, fullName, posts,interests)
            #Adding the new user to the list of users
            self.list_of_users[userId]=new_user
            #Adding a node or vertex(user) to the graph
            self.Network.add_node(userId)
        # print a message if the userId already exists
        else:
            print("The user "+fullName+" with ID "+str(userId)+" already exist")
    
    def remove_user(self,userId):
        """
        Removing an existing user from the list of users.
        Parameters:
                  userId: ID of the user
                  
        """
        # Checking if the userId is in the list of users
        if userId  in self.list_of_users:
            #Deleting the user from the list of users
            del self.list_of_users[userId]
            #Removing a node or vertex(user) from the Graph
            self.Network.remove_node(userId)

        # print a message if the userId doesnt exist
        else:
            print("The user with ID "+str(userId)+" doesnt exist")

    def search_byId(self,userId):
        """
        Search for a user by their ID using a binary search algorithm.

        Parameters: 
                  userId : The ID of the user to search for.
        """
        #Starting indices
        low=0
        high=len(self.list_of_users)
        while (low<=high):
            #Caluculating middle value 
            mid=(low+high)/2
            mid=(math.ceil(mid))
            if(userId==self.list_of_users[mid].userId):
                #Returning the userId if founded
                return self.list_of_users[mid]
            elif(userId>self.list_of_users[mid].userId):
                low=mid+1
            else:
                high=mid-1
        #print a message if the userId is not found
        print("The user with ID "+str(userId)+" is not found")
        
        
            
    def search_byName(self,fullName):
        """
        Search for a user by their name using a linear search algorithm.

        Parameters: 
                  fullName : The Name of the user to search for.
        """
        #Iterating through all the values in the list of users 
        for u in self.list_of_users.values():
            # Check if the names matches.
            if u.fullName.lower()==fullName.lower():
                print("The user with name "+fullName+" is found")
                return u
        #print a message if the name is not found  
        print("The user with name "+fullName+" is not found")

    def __str__(self):
        """
         Display the list of users with their details.
    
         Returns:
         str: A string representation of the users list.
        """
        users_list=""
        for userId,name in self.list_of_users.items():
            users_list+="User ID: "+str(userId)+",Name: "+name.fullName +",Posts: "+str(name.posts) + ",Interests: "+str(name.interests)+"\n"
        return users_list
    
    def selectionSort(self,lst):
        """
       Sorts a list of User objects using the selection sort algorithm.
    
        Parameters:
                  lst : The list of User objects to be sorted.
        """
        for i in range(len(lst)-1):
            #Assuming that the first element is the minimum
            min=i
            for j in range (i+1,len(lst)):
                # Finding the smallest value in remaining list
                if lst[j].fullName<lst[min].fullName:
                    #Updating the minimum element
                    min=j
            if min!= i:
             # Swaping the found minimum element with the first element
             lst[i],lst[min]=lst[min],lst[i]
        return lst
    
    def users_sorted_byName(self):
        """
        Sorts the users by their full names and returns them as a dictionary.
        Using the function selectionSort
        """
        # Converting dictionary values to a list
        lst_users = list(self.list_of_users.values()) 
        # Sorting the list using selection sort
        sorted_users = self.selectionSort(lst_users) 
        #Converting sorted list into dictionary
        dict_sorted = {}
        for user in sorted_users:
            dict_sorted[user.userId] = user
        return dict_sorted
    
        
    def new_friend_suggestion(self, logged_in_user):
        """
        Suggests new friends for the logged-in user based on common interests.
        
        Parameters:
        logged_in_user : The user for whom to suggest new friends.
        
        It will return a list of suggested Users
        """
        # Check if the logged-in user has any interests
        if not logged_in_user.interests:
            print('Logged in user has no interests')
            return []
        # Convert the logged-in user's interests to a set for easy comparison
        interests_set = set(logged_in_user.interests)
        # Priority queue to store users with common interests
        priority_queue = []
        # List to store the final suggestions
        out = []
         # Iterating over each user in the list of users
        for user_id in self.list_of_users:
            # Checking if the user is not a friend of the logged-in user and is not the logged-in user
            if user_id not in logged_in_user.friendsList and user_id !=logged_in_user.userId:
                # Get the user object by ID
                user_obj = self.search_byId(user_id)
                
                # Check if the user exists and has interests
                if user_obj and user_obj.interests:
                    # Convert the user's interests to a set
                    user_interests_set = set(user_obj.interests)
                    # Find common interests
                    common_interest = interests_set & user_interests_set
                    # If there are common interests, add the user to the priority queue
                    if common_interest:
                        priority_queue.append((len(common_interest), user_obj))
                        
                else:
                    print(f'User {user_id} has no interests or not found')
            # else:
            #     print(f'User {user_id} is already a friend')
        
        def custom_key(item):
            return item[0]
         # Sort the priority queue based on the number of common interests (in descending order)
        priority_queue = sorted(priority_queue, key=custom_key, reverse=True)
       
        # Get the top suggestions (for example, the top 4)
        max_val = min(4, len(priority_queue))
        
        # Add the top suggestions to the output list
        for i in range(max_val):
            out.append(priority_queue.pop(0))
        
        return out


    def follow_User(self,logged_in_user,userId,weight):
        """
        Adding/following a new friend to the logged-in user's friend list and updates the social network graph.
        
        Parameters:
                  logged_in_user : The user who wants to add a new friend.
                  userId : The ID of the user to be added as a friend.
                  weight : The weight or strength of the relationship .
        """
        # Checking if the logged-in user is adding himself as a friend
        if logged_in_user.userId==userId:
            print("You cant add your self")
        #Checking if the user with the given ID exist in the list of users
        elif userId not in self.list_of_users:
            print("The user with ID "+str(userId)+" doesnt exist")

        else:
            # Finding the name of the user to be added as a friend
            user_name=self.list_of_users[userId].fullName
            #Adding the user to the logged in user's friendsList
            logged_in_user.add_friend(userId,user_name,weight)
            #Adding edge  in the graph and edge weight
            self.Network.add_edge(logged_in_user.userId,userId,weight=weight) 
            

    def unfollow_User(self,logged_in_user,userId):
        """
        Deleting/Unfollowing a friend from the logged-in user's friend list and updates the social network graph.
        
        Parameters:
                  logged_in_user : The user who wants to remove a friend.
                  userId : The ID of the user to be removed
                  
        """
        
        #Checking if the user with the given ID exist in the list of users
        if userId not in self.list_of_users:
            print("The user with ID "+str(userId)+" doesnt exist")
        else:
            #Removing the user from the logged in user's friendsList
            logged_in_user.remove_friend(userId)
            #Removing edge from the graph
            self.Network.remove_edge(logged_in_user.userId,userId)

    def update_post_forUser(self,logged_in_user,post):
        """
            Updates the posts of a logged-in user.

            Parameters:
                      logged_in_user : The user whose post needs to be updated.
                      post : The new post to be added. 
        """
        #Checking if the logged in user exist in the list of users
        if logged_in_user.userId not in self.list_of_users:
            print("User doesnt exist")
        else:
            #Adding/Updating post of the logged in user
            logged_in_user.post_Update(post)

    
    def update_interests_forUser(self,logged_in_user,interest):
        """
            Updates the intersets of a logged-in user.

            Parameters:
                      logged_in_user : The user whose interest needs to be updated.
                      post : The new interest to be added. 
        """
        #Checking if the logged in user exist in the list of users
        if logged_in_user.userId not in self.list_of_users:
            print("User doesnt exist")
        else:
            #Adding/Updating post of the logged in user
            logged_in_user.interests_Update(interest)
    
    def Network_Statistics(self):
        """
            Calculates and displays network statistics:
                #A-The average number of friends per user.
                #B-The density of the network.
        """
        #A
        #Calculate the number of users using length of list of users
        number_of_users = len(self.list_of_users)
        total_numbers_friends=0
        # Calculate the total number of friends for all users
        if number_of_users>0 :
          for user in self.list_of_users.values():
             total_numbers_friends += len(user.friendsList)
        else:
            return
        #Calculate the average number of friends per user
        Average = total_numbers_friends / number_of_users 

        print("The average number of friends per user is : "+str(Average))
        #B
        #number_of_users are the vertices
        #In a directed graph the maximum number of edges is V*(V-1)
        max_number_edges=number_of_users*(number_of_users - 1)

        #Calculate the density network
        if max_number_edges>0:
          density=self.Network.number_of_edges() / max_number_edges
        else:
            return
        print("The Network density is: "+str(density))

    
    def BFS(self, start):
        """
          Explores the social network level by level.# It starts from a given user (root node) and visits all their direct follower friends first,  
          then their friends' friends, and so on. 

          It will return a list of users ID representing the BFS traversal

          Parameters:
                start : The ID of the starting user.
           
        """
        # Checking if the start user ID exists in the list of users
        if start not in self.list_of_users:
            print("The user with ID "+str(start)+ "doesnt exist")

        #Creating an empty set to track the visited users
        visited = set()
        #Creating a queue with the starting user ID
        queue = [start]
        #Creating a list representing the BFS traversal
        bfs_traversal = []

        while queue:
            #Remove the first user Id from the queue
            userId = queue.pop(0)
            if userId not in visited:
                #Adding the user Id to the visited set
                visited.add(userId)
                #Adding the user Id to the BFS traversal list
                bfs_traversal.append(userId)
                #restore the user object 
                user=self.list_of_users[userId]
                # Iterating through the friends list of the user
                for friend,_ in user.friendsList:
                    #If the friend is not in the visited set
                    if friend not in visited:
                        #Add the friend to the queue 
                        queue.append(friend)
        
        return bfs_traversal
    
    def DFS(self, start):
        """
            Explores the network by going as deep as possible down one path before backtracking.
            It starts from a given user and explores each branch of friends fully before moving to the next branch. 
        """
        # Checking if the start user ID exists in the list of users
        if start not in self.list_of_users:
            print("The user with ID "+str(start)+ "doesnt exist")
            
        #Creating an empty set to track the visited users
        visited = set()
        #Creating a stack with the starting user ID
        stack = [start]
        #Creating a list representing the DFS traversal
        dfs_traversal = []

        while stack:
            #Remove the first user Id from the stack
            userId = stack.pop()
            if userId not in visited:
                #Adding the user Id to the visited set
                visited.add(userId)
                #Adding the user Id to the DFS traversal list
                dfs_traversal.append(userId)
                #restore the user object 
                user=self.list_of_users[userId]
                # Iterating through the friends list of the user
                for friend, _ in user.friendsList:
                    #If the friend is not in the visited set
                    if friend not in visited:
                        #Add the friend to the stack
                        stack.append(friend)

        return dfs_traversal
    
    def shortest_path(self,start,target):
        """
                Finds the shortest path between two users using Dijkstra's algorithm.

                Parameters:
                            start : The ID of the starting user.
                            target : The ID of the target user.
         """
     
        if start not in self.list_of_users and target not in self.list_of_users:
            print("The start and target ID doesnt exist")
        
        distance = {}
        previous_nodes = {}
        for user in self.list_of_users:
            distance[user]= float('inf')
            previous_nodes[user] = None
        distance[start] = 0

        # Creating a list as a priority queue
        priority_queue = [(0, start)]
        visited = set()

        while priority_queue:
            # Find user with the smallest distance
            priority_queue.sort()
            current_distance, current_user_id = priority_queue.pop(0)

            if current_user_id in visited:
                continue

            visited.add(current_user_id)

            if current_user_id == target:
                # Construct the path
                path = []
                while current_user_id is not None:
                    path.append(current_user_id)
                    current_user_id = previous_nodes[current_user_id]
                path.reverse()
                print("Shortest path:", path)
                return path
            
              # Update distances for neighboring nodes
            current_user = self.list_of_users[current_user_id]
          
            for friend_id,_, weight in current_user.friendsList:
                if friend_id not in visited:
                    
                    new_distance = current_distance + weight
                    if new_distance < distance[friend_id]:
                        distance[friend_id] = new_distance
                        previous_nodes[friend_id] = current_user_id
                        priority_queue.append((new_distance, friend_id))

        print("There is no path between the users")
 
    def Graph_Visualization(self):
        """
                Visualizes the social network graph using NetworkX and Matplotlib.
         """
        #creating a directed graph G using  NetworkX library.
        G= nx.DiGraph()

        #Iterating over each user
        for user in self.list_of_users.values():
            #add node ,each node represent the user
            G.add_node(user.userId, label=user.fullName)
            #For each user, iterate over their friendsList.
            for friendId, _, _ in user.friendsList:
                 #add an edge from the user to each friend.
                 G.add_edge(user.userId, friendId)

        pos = nx.spring_layout(G)
        labels = nx.get_node_attributes(G, 'label')

        #Drawing and configuring the Graph
        plt.figure(figsize=(20, 20))
        nx.draw(G, pos, labels=labels, with_labels=True, node_color='Red', node_size=2000, font_size=15, font_color='black', font_weight='bold', edge_color='gray')
        plt.title('Social Network Media')
        plt.show()

         
    def displayMenu(isLoggedIn):
        """
             Displays the menu options based on the user's login status.
    
             Parameters:
                isLoggedIn : Indicates if  the user is logged in or not.
    
         """
        ifNotLoggedIn=("The menu is :\n"
        "0 - Log in\n"
        "1 - Add User\n"
        "2 - Delete User\n")
        ifLoggedIn=("3 - Average friends and Network density\n"
        "4 - Follow friend\n"
        "5 - Unfollow friend\n"
        "6 - Add new post\n"
        "7 - Add new Interest\n"
        "8 - Show all users by name\n"
        "9- Search for user by name\n"
        "10 - Search for user by ID\n"
        "11 - BFS Traversal\n"
        "12 - DFS Traversal\n"
        "13 - Find shortest path between Two users\n"
        "14 - Suggest top 4 new friends based on common interests\n"
        "15 - Print out my Social Network\n")
        toExit=("16- Exit")
        
        return (ifNotLoggedIn+ifLoggedIn+toExit) if isLoggedIn else ifNotLoggedIn+toExit
    

    




  

    