import random
from menu_aautorization.dataset import DATASET
import pandas as pd
import menu_aautorization.registration as registration
import gamelab
from some_functions import dots
from some_functions import if_csv_exists
def menu():
    print("👉 Welcome in Gamelab ", end="")
    while True:
        print("Registration 👈: ")
        print("1. Register\n2. Play\n3. Forgot password?\n4. Quit")
        choice = input("Enter Your choice: ").lower().strip()
        while True:
            if choice == "register" or choice == "1":
                new_user = registration.User()
                new_user.register()
                name, surname, password, tel = new_user.get()
                if if_csv_exists("menu_aautorization/Data.csv"):
                    while True:
                        nickname = input("What is Your Nickname: ")
                        if nick_val(nickname):
                            add_to_csv(name, surname, nickname, password, tel)
                            print("You registered 🥳")
                            break
                        else:
                            print("This nickname exists, Try again!")
                else:
                    nickname = input("What is Your Nickname: ")
                    create_csv(name, surname, nickname, password, tel)
                break        
            elif choice == "play" or choice == "2":
                your_nickname = input("Enter your nickname: ")
                if if_csv_exists("menu_aautorization/Data.csv"):
                    if check_the_presence(your_nickname, "Nickname"):
                        passw = input("What is your password: ")
                        if check_the_passw(your_nickname, passw):
                            print("Congrats you signed in 🥳")
                            gamelab.gamelab(your_nickname)
                            break
                        else:
                            print("Incorret password, try again!")
                else:
                    print("There is no any user Registered!")
                    break
            elif choice == "forgot password" or choice == "3":
                check_nick = input("What is your nickname: ")
                if if_csv_exists("menu_aautorization/Data.csv"):
                    if check_the_presence(check_nick, "Nickname"):
                        tel_num = input("Enter mobile number: ") 
                        if check_the_mobile(check_nick, tel_num):
                            dots("Sending..........")
                            randnum = generate_int(6)
                            print(f"This is 6-digit one time code ( {randnum} )") 
                            while True:
                                my_guess = input("Enter the one time code we sent on given number: ").strip()
                                if my_guess == randnum:
                                    passwordd = return_the_passw(check_nick)
                                    print("Okay here is your password-----> ", passwordd)
                                    question = input("Do you want to change Password? (Y/N): ").strip().lower()
                                    if question == "y":
                                        while True:
                                            new_passw = input("Enter new password: ")
                                            if registration.password_validator(new_passw) == "Okay Your password is strong":
                                                print(registration.password_validator(new_passw))
                                                repeated = input("Repeat you password: ")
                                                if repeated == new_passw:
                                                    print("You changed the password 🥳")
                                                    change_password(check_nick, new_passw)
                                                    break
                                                else:
                                                    print("Repeated password is incorrect!")
                                                    continue
                                            else:
                                                print(registration.password_validator(new_passw))
                                                continue
                                        break
                                    elif question == 'n':
                                        print("You must remember it than!")
                                        break
                                else:
                                    print("Incorrect guess!")
                                    continue
                break
                                
                                
            elif choice == "quit" or choice == "q" or choice == "4":
                exit("You left the game 😉")
                
def check_the_presence(name, initializator):
    my_list = pd.read_csv('menu_aautorization/Data.csv')
    for nickname in my_list[initializator]:
        if nickname == name:
            return True
    print(f"Invalid {initializator}, Try again!")
    return False
def check_the_passw(name, passw):
    my_list = pd.read_csv('menu_aautorization/Data.csv')
    for nickname in my_list["Nickname"]:
        print(nickname)
        if nickname == name:
            my_full_list = my_list[my_list["Nickname"] == nickname]
            if any(my_full_list["Password"] == passw): # any returns True
                return True
            else:
                return False
def add_to_csv(name, surname, nickname, password, tel):
    new_row ={
    "Name": name,
    "Surname": surname,
    "Nickname" : nickname,
    "Password" : password,
    "Tel": tel
    }
    newdata = pd.read_csv('menu_aautorization/Data.csv')
    newrow = pd.DataFrame([new_row])
    newdata = pd.concat([newdata, newrow], ignore_index=True)
    newdata.to_csv('menu_aautorization/Data.csv', index=False)
def create_csv(name, surname, nickname, password, tel):
    DATASET["Name"].append(name)
    DATASET["Surname"].append(surname)
    DATASET["Nickname"].append(nickname)
    DATASET["Password"].append(password)
    DATASET["Tel"].append(tel)
    newdata = pd.DataFrame(DATASET)
    newdata.to_csv('menu_aautorization/Data.csv', index=False)
def check_the_mobile(name, tel):
    my_list = pd.read_csv('menu_aautorization/Data.csv')
    for nickname in my_list["Nickname"]:
        if nickname == name:
            my_full_list = my_list[my_list["Nickname"] == nickname]
            if any(my_full_list["Tel"] == int(tel)): # any returns True
                return True
            else:
                print("Invalid Telefon number!")
                return False
def generate_int(n):
    my_list_int = ""
    for i in range(n):
        my_list_int += str(random.randint(0,9))
    return my_list_int
def return_the_passw(name):
    my_list = pd.read_csv('menu_aautorization/Data.csv')
    for nickname in my_list["Nickname"]:
        if nickname == name:
            my_full_list = my_list[my_list["Nickname"] == nickname]
            return my_full_list["Password"][1]
def change_password(nick, passw):
    my_list = pd.read_csv('menu_aautorization/Data.csv')
    filtered = my_list["Nickname"] == nick
    my_list.loc[filtered, "Password"] = passw
    my_list.to_csv('menu_aautorization/Data.csv', index=False)
def nick_val(nick):
    my_list = pd.read_csv('menu_aautorization/Data.csv')
    if any(my_list["Nickname"] == nick):
        return False
    return True
if __name__ == "__main__":
    menu()