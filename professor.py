import random


def main():
    level = get_level()
    score = 0
    turns = 0
    # Prompts the user to solve each of those problem. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user up to three tries in total. If the user has still not answered correctly after three tries, the program should output the correct answer.
    while True:
        try:
            if turns != 10:
                chance = 0
                x, y = generate_integer(level)
                correct_answer = x + y
                while True:
                    if chance != 3:
                        user_answer = int(input(f"{x} + {y} = "))
                        if correct_answer == user_answer:
                            score += 1
                            break
                        else:
                            print("EEE")
                            chance += 1
                    elif chance == 3:
                        print(correct_answer)
                        break

                turns += 1
                pass
            else:
                break
        except:
            print(Exception)
    # The program should ultimately output the user’s score, a number out of 10.
    print("Score: ", score)


# Prompts the user for a level, . If the user does not input 1, 2, or 3, the program should prompt again.
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
            else:
                raise ValueError
        except ValueError:
            pass


# Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with  digits. No need to support operations other than addition (+).
def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        return x, y
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
        return x, y
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
        return x, y
    else:
        print("Too Complex")


if __name__ == "__main__":
    main()
