import random



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

#Write your code below this line 👇
game_images = [rock, paper, scissors]

player_input = int(input("What do you choose?  Type 0 for Rock, 1 for Paper or 2 for Scissors!\n"))
if player_input >= 3 or player_input <0:
  print("You chose an incorrect value. Please start over.")
else:
  print(f"You chose {game_images[player_input]}")

  computer_input = random.randint(0,2)
  print(f"The Computer chose: {game_images[computer_input]}")

  if player_input == 0 and computer_input == 2:
    print("You won!")
  elif player_input == 1 and computer_input == 0:
    print("You won!")
  elif player_input == 2 and computer_input == 1:
    print("You won!")
  elif player_input == computer_input:
    if player_input == 0:
      print("Tie! Play again!")
  else:
    print("You lose!")
# create two players me and the PC
# require me to choose Rock paper or scissors (use .lower() for whatever is input)
# make the PC input a random function which will run after I input my choice
# ensure that the ascii art also displays after I have completed my choice and the pc has run its random function
# print something like : you chose rock and display the rock ascii art and then print the computer chose whatever random thing it chose.
# ensure that I have laid out the rules of RPS with if statements if whatever input is greater than whatever the pC chooses, then print,
# you lose or you win, etc..
