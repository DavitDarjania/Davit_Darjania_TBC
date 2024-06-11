from Games.pig_dice_game import dots
import random
def tic_tac_toe():
    wins = 0
    looses = 0
    while True:
        question = input("Do you want to play Tic-tac-toe?? (Y/N): ").strip().upper()
        if question == "Y": pass
        elif question == "N":
            print("Game is over!")
            break
        else:
            print("Incorrect input. Try again")
            continue
        matrix = [[" "," "," "], [" ", " ", " "], [" ", " ", " "]]
        counter = 0
        print(f" {matrix[0][0]} | {matrix[0][1]} | {matrix[0][2]}\n-----------\n {matrix[1][0]} | {matrix[1][1]} | {matrix[1][2]}\n-----------\n {matrix[2][0]} | {matrix[2][1]} | {matrix[2][2]}")
        while True:
            transposed_matrix = list(zip(*matrix))
            x_won = any(sum(1 for element in row if element == "X") == 3 for row in matrix)
            O_won = any(sum(1 for element in row if element == "O") == 3 for row in matrix)
            x_won_transposed_matrix = any(sum(1 for element in row if element == "X") == 3 for row in transposed_matrix)
            O_won_transposed_matrix = any(sum(1 for element in row if element == "O") == 3 for row in transposed_matrix)
            diagonal_x = ("X" == matrix[0][0] and "X" == matrix[1][1] and "X" == matrix[2][2]) or ("X" == matrix[0][2] and "X" == matrix[1][1] and "X" == matrix[2][0])
            diagonal_o = ("O" == matrix[0][0] and "O" == matrix[1][1] and "O" == matrix[2][2]) or ("O" == matrix[0][2] and "O" == matrix[1][1] and "O" == matrix[2][0])
            if x_won or x_won_transposed_matrix or diagonal_x:
                print("You won!")
                wins += 1
                break
            if O_won or O_won_transposed_matrix or diagonal_o:
                print("You lost!")
                looses += 1
                break
            row, column = input("Row: "), input("Column: ")
            if row.isdigit() and column.isdigit():
                row, column = int(row) - 1, int(column) - 1
                if not row <=2 or not row>=0 or not column<=2 or not column>=0:
                    print("You should enter from 1 to 3")
                    continue
                if matrix[row][column] == "X" or matrix[row][column] == "O":
                    print("There is already symbol here :(")
                    continue
            else:
                continue
            comp_row, comp_column = random.randint(0,2), random.randint(0,2)
            matrix[row][column] = "X"
            print(f" {matrix[0][0]} | {matrix[0][1]} | {matrix[0][2]}\n-----------\n {matrix[1][0]} | {matrix[1][1]} | {matrix[1][2]}\n-----------\n {matrix[2][0]} | {matrix[2][1]} | {matrix[2][2]}")
            dots("Thinking.....", 0)
            while matrix[comp_row][comp_column] == "X" or matrix[comp_row][comp_column] == "O":
                comp_row, comp_column = random.randint(0,2), random.randint(0,2)
            matrix[comp_row][comp_column] = "O"
            counter += 1
            print(f" {matrix[0][0]} | {matrix[0][1]} | {matrix[0][2]}\n-----------\n {matrix[1][0]} | {matrix[1][1]} | {matrix[1][2]}\n-----------\n {matrix[2][0]} | {matrix[2][1]} | {matrix[2][2]}")
    return wins, looses
if __name__ == "__main__":
    tic_tac_toe()
