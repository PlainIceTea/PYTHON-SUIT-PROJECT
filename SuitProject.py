import random

#Score
playerScore = 0
BotScore = 0

#Bot brain
def BotChoose():
     x = random.randint(1,3)
     if(x == 1):
          return "kertas"
     elif(x == 2):
          return "batu"
     elif(x == 3):
          return "gunting"

def brain(inputPlayer , inputBot):
        global playerScore, BotScore  
    #gunting - kertas - batu
        if inputPlayer == "gunting":
            if inputBot == "gunting":
                print("SERI")
            elif inputBot == "batu":
                  print("Player Menang")
                  playerScore += 1
            elif inputBot == "kertas":
                  print("Bot menang")
                  BotScore += 1
#kertas - batu - gunting
        elif inputPlayer == "kertas":
            if inputBot == "gunting":
                print("Player Menang")
                playerScore += 1
            elif inputBot == "batu":
                  print("Bot menang")
                  BotScore += 1
            elif inputBot == "kertas":
                  print("SERI")
#batu - gunting - kertas
        elif inputPlayer == "batu":
            if inputBot == "gunting":
                print("Player Menang")
                playerScore += 1
            elif inputBot == "batu":
                  print("SERI")
            elif inputBot == "kertas":
                  print("Bot menang")
                  BotScore += 1

#Main
loop = 1
while(playerScore != 3 and BotScore != 3):
     print("Babak ke-",loop)
     inputPlayer = input('SUIT ! ') 
     inputBot = BotChoose()
     print("bot->",inputBot)
     brain(inputPlayer,inputBot)
     loop += 1
     print()

if (playerScore == 3):
     print("SLAMAT ANDA MENANG!")
else:
     print("BOO ANDA KALAH")
     






