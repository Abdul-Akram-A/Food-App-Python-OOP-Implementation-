from UserDetails import UserInfo 
from UserList import UserList
from MainMenu import Mainmenu
class LoginSystem:
    Userlist=UserList()
    def Login(self):
        next_choice=""
        while next_choice!="N" and next_choice!="n":
            email = input("Enter your Email ID:")
            password=input("Enter password:")
            if self.Userlist.Login_check(email, password):
                menu=Mainmenu()
                menu.Start()
                break
            else:
                next_choice=input("Do you want to try again? Y/N : ")
    def SignUp(self):
        while True:
            name = input("Enter your Name:")
            phone= int(input("Enter Phone Number:"))
            email = input("Enter your Email ID:")
            password=input("Enter password:")
            user = UserInfo()
            if user.Validate_userInfo(name, phone, email, password):
                self.Userlist.Add_user(user)
                break  # Break the loop if validation succeeds
            else:
                print("Please try again.")
                
    def Exit(self):
        print("Thanks for using using our app")
        exit()

    def Validate(self,choice):
        getattr(self,choice)()