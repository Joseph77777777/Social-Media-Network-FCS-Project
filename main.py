from Social_Network.UsersManagement import Users

def main():
    U1=Users()
    print(Users.displayMenu())
    choice=int(input("Please enter your choice: "))
    while(choice!=14):
        if(choice==1):
           user_id=int(input("Enter user ID: "))
           full_name=input("Enter user full name: ")
           U1.add_new_user(user_id,full_name)
           #print(U1)
           print(Users.displayMenu())
           choice=int(input("Please enter your choice: "))

        elif(choice==2):
           user_id=int(input("Enter user ID to be removed: "))
           U1.remove_user(user_id)
           print(Users.displayMenu())
           choice=int(input("Please enter your choice: "))

        elif(choice==3):
           U1.Network_Statistics()

        elif(choice==4):
           logged_in_user_id=int(input("Enter your user ID: "))
           friend_Id=int(input("Enter User ID to follow: "))
           logged_in_user = U1.search_byId(logged_in_user_id)
           U1.follow_User(logged_in_user, friend_Id)
           #print(U1)
           print(Users.displayMenu())
           choice=int(input("Please enter your choice: "))

        elif(choice==5):
           logged_in_user_id=int(input("Enter your user ID: "))
           friend_Id=int(input("Enter User ID to Unfollow: "))
           logged_in_user = U1.search_byId(logged_in_user_id)
           U1.unfollow_User(logged_in_user, friend_Id)
           #print(U1)
           print(Users.displayMenu())
           choice=int(input("Please enter your choice: "))
           
        elif(choice==6):
           logged_in_user_id=int(input("Enter your user ID: "))
           adding_post=input("Enter a post: ")
           logged_in_user=U1.search_byId(logged_in_user_id)
           U1.update_post_forUser(logged_in_user,adding_post)
           #print(U1)
           print(Users.displayMenu())
           choice=int(input("Please enter your choice: "))

        elif(choice==7):
           logged_in_user_id=int(input("Enter your user ID: "))
           adding_Interest=input("Enter an interest: ")
           logged_in_user=U1.search_byId(logged_in_user_id)
           U1.update_interests_forUser(logged_in_user,adding_Interest)
           #print(U1)
           print(Users.displayMenu())
           choice=int(input("Please enter your choice: "))

        elif(choice==8):
           sorted_users = U1.users_sorted_byName()
           for userId, name in sorted_users.items():
            print("User ID: "+str(userId)+ ", " +"Name:"+name.fullName)
           print(Users.displayMenu())
           choice=int(input("Please enter your choice: "))

        elif(choice==9):
            Name = input("Enter user's name: ")
            U=U1.search_byName(Name)
            print(U)
            print(Users.displayMenu())
            choice=int(input("Please enter your choice: "))
           
        elif(choice==10):
           ID=int(input("Enter user's ID: "))
           U=U1.search_byId(ID)
           print(U)
           print(Users.displayMenu())
           choice=int(input("Please enter your choice: "))

        elif(choice==11):
           Start_userId=int(input("Enter a start user ID: "))
           bfs=U1.BFS(Start_userId)
           print("The BFS traversal: "+ str(bfs))
           
        #elif(choice==12):
           
        elif(choice==13):
           U1.Graph_Visualization() 
           print(Users.displayMenu())
           choice=int(input("Please enter your choice: "))  
        else:
            print("This is invalid input.Try Again!")
            print(Users.displayMenu())
            choice=int(input("Please enter your choice: "))
    
    print("Thank you for using our Social Network System")
main()
