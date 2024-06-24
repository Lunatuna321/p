import random

guessTaken = 0

number = random.randint(1,20)
AllowKeepGuessing = True

while AllowKeepGuessing:
    playerAttempt = int(input("Take a guess "))
    guessTaken += 1
    if (playerAttempt > number):
        print("Number too high, you idiot")
    elif (playerAttempt < number):
        print("Number too low")
    if (playerAttempt == number):
        print("You won")
        AllowKeepGuessing = False
    
print("Game Over")