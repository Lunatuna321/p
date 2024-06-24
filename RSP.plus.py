import random

HandGest = ["rock", "paper", "scissors"]

answer = HandGest[random.randint(0, 2)]
print("I am going " + answer)


playerAttempt = (input("Rock, Paper, or Scissors? ")).lower()
if (playerAttempt == "rock" and answer == "scissors") | (playerAttempt == "paper" and answer == "rock") | (playerAttempt == "scissors" and answer == "paper"):
    print("You won")
elif (playerAttempt == answer):
    print("Tie!")
else:
    print("You Lose!")

        
    
