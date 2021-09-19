import random

you_chose = input("What would you like to choose? ")
you_chose = you_chose.lower()
rps_list = ["rock", "paper", "scissors"]
ai_chose = random.choice(rps_list)

if you_chose == ai_chose:
    print("It's a draw! You both chose " + you_chose + "!")
if you_chose == "rock" and ai_chose == "paper":
    print("The AI won! You chose " + you_chose + " and the AI chose " + ai_chose)
if you_chose == "scissors" and ai_chose == "rock":
    print("The AI won! You chose " + you_chose + " and the AI chose " + ai_chose)
if you_chose == "paper" and ai_chose == "scissors":
    print("The AI won! You chose " + you_chose + " and the AI chose " + ai_chose)
if you_chose == "paper" and ai_chose == "rock":
    print("You won! You chose " + you_chose + " and the AI chose " + ai_chose)
if you_chose == "rock" and ai_chose == "scissors":
    print("You won! You chose " + you_chose + " and the AI chose " + ai_chose)
if you_chose == "scissors" and ai_chose == "paper":
    print("You won! You chose " + you_chose + " and the AI chose " + ai_chose)
else:
    print("Error: You didn't choose rock, paper or scissors.")
