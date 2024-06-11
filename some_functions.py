import time
import pandas as pd
import os
def dots(word, n=0):
    length = len(word) - 1
    if n > length:
        return print()
    print(word[n], end="")
    time.sleep(0.15)
    return dots(word, n + 1)
def ratings_for_games(nick, game_loc):
    df = pd.read_csv(game_loc)
    if any(df["Nickname"] == nick):
        filltered = df[df["Nickname"] == nick]
        return filltered["Wins"][0], filltered["Looses"][0]
    else:
        return 0,0
def if_csv_exists(name):
    if os.path.exists(name):
        return True
    return False