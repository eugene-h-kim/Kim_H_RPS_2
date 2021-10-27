from random import randint
from gameComponents import winLose, gameVars


# set up our game loop so that we can keep playing and not exit
while gameVars.player is False:
  gameVars.player = input("Choose your weapon: rock, paper or scissors: ")
  gameVars.computer = gameVars.choices[randint(0, 2)]

  print("player chose: " + gameVars.player)
  print("computer chose:" + gameVars.computer)

  if gameVars.computer == player:
    # tie - nothing else to compare, so it'll exit
    print("tie! try again")

  elif player == "rock":
    if gameVars.computer == "paper":
      print("you lose!")
      playerLives = playerLives - 1
    else:
      print("you win!")
      computerLives = computerLives - 1

  elif player == "paper":
    if gameVars.computer == "scissors":
      print("you lose!")
      playerLives = playerLives - 1
    else:
      print("you win!")
      computerLives = computerLives - 1

  elif player == "scissors":
    if gameVars.computer == "rock":
      print("you lose!")
      playerLives = playerLives - 1
    else:
      print("you win!")
      computerLives = computerLives - 1

  print("player life count: " + str(playerLives))
  print("computer life count: " + str(computerLives))

  if playerLives == 0:
    winLose.winorlose("lost")
    
  elif computerLives == 0:
    winLose.winorlose("won")
    
  player = False
