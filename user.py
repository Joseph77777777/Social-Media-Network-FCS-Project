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