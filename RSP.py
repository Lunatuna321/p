import random

TurnsTaken = 0
AllowTimesPlaying = 3

number = random.randint(1,3)
print (number)

Rock = 3
Scissors = 2
Paper = 1

while AllowTimesPlaying:
    PlayerAttempt = input("Rock, scissors, paper!")
    if PlayerAttempt == "Rock":
        PlayerAttempt = 3
    if PlayerAttempt =="Scissors":
        PlayerAttempt = 2
    if PlayerAttempt == "paper":
        PlayerAttempt = 1
    TurnsTaken += 1
    if ((number == 1) and (PlayerAttempt == Scissors)) or ((number== 2) and (PlayerAttempt == Rock)) or ((number == 3) and (PlayerAttempt == Paper)):
        print("You won...")
    else :
        print("You lost!")
       
