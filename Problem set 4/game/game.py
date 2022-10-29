from random import randint

while True:
    try:
        number = int(input("Level: "))
    except ValueError:
        continue
    if number > 0:
        break
level = randint(1, number)
while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        continue
    else:
        if guess < level:
            print("Too small!")
            continue
        elif guess > level:
            print("Too large!")
            continue
        else:
            print("Just right!")
            break