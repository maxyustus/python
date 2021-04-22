import random

"""Rock, Paper, Scissors"""
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

your_move = int(input("What do you choose? Type 0  for Rock, 1 for Paper or 2 for Scrissors. "))
if your_move >= 3 or your_move < 0:
    print("You typed an invalid number, you lose!")
else:
    print(f"Your move:\n{game_images[your_move]}")
    computer_move = random.randint(0, len(game_images) - 1)
    print(f"Computer chose:\n{game_images[computer_move]}")

    if your_move == 0 and computer_move == 2:
        print("You win!")
    elif computer_move == 0 and your_move == 2:
        print("You lose")
    elif computer_move > your_move:
        print("You lose")
    elif your_move > computer_move:
        print("You win!")
    elif computer_move == your_move:
        print("It's a draw")


"""Treasure map"""
# row1 = ["1", "2", "3"]
# row2 = ["4", "5", "6"]
# row3 = ["7", "8", "9"]
# hashmap = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure?")
#
# horizontal = int(position[0])
# vertical = int(position[1])
#
# hashmap[vertical-1][horizontal-1] = "X"
# # selected_row = hashmap[vertical-1]
# # selected_row[horizontal-1] = "X"
# print(f"{row1}\n{row2}\n{row3}")