import Games.pig_dice_game as pig_dice_game
import Games.tic_tac_toe as tic_tac_toe
import Games.professor as professor
import for_every_game
from some_functions import ratings_for_games
from some_functions import if_csv_exists
def gamelab(nick):
    while True:
        print("What game do you want to play? 🧐\n1.Pig dice game\n2.Tic-Tac-Toe\n3.Profesor\n4.Quit")
        choice = input("Enter your choice: ").lower()
        if choice == "1" or choice == "pig dice game":
            if if_csv_exists('Games/Pig_Dice.csv'):
                pre_win, pre_los = ratings_for_games(nick, 'Games/Pig_Dice.csv')
            else:
                pre_win, pre_los = 0,0
            print(f"{nick} | Wins: {pre_win} | Looses: {pre_los}")
            wins, looses = pig_dice_game.rolling_dice()
            for_every_game.for_pig_dice(wins, looses, nick)
        elif choice == "2" or choice == "tic-tac-toe":
            wins, looses = tic_tac_toe.tic_tac_toe()
            for_every_game.for_tic_tac(wins, looses, nick)
        elif choice == "3" or choice == "professor":
            score = professor.main()
            print(score)
        elif choice == "4" or choice == "q" or choice == "quit":
            print("You left the gamelab.")
            break
if __name__ == "__main__":
    gamelab()