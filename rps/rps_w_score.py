import random

you_chose = input("What would you like to choose? ")
you_chose = you_chose.lower()
rps_list = ["rock", "paper", "scissors"]
ai_chose = random.choice(rps_list)
ai_score = 0
your_score = 0

def rps():
    global your_score
    global ai_score
    while True:
        if you_chose == ai_chose:
            print("It's a draw! You both chose " + you_chose + "!")
            ai_score += .5
            your_score += .5
        elif you_chose == "rock" and ai_chose == "paper":
            print("The AI won! You chose " + you_chose + " and the AI chose " + ai_chose)
            ai_score += 1
        elif you_chose == "scissors" and ai_chose == "rock":
            print("The AI won! You chose " + you_chose + " and the AI chose " + ai_chose)
            ai_score += 1
        elif you_chose == "paper" and ai_chose == "scissors":
            print("The AI won! You chose " + you_chose + " and the AI chose " + ai_chose)
            ai_score += 1
        elif you_chose == "paper" and ai_chose == "rock":
            print("You won! You chose " + you_chose + " and the AI chose " + ai_chose)
            your_score += 1
        elif you_chose == "rock" and ai_chose == "scissors":
            print("You won! You chose " + you_chose + " and the AI chose " + ai_chose)
            your_score += 1
        elif you_chose == "scissors" and ai_chose == "paper":
            print("You won! You chose " + you_chose + " and the AI chose " + ai_chose)
            your_score += 1
        else:
            print("Error: You didn't choose rock, paper or scissors.")
        break


rps()

def ask_cont():
    global rq_cont
    rq_cont = input("Do you want to continue? Y/N: ")

while True:
    ask_cont()
    if rq_cont == "Y":
        you_chose = input("What would you like to choose? ").lower()
        rps()
    if rq_cont == "N":
        print("Your score was: " + str(your_score) + ".")
        print("AI's score was: " + str(ai_score) + ".")
        break
