# პროფესორი არის თამაში სადაც მათემატიკური კითხვებია, შესვლისთანავე გვეკითხება სიძნელის დონეს
# 1)რიცხვები 1-9 | 2)10-99 | 3)100-999
# არის 10 კითხვა, სწორად გაცემის შემთხვევაში გადადის შემდეგ კითხვაზე
# არასწორად გაცემის შემთხვევაში მეორდება კითხვა, 3 ჯერ ზედიზედ შეშლის შემთხვევაში წერს სწორ პასუხს
# და გადადის შემდეგ კითხვაზე
import random
def main():
    print("You are in game named professor in which you need to calculate and write correct answer.\nChoose level from 1 to 3")
    level, correct_counter, counter, not_counter, how_many = get_level(), 0, 0, True, 0  
    while counter < 10:
        if not_counter:
            x, y, z = generate_integer(level)
            how_many = 0
        else:
            how_many += 1
            not_counter = True
        if how_many == 3:
            print(x, y, z, "=", x + z)
            continue
        print(x, y, z, "= ", end = "")
        try:
            actual_input = int(input())
            if level == 1 or level == 2 or level == 3:
                result = x + z
                if actual_input == result:
                    correct_counter += 1
                    counter += 1
                    continue
                else:
                    raise ValueError
        except ValueError:
            counter +=1
            not_counter = False
            print("EEE")
            continue
    print(f"Score: {correct_counter}")
    return correct_counter
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level <= 0 or level > 3:
                raise ValueError
        except ValueError:
            continue
        else:
            break
    return level
def generate_integer(level):
    match level:
        case 1:
            number = random.randint(0, 9)
            number2 = random.randint(0, 9)
            return number, '+', number2
        case 2:
            number = random.randint(10, 99)
            number2 = random.randint(10, 99)
            return number, '+', number2
        case 3:
            number = random.randint(100, 999)
            number2 = random.randint(100, 999)
            return number, '+', number2
if __name__ == "__main__":
    main()