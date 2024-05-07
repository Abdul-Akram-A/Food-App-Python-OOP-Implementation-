#Main Page
from Login import LoginSystem
from MainMenu import Mainmenu
class Initialization:
    options={1:"Login",2: "SignUp",3:"Exit"}
    
    @staticmethod
    def Init():
        login=LoginSystem()
        print("<<Welcome to our Food App>>")
        while True:
            try:
                for key,value in Initialization.options.items():
                    print(f"{key}.{value}",end=" ")
                choice=int(input("\nEnter your option number :"))
                login.Validate(Initialization.options[choice])
            except (ValueError, KeyError):
                print("------Chooe Valid Choice------")
                
              

main=Initialization()
main.Init()
