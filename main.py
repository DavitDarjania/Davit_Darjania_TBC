import sys
import menu
import csv
from some_functions import if_csv_exists
length = len(sys.argv)
if length == 1:
    menu.menu()
elif length == 2:
    if sys.argv[1] == "-p" or sys.argv[1] == "--pig-dice-game":
        if if_csv_exists('Games/Pig_Dice.csv'):
            with open('Games/Pig_Dice.csv') as file_csv:
                text = csv.reader(file_csv)
                text = list(zip(*text))
                for row in text:
                    print(row)
        else:
            print("Pig dice - CSV File does not exists")
    elif sys.argv[1] == "-t" or sys.argv[1] == "--tic-tac-toe":
        if if_csv_exists('Games/tic_tac.csv'):
            with open('Games/tic_tac.csv') as file_csv:
                text = csv.reader(file_csv)
                text = list(zip(*text))
                for row in text:
                    row = str(row).replace("[", "").replace("]", "").replace("'", "")
                    print(row)
        else:
            print("tic-tac-toe - CSV File does not exists")
    elif sys.argv[1] == "-d" or sys.argv[1] == "--data":
        if if_csv_exists('menu_aautorization/Data.csv'):
            with open('menu_aautorization/Data.csv') as file_csv:
                text = csv.reader(file_csv)
                for row in text:
                    row = str(row).replace("[", "").replace("]", "").replace("'", "")
                    print(row) 
        else:
            print("Data - csv does not exists")
    elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
        with open('help.txt') as file_txt:
            text = csv.reader(file_txt)
            for row in text:
                row = str(row).replace("[", "").replace("]", "").replace("'", "")
                print(row)
elif length == 3:
    if if_csv_exists('menu_aautorization/Data.csv'):
        if (sys.argv[1] == "-d" and sys.argv[2] == "--sorted") or sys.argv[1] == "--data" and sys.argv[2] == "--sorted":
            data = []
            with open('menu_aautorization/Data.csv') as file_csv:
                text = csv.reader(file_csv)
                next(text, None)
                for row in text:
                    data.append(row)
            data.sort(key= lambda row: row[0])
            fieldnames = ["Name,", "Surname,", "Nickname,", "Password,", "Tel"]
            for names in fieldnames:
                print(names, end=" ")
            print()
            for roww in data:
                roww = str(roww).replace("[", "").replace("]", "").replace("'", "")
                print(roww)
    else:
        print("Data - csv does not exists")
