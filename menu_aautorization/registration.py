class User():
    name = ""
    surname = ""
    __password = ""
    tel = ""
    def register(self):
        while True:
            self.name = input("What is your name? ")
            if user_validator(self.name) == True:break
            else: print(user_validator(self.name, "Name"))
        while True:
            self.surname = input("What is your last name? ")
            if user_validator(self.surname) == True:break
            else: print(user_validator(self.surname, "Surname"))
        while True:
            self.tel = input("For Emergency enter your mobile number: ")
            if telnum_validator(self.tel) == True:break
            else: print(telnum_validator(self.tel))
        while True:
            self.__password = input("Create Your password: ")
            if password_validator(self.__password) == "Okay Your password is strong":
                repeated = input("Repeat you password: ")
                if repeated == self.__password:
                    break
                else:
                    print("You had a mistake")
            else: print(password_validator(self.__password))
    def get(self):
        return self.name, self.surname, self.__password, self.tel
def user_validator(name, initializator = None):
    if name.isdigit():
        return f"Your {initializator} should not be numerical!"
    if not name.isalpha():
        return f"Your {initializator} should include only words!" 
    if name != name.capitalize():
        return f"Enter only capitalized input!"
    return True
def password_validator(passw):
    if len(passw) < 8:
        return "Length must be more than 8 symbols!"
    strval, intval, symbolval = False, False, False
    mystring = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    myint = "0123456789"
    mysymbol = "!@#$%^&*()?|~"
    for element in passw:
        if element in mystring: strval = True
        elif element in myint: intval = True
        elif element in mysymbol: symbolval = True
    if strval and intval and symbolval: return "Okay Your password is strong"
    elif strval and intval: return "You should input at least one special symbol '!@#$%^&*()?|~'"
    elif strval and symbolval: return "There should be at least one number!"
    elif intval and symbolval: return "Your password should include words!"
    elif strval: return "Weak password include numbers and symbols too!"
    elif intval: return "Weak password Include words and symbols too!"
    elif symbolval: return "Medium password but include words and integers for more safety"
def telnum_validator(tel):
    if not tel.isdigit():
        return "Tel. number must be all integer!"
    if len(tel) != 9:
        return "Tel. number must be 9 digit!"
    if tel[0] != "5":
        return "Tel. numbers starts with 5!"
    return True
