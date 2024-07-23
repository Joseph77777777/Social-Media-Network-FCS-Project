from Social_Network.UsersManagement import Users

def main():
    U1=Users()
    logged_in_user=None
    print(Users.displayMenu(False))
    try:
      choice=int(input('Please enter your choice: '))
      while(choice!=16):
         if (choice==0):
            user_id=int(input('Enter user ID: '))
            full_name=input('Enter user full name: ')
            logged_in_user=U1.check_user_exist(user_id,full_name)
            print(Users.displayMenu(logged_in_user!=None))
            print(f'Hello {full_name}')
            choice=int(input('Please enter your choice: '))

         elif(choice==1):
            user_id=int(input('Enter user ID: '))
            full_name=input('Enter user full name: ')
            U1.add_new_user(user_id,full_name)
            print(U1)
            print(Users.displayMenu(logged_in_user!=None))
            choice=int(input('Please enter your choice: '))

         elif(choice==2):
            user_id=int(input('Enter user ID to be removed: '))
            U1.remove_user(user_id)
            print(Users.displayMenu(logged_in_user!=None))
            choice=int(input('Please enter your choice: '))

         elif(choice==3):
            U1.Network_Statistics()

         elif(choice==4):
            friend_Id=int(input('Enter User ID to follow: '))
            weight=int(input('How close are you from 1 to 5:'))
            U1.follow_User(logged_in_user, friend_Id,weight)
            print(U1)
            print(Users.displayMenu(logged_in_user!=None))
            choice=int(input('Please enter your choice: '))

         elif(choice==5):
            
            friend_Id=int(input('Enter User ID to Unfollow: '))
            U1.unfollow_User(logged_in_user, friend_Id)
            print(Users.displayMenu(logged_in_user!=None))
            choice=int(input('Please enter your choice: '))
            
         elif(choice==6):
            adding_post=input('Enter a post: ')
            U1.update_post_forUser(logged_in_user,adding_post)
            print(f'Your posts are:{logged_in_user.posts}')
            print(Users.displayMenu(logged_in_user!=None))
            choice=int(input('Please enter your choice: '))

         elif(choice==7):
            adding_Interest=input('Enter an interest: ')
            U1.update_interests_forUser(logged_in_user,adding_Interest)
            print(f'Your posts are:{logged_in_user.interests}')
            print(Users.displayMenu(logged_in_user!=None))
            choice=int(input('Please enter your choice: '))

         elif(choice==8):
            sorted_users = U1.users_sorted_byName()
            for userId, name in sorted_users.items():
               print(f'User ID: {userId}, Name: {name.fullName}')
            print(Users.displayMenu(logged_in_user!=None))
            choice=int(input('Please enter your choice: '))

         elif(choice==9):
               Name = input(f'Enter user\'s name: ')
               U=U1.search_byName(Name)
               print(U)
               print(Users.displayMenu(logged_in_user!=None))
               choice=int(input('Please enter your choice: '))
            
         elif(choice==10):
            ID=int(input('Enter user\'s ID: '))
            U=U1.search_byId(ID)
            print(U)
            print(Users.displayMenu(logged_in_user!=None))
            choice=int(input('Please enter your choice: '))

         elif(choice==11):
            Start_userId=int(input('Enter a start user ID: '))
            bfs=U1.BFS(Start_userId)
            print(f'The BFS traversal: {bfs}')
            print(Users.displayMenu(logged_in_user!=None))
            choice=int(input('Please enter your choice: '))
            
         elif(choice==12):
            Start_userId=int(input('Enter a start user ID: '))
            dfs=U1.DFS(Start_userId)
            print(f'The DFS traversal: {dfs}')
            print(Users.displayMenu(logged_in_user!=None))
            choice=int(input('Please enter your choice: '))
            
         elif(choice==13):
            Start_userId=int(input('Enter a start user ID: '))
            Target_userId=int(input('Enter a target user ID: '))
            Short_path=U1.shortest_path(Start_userId,Target_userId)
            print('The shortest path is : {Short_path}')
            print(Users.displayMenu(logged_in_user!=None))
            choice=int(input('Please enter your choice: '))
            

         elif(choice==14):
            U1.Graph_Visualization() 
            print(Users.displayMenu(logged_in_user!=None))
            choice=int(input('Please enter your choice: '))  
         else:
               print('This is invalid input.Try Again!')
               print(Users.displayMenu(logged_in_user!=None))
               choice=int(input('Please enter your choice: '))
      
      print('Thank you for using our Social Network System')
    except:
      print('OOPs This is invalid input.Try Again!')
      main()

       
   
main()
