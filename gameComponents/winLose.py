from gameComponents import gameVars

def winorlose(status):
  print("you " + status)

  choice = input("Do you want to play again? y/n: ")

  if choice == "n":
    print("========== see ya! (looser) ==========")
    exit()
  elif choice == "y":
    gameVars.playerLives = 5
    gameVars.computerLives = 5
    gameVars.player = False
