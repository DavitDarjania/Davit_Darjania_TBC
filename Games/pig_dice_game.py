# ეს თამაში კამათელის გაგორებაზეა
import random
from some_functions import dots
def rolling_dice():
    wins, looses = 0, 0
    while True:
        question = input("Do you want to rool a dice? (Y/N): ").strip().upper()
        if question == "N":
            print("Okay game is over! 😋")
            return wins, looses
        elif question == "Y":
            first_dice, second_dice = random.randint(1,6), random.randint(1,6)
            print(f"You rolled |{first_dice}|")
            dots("Thinking...")
            print(f"Computer rolled |{second_dice}|")
            if first_dice == second_dice:
                print("It's Draw!")
                continue
            elif first_dice > second_dice:
                print("You won!")
                wins += 1
                continue
            else:
                print("You lost :(")
                looses += 1
                continue
        else:
            print("Incorrect input, Try again!")
            continue
if __name__ == "__main__":
    rolling_dice()
        

