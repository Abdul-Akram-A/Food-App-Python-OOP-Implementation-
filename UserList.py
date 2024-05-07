from UserDetails import UserInfo

class UserList():
    __User = []
    count = 0
    def Add_user(self, user):
        
        if isinstance(user, UserInfo):
            self.__User.append(user)
            self.count += 1
            print("Successfully registered")
        else:
            print("Invalid user")
            
    def Login_check(self,username,password):
        for user_d in self.__User:
            if user_d.email == username and user_d.pwd == password:
                print("Login detail found")
                return user_d
        print("Login detail not found")
        return None