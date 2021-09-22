from random import choice
from tkinter import Tk, END, Button, Entry, W, E

# Start Program and give title
root = Tk()
root.title("Rock, Paper, Scissors")

rps_list = ["rock", "paper", "scissors"]

ai_score = 0
you_score = 0


# Main Function

def button_click(rps):
    global ai_score
    global you_score
    output_field.delete(0, END)
    you_chose = rps
    ai_chose = choice(rps_list)
    if you_chose == ai_chose:
        output_field.delete(0, END)
        output_field.insert(0, "It's a draw! You both chose " + you_chose + "!")
        ai_score += .5
        you_score += .5
        you_score_field.delete(0, END)
        ai_score_field.delete(0, END)
        you_score_field.insert(0, you_score)
        ai_score_field.insert(0, ai_score)
    elif you_chose == "rock" and ai_chose == "paper":
        output_field.delete(0, END)
        output_field.insert(0, "The AI won! You chose " + you_chose + " and the AI chose paper!")
        ai_score += 1
        ai_score_field.delete(0, END)
        ai_score_field.insert(0, ai_score)
    elif you_chose == "scissors" and ai_chose == "rock":
        output_field.delete(0, END)
        output_field.insert(0, "The AI won! You chose " + you_chose + " and the AI chose rock!")
        ai_score += 1
        ai_score_field.delete(0, END)
        ai_score_field.insert(0, ai_score)
    elif you_chose == "paper" and ai_chose == "scissors":
        output_field.delete(0, END)
        output_field.insert(0, "The AI won! You chose " + you_chose + " and the AI chose scissors!")
        you_score += 1
        ai_score_field.delete(0, END)
        ai_score_field.insert(0, ai_score)
    elif you_chose == "paper" and ai_chose == "rock":
        you_score += 1
        output_field.delete(0, END)
        output_field.insert(0, "You won! You chose " + you_chose + " and the AI chose rock!")
        you_score_field.delete(0, END)
        you_score_field.insert(0, you_score)
    elif you_chose == "rock" and ai_chose == "scissors":
        you_score += 1
        output_field.delete(0, END)
        output_field.insert(0, "You won! You chose " + you_chose + " and the AI chose scissors!")
        you_score_field.delete(0, END)
        you_score_field.insert(0, you_score)
    elif you_chose == "scissors" and ai_chose == "paper":
        you_score += 1
        output_field.delete(0, END)
        output_field.insert(0, "You won! You chose " + you_chose + " and the AI chose paper!")
        you_score_field.delete(0, END)
        you_score_field.insert(0, you_score)
    else:
        output_field.delete(0, END)
        output_field.insert(0, "ERROR BLYAT " + you_chose + ' ' + ai_chose)



# Buttons and Entry

b_rock = Button(root, text="rock", padx=331, pady=20, command=lambda: button_click("rock"))
b_paper = Button(root, text="paper", padx=329, pady=20, command=lambda: button_click("paper"))
b_scissors = Button(root, text="scissors", padx=323, pady=20, command=lambda: button_click("scissors"))

output_field = Entry(root, width=40)
you_score_field = Entry(root, width=4)
ai_score_field = Entry(root, width=4)

# Giving the buttons locations

b_rock.grid(row=1, column=0)
b_paper.grid(row=2, column=0)
b_scissors.grid(row=3, column=0)

output_field.grid(row=5, column=0, padx=25, pady=10)
you_score_field.grid(row=6, column=0, sticky=W)
ai_score_field.grid(row=6, column=0, sticky=E)

root.mainloop()
