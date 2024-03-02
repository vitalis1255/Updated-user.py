# Assessment:
# Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored
# in a user profile. Make a method called describe_user() that prints a summary
# of the user’s information. Make another method called greet_user() that prints
# a personalized greeting to the user.
# Create several instances representing different users, and call both meth-
# ods for each user.



# B
# Login Attempts: Add an attribute called login_attempts to your User class 
# Write a method called increment_login_attempts()
# that increments the value of login_attempts by 1. Write another method called
# reset_login_attempts() that resets the value of login_attempts to 0.
# Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was incremented
# properly, and then call reset_login_attempts(). Print login_attempts again to
# make sure it was reset to 0.


# Assessment C
# Admin: An administrator is a special kind of user. Write a class called
# Admin that inherits from the User class  Add an attribute, privileges, that stores a list of
# strings like "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator’s set of
# privileges. Create an instance of Admin, and call your method.


# D
# Privileges: Write a separate Privileges class. The class should have one
# attribute, privileges, that stores a list of strings as described in C.
# Move the show_privileges() method to this class. Make a Privileges instance
# as an attribute in the Admin class. Create a new instance of Admin and use your
# method to show its privileges.


class User:
    """
    Create class
    """
    def __init__(self, first_name, last_name, login_attempts = 1):
        """
        Initialize values
        """
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts

        self.user_profile = []

    def add_profile(self, phone,address,email,religion,level):
        """
        Add User Profile
        """
        for user in self.user_profile:
            if user["first_name"] == self.first_name:
                print("Name already exists")
                return
        
        #add new name if the name does not exist
        new_user = {

            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone": phone,
            "address": address,
            "email": email,
            "religion": religion,
            "level": level
        }

        self.user_profile.append(new_user)

        print("Added Successfully!!!")



    def update_user(self, phone,address,email,religion,level):
        """
        Update user profile
        """
        update_name = {

            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone": phone,
            "address": address,
            "email": email,
            "religion": religion,
            "level": level
        }
        self.user_profile.append(update_name)

        print("user updated successfully")

        
               


    def describe_user(self):
        """
        prints a summary of the user information
        """
        return self.user_profile
    

    def greet_user(self):
        """
        prints a personalized greeting to the user.
        """
        return f"You are warmly welcome {self.first_name}  {self.last_name}"
    
    
    def increment_login_attempts(self, login_attempts ):
        """
        Increments the value of login_attempts by 1
        """
        self.login_attempts += login_attempts

        return self.login_attempts
    

    def reset_login_attempts(self):
        """
        Resets the value of login_attempts to 0
        """
        self.login_attempts = 0

        return self.login_attempts
    

    

class Privileges:

    def __init__(self):
         
         #stores strings as in C
        #privilges attribute is removed from the Admin class.
        self.privileges = [

            "can add post", "can delete post",
            "can ban user", "can suspend user",
            "can bill user for an error","can pardon user",
            "can edit post", "can remove post"
        ]

    #moved show_privileges () from Admin class to Privilege class.
    #The show_privilege() is deleted at Admin class.
    def show_privileges(self):
        """
         lists the set of privilages
         for the administrator
        """
        #print not as a list
        for privilege in self.privileges:
            print(privilege)
        


class Admin(User):
    """
    Admin that inherits from the User class
    """
    def __init__(self, first_name, last_name, longin_attempts=1):
        super().__init__(first_name, last_name, longin_attempts)
        
        #making a privileges instance as an attribute in the Admin class. Assign everythin
        #in the Privilege class to self.privilege_instance.
        self.privilege_instance = Privileges()

        #self.privileges = [

            #"can add post", "can delete post",
            #"can ban user", "can suspend user",
           # "can bill user for an error","can pardon user",
           # "can edit post", "can remove post"
       # ]

    #def show_privileges(self):
      #  """
        # lists the set of privilages
        # for the administrator
       # """
        #for privilege in self.privileges:
         #   print(privilege)


    
user1 = User("Joe","Odo",1)
user1.add_profile("08066023002","no 11 odim","vitaboy@gmail.com","christian","student")
user1.add_profile("08030023112","no 190 ovoko","gentleboy@gmail.com","muslim","businessman")
user2 = User("Izu","Onyeke",1)
user2.update_user("090234567","no 12 opo","opuy@gmail.com","muslim","teacher")
user3 = User("James","Onah",1)
user3.update_user("0711110234","no 128 obodo","myguy@gmail.com","pagan","businessLady")
user4 = User("Norbert", "Abonyi",1)
user4.update_user("080987645","no 1276 olpolo","mygirl@gmail.com","none","Engr")
user5 = User("Onyinye", "okoro",1)
user5.update_user("090234008567","no 1442 opllo","oppoy@gmail.com","nothing","teaching")
print()
print(user1.describe_user())
print(user2.describe_user())
print(user3.describe_user())
print(user4.describe_user())
print(user5.describe_user())
print()
print(user1.greet_user())
print(user2.greet_user())
print(user3.greet_user())
print(user4.greet_user())
print(user5.greet_user())
print()
print("User 1 Incremented by:", user1.increment_login_attempts(1))
print("User 2 Incremented by:", user2.increment_login_attempts(2))
print("User 3 Incremented by:", user3.increment_login_attempts(3))
print("User 4 Incremented by:", user4.increment_login_attempts(4))
print("User 5 Incremented by:", user5.increment_login_attempts(5))
print()
print("user 1 after increment: ",user1.login_attempts)
print("user 2 after increment: ",user2.login_attempts)
print("user 3 after increment: ",user3.login_attempts)
print("user 4 after increment: ",user4.login_attempts)
print("user 5 after increment: ",user5.login_attempts)
print()
print("Reset User 1: ", user1.reset_login_attempts())
print("Reset User 2: ", user2.reset_login_attempts())
print("Reset User 3: ", user3.reset_login_attempts())
print("Reset User 4: ", user4.reset_login_attempts())
print("Reset User 5: ", user5.reset_login_attempts())
print()

#Create an instance of Admin, and call your method.
admin = Admin("man","odu",1)
print("PRIVILEGES: ")
#Create a new instance of Admin and use your
# method to show its privileges.
admin.privilege_instance.show_privileges()
print()
