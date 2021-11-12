from random import randint
from gameComponents import winLose, gameVars, comparePlayers


# set up our game loop so that we can keep playing and not exit
while gameVars.player is False:
  
  gameVars.player = input("Choose your weapon: rock, paper or scissors: ")
  gameVars.computer = gameVars.choices[randint(0, 2)]
  print("============= RPS =============")
  print("player chose: " + gameVars.player)
  print("computer chose:" + gameVars.computer)
  comparePlayers.compare()
  print("player life count: " + str(gameVars.playerLives))
  print("computer life count: " + str(gameVars.computerLives))

  if gameVars.playerLives == 0:
    winLose.winorlose("======= lost =======")
    
  elif gameVars.computerLives == 0:
    winLose.winorlose("******* won *******")
    
  gameVars.player = False