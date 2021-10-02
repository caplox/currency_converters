from bs4 import BeautifulSoup
import urllib.request
from tkinter import Tk, Text, Entry, Button, END, INSERT
from urllib.error import HTTPError

root = Tk()
root.title("Dutch Wikipedia")

def random_click():
    content = urllib.request.urlopen('https://nl.wikipedia.org/wiki/Speciaal:Willekeurig')
    read_content = content.read()
    soup = BeautifulSoup(read_content, 'html.parser')
    pAll = soup.find_all('p')
    answer = str(pAll[0].text)

    answer = answer.replace("[1]", "")
    answer = answer.replace("[2]", "")
    answer = answer.replace("[3]", "")
    answer = answer.replace("[4]", "")
    answer = answer.replace("[5]", "")
    answer = answer.replace("[6]", "")
    answer = answer.replace("[7]", "")
    answer = answer.replace("[8]", "")
    answer = answer.replace("[9]", "")
    answer = answer.replace("[10]", "")
    answer = answer.replace("[11]", "")
    answer = answer.replace("(info / uitleg);", ":")

    output_field.delete('1.0', END)
    output_field.insert(INSERT, answer)


def conf_click():
    word = input_field.get()
    try:
        if " " in word:
            word = word.replace(" ", "_")
        if word[0].islower:
            word = word[0].upper() + word[1:]
        if "_" in word:
            space1 = (word.index("_") + 1)
            if word[space1].islower:
                word = word[:space1] + word[space1].upper() + word[space1 + 1:]

        content = urllib.request.urlopen('https://nl.wikipedia.org/wiki/' + word)
        read_content = content.read()
        soup = BeautifulSoup(read_content, 'html.parser')
        pAll = soup.find_all('p')
        answer = str(pAll[0].text)

        answer = answer.replace("[1]", "")
        answer = answer.replace("[2]", "")
        answer = answer.replace("[3]", "")
        answer = answer.replace("[4]", "")
        answer = answer.replace("[5]", "")
        answer = answer.replace("[6]", "")
        answer = answer.replace("[7]", "")
        answer = answer.replace("[8]", "")
        answer = answer.replace("[9]", "")
        answer = answer.replace("[10]", "")
        answer = answer.replace("[11]", "")
        answer = answer.replace("(info / uitleg);", ":")

        if len(answer) == len(word) + 21:
            output_field.delete('1.0', END)
            output_field.insert(INSERT, word + " kan verwijzen naar meerdere dingen. Probeer wat specifieker te zijn.")
        elif str(pAll[0].text) != len(word) + 21:
            output_field.delete('1.0', END)
            output_field.insert(INSERT, answer)
    except HTTPError:
        output_field.delete("1.0", END)
        output_field.insert(INSERT, "Hier bestaat nog geen artikel over.")


input_field = Entry(root)
output_field = Text(root)

cf_input_field = Button(root, text="Confirm?", command=lambda: conf_click())
random_input_field = Button(root, text="Random", command=lambda: random_click())

input_field.grid(row=0, column=0, padx=30, pady=2)
output_field.grid(row=1, column=0, padx=100, pady=50, columnspan=5, ipady=50)

cf_input_field.grid(row=0, column=1)
random_input_field.grid(row=0, column=2)

root.mainloop()
