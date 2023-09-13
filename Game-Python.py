import random
import os
os.system("cls")
print("Welcome To the Rock Paper Scissor Game")
Playerscore=0
Computerscore=0
Tiescore=0

while True:
    print("Player:",Playerscore,"Computer:",Computerscore,"Tie:",Tiescore)
    player=input("Player Has to Choose either Rock, Paper, or Scissors or quit:")
   
    if player == "quit":
       print("GAME-OVER")
       break
    print("Player has Chose:",player)
    
    choices=["Rock","Paper","Scissors"]
    computer=random.choice(choices)
    print("Computer Has chose",computer)
    
    if player==computer:
        print("It's a Tie")
        Tiescore+=1
    elif((player=="Rock" and computer=="Scissors")
    or (player=="Paper" and computer =="Rock")
    or (player=="Scissors" and computer =="Paper")):
        print("Player Wins")
        Playerscore+=1
    else:
        print("Computer Wins")
        Computerscore+=1

        
    


