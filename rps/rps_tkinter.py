from random import choice
from tkinter import Tk, Entry, END, Button

# Start Program and give title
root = Tk()
root.title("Rock, Paper, Scissors")

rps_list = ["rock", "paper", "scissors"]


# Main Function

def button_click(rps):
    output_field.delete(0, END)
    you_chose = str(rps)
    while True:
        ai_chose = choice(rps_list)
        if you_chose == ai_chose:
            output_field.delete(0, END)
            output_field.insert(0, "It's a draw! You both chose " + you_chose + "!")
        elif you_chose == "rock" and ai_chose == "paper":
            output_field.delete(0, END)
            output_field.insert(0, "The AI won! You chose " + you_chose + " and the AI chose paper!")
        elif you_chose == "scissors" and ai_chose == "rock":
            output_field.delete(0, END)
            output_field.insert(0, "The AI won! You chose " + you_chose + " and the AI chose rock!")
        elif you_chose == "paper" and ai_chose == "scissors":
            output_field.delete(0, END)
            output_field.insert(0, "The AI won! You chose " + you_chose + " and the AI chose scissors!")
        elif you_chose == "paper" and ai_chose == "rock":
            output_field.delete(0, END)
            output_field.insert(0, "You won! You chose " + you_chose + " and the AI chose rock!")
        elif you_chose == "rock" and ai_chose == "scissors":
            output_field.delete(0, END)
            output_field.insert(0, "You won! You chose " + you_chose + " and the AI chose scissors!")
        elif you_chose == "scissors" and ai_chose == "paper":
            output_field.delete(0, END)
            output_field.insert(0, "You won! You chose " + you_chose + " and the AI chose paper!")
        else:
            output_field.delete(0, END)
            output_field.insert(0, "ERROR BLYAT " + you_chose + ' ' + ai_chose)
        break


# Buttons and Entry

b_rock = Button(root, text="rock", padx=331, pady=20, command=lambda: button_click("rock"))
b_paper = Button(root, text="paper", padx=329, pady=20, command=lambda: button_click("paper"))
b_scissors = Button(root, text="scissors", padx=323, pady=20, command=lambda: button_click("scissors"))

output_field = Entry(root, width=40)

# Giving the buttons locations and ending program

b_rock.grid(row=1, column=0)
b_paper.grid(row=2, column=0)
b_scissors.grid(row=3, column=0)

output_field.grid(row=5, column=0, padx=25, pady=10, ipady=10, ipadx=50)

root.mainloop()
