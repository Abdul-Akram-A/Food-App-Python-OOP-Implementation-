class UserInfo:
    def __init__(self): 
        self.name = None
        self.phone=None
        self.email=None
        self.pwd=None
    def Validate_userInfo(self,name,phone,email,password):
        if len(name)>=5:
            self.name = name
        else:
            print("Enter Valid Name: Length must be greater than 4 characters")
            return False
        if len(str(phone))==10:
            self.phone = phone
        else:
            print("Please Enter a valid Phone Number")
            return False
        if "@gmail.com" in email or "@yahoo.com" in email:
            self.email = email
        else:
            print("Enter Valid email")
            return False
        if len(password) >=8:
            self.pwd = password
        else:
            print("Enter Valid Password: Length must be greater than 8 characters")
            return False
        return True