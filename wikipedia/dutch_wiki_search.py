from bs4 import BeautifulSoup
import urllib.request
import urllib.error

# Asking for the word to look up

word = input("word: ")
if " " in word:
    word = word.replace(" ", "_")
if word[0].islower:
    word = word[0].upper() + word[1:]
if "_" in word:
    space1 = (word.index("_") + 1)
if "_" in word:
    if word[space1].islower:
        word = word[:space1] + word[space1].upper() + word[space1+1:]

# Scary BeautifulSoup stuff

content = urllib.request.urlopen('https://nl.wikipedia.org/wiki/' + word)
read_content = content.read()
soup = BeautifulSoup(read_content, 'html.parser')
pAll = soup.find_all('p')
answer = str(pAll[0].text)

# Removing words I don't want using replace command

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

# Printing the answer

if len(answer) == len(word) + 21:
    print(word + " kan verwijzen naar meerdere dingen. Probeer wat specifieker te zijn.")
elif str(pAll[0].text) != len(word) + 21:
    print(answer)
