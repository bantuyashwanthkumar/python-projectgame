# creating a snake and water game and playing which is capable to user.
'''
1 for snake 
-1 for humam
0 for mungisa
'''

import random

youdict = {"s": 1, "h": -1, "m": 0}
reversedict = {1: "snake", -1: "human", 0: "mungisa"}

yourstr = input("Enter your choice (s for snake, h for human, m for mungisa): ").lower()

if yourstr not in youdict:
    print("Invalid input! Please enter 's', 'h', or 'm'.")
else:
    you = youdict[yourstr]
    computer = random.choice([-1, 0, 1])

    print(f"You chose {reversedict[you]}\nComputer chose {reversedict[computer]}")

    if computer == you:
        print("It's a draw.")
    else:
        if computer == -1 and you == 1:
            print("You win!")
        elif computer == -1 and you == 0:
            print("You lose.")
        elif computer == 1 and you == -1:
            print("You lose.")
        elif computer == 1 and you == 0:
            print("You win!")
        elif computer == 0 and you == 1:
            print("You lose.")
        elif computer == 0 and you == -1:
            print("You win!")
