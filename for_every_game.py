import pandas as pd
import os
from menu_aautorization.dataset import PIG_DICE_SET
def for_pig_dice(win, los, nick):
    if if_csv_exists('Games/Pig_Dice.csv'):
        if if_nick_exists(nick, 'Games/Pig_Dice.csv'):
            adding(win, los, nick, 'Games/Pig_Dice.csv')
        else:
            add_pig_csv(win, los, nick, 'Games/Pig_Dice.csv')
    else:
        create_pig(win, los, nick, 'Games/Pig_Dice.csv')
def for_tic_tac(win, los, nick):
    if if_csv_exists('Games/tic_tac.csv'):
        if if_nick_exists(nick, 'Games/tic_tac.csv'):
            adding(win, los, nick, 'Games/tic_tac.csv')
        else:
            add_pig_csv(win, los, nick, 'Games/tic_tac.csv')
    else:
        create_pig(win, los, nick, 'Games/tic_tac.csv')
def if_csv_exists(name):
    if os.path.exists(name):
        return True
    return False
def add_pig_csv(win, los, nick, filename):
    pig_dice = {
        "Nickname": nick,
        "Wins" : win,
        "Looses" : los
    }
    newdata = pd.read_csv(filename)
    newrow = pd.DataFrame([pig_dice])
    newdata = pd.concat([newdata, newrow], ignore_index=True)
    newdata.to_csv(filename, index=False)
def create_pig(win, los, nick, filename):
    PIG_DICE_SET["Nickname"].append(nick)
    PIG_DICE_SET["Wins"].append(win)
    PIG_DICE_SET["Looses"].append(los)
    newdata = pd.DataFrame(PIG_DICE_SET)
    newdata.to_csv(filename, index=False)
def if_nick_exists(nick, filename):
    my_list = pd.read_csv(filename)
    if any(my_list["Nickname"] == nick):
        return True
    return False
def add_to_each_other_pig(win, los, nick):
    my_list = pd.read_csv('Games/Pig_Dice.csv')
    new_df = pd.DataFrame({'Nickname': [nick], 'Wins': [win], 'Looses': [los]})
    combined = pd.concat([my_list, new_df], ignore_index=True)
    personal = combined[combined['Nickname'] == nick]
    personal["Wins"] = personal["Wins_x"] + personal["Wins_y"]
    personal["Looses"] = personal["Looses_x"] + personal["Looses_y"]
    combined.update(personal)
    combined.to_csv('Games/Pig_Dice.csv', index=False)
def adding(win, los, nick, filename):
    my_list = pd.read_csv(filename)
    filtered = my_list["Nickname"] == nick
    my_list.loc[filtered, "Wins"] += win
    my_list.loc[filtered, "Looses"] += los
    my_list.to_csv(filename, index=False)