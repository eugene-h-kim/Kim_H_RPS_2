from random import randint

choices = ["rock", "paper", "scissors"]

# player will be the weapon the player chooses via input
player = input("Choose your weapon: rock, paper or scissors: ")

computer = choices[randint(0, 2)]

print("player chose: " + player)
print("computer chose:" + computer)

if (computer == player):
  # tie - nothing else to compare, so it'll exit
  print("tie! try again")

elif (player == "rock"):
  if (computer == "paper"):
    print("you lose!")
  else:
    print("you win!")

elif (player == "paper"):
  if (computer == "scissors"):
    print("you lose!")
  else:
    print("you win!")

elif (player == "scissors"):
  if (computer == "rock"):
    print("you lose!")
  else:
    print("you win!")