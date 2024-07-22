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
           U1.remove_user()
        elif(choice==3):
           U1.Network_Statistics()
        elif(choice==4):
           U1.follow_User()
        elif(choice==5):
           U1.unfollow_User()
        elif(choice==6):
           U1.update_post_forUser()
        elif(choice==7):
           U1.update_intersets_forUser()
        elif(choice==8):
           U1.users_sorted_byName()
        elif(choice==9):
           U1.search_byName()
        elif(choice==10):
           U1.search_byId()
        elif(choice==11):
           U1.DFS()
        elif(choice==12):
           U1.BFS()
        elif(choice==13):
           U1.Graph_Visualization()   
        else:
            print("This is invalid input.Try Again!")
            print(Users.displayMenu())
            choice=int(input("Please enter your choice: "))
    
    print("Thank you for using our system")
main()
