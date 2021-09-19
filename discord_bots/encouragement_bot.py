# The code won't work because the token (line 12) is secret. Change this to your own token.

from keep_alive import keep_alive
import os
import discord
import requests
import json
import random
from replit import db

# Making the token key secret and importing it.
my_secret = os.environ['TOKEN']

# Making the client
client = discord.Client()

# List to detect sad words
sad_words = ["sad", "depressed", "unhappy", "miserable", "depressing"]

starter_encouragements = [
    "Cheer up!",
    "Hang in there!",
    "You can do it!"
]


# If you run this functions, you get a random quote from zenquotes.io
# 'q' = quote and 'a' = author
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote


# Allowing users to add encouragements from the Discord server
def update_encouragements(encouraging_message):
    if "encouragements" in db.keys():
        encouragements = db["encouragements"]
        encouragements.append(encouraging_message)
        db["encouragements"] = encouragements

    # If they're aren't any encouragements in the database, then we need to create some.
    else:
        db["encouragements"] = [encouraging_message]


# Removes an encouragement
def delete_encouragement(index):
    encouragements = db["encouragements"]
    # Making sure the given index is actually in the list
    if len(encouragements) > index:
        del encouragements[index]
        db["encouragements"] = encouragements


# Show in console that log-in was successfull
@client.event
async def on_ready():
    print("logged in as {0.user}".format(client))


# Ignoring messages if it is the bot himself
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    # Sending "Hello" if someone types "$hello"
    if msg.startswith("$inspire"):
        quote = get_quote()
        await message.channel.send(quote)

    # Making it able for users to add encouragements
    options = starter_encouragements
    if "encouragements" in db.keys():
        options = options + list(db["encouragements"])

    # Detecting sad words, responding with positive messages
    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(options))

    # if a message that a user types starts with "$new", remove the command and add the rest to the list
    if msg.startswith("$new"):
        encouraging_message = msg.split("$new ", 1)[1]
        update_encouragements(encouraging_message)
        await message.channel.send("New encouraging message added!")

    # Allowing users to delete from database
    if msg.startswith("$del"):
        encouragements = []
        if "encouragements" in db.keys():
            index = int(msg.split("$del", 1)[1])
            delete_encouragement(index)
            encouragements = db["encouragements"]
        # Printing the new list
        await message.channel.send(encouragements)


keep_alive()

# Run the bot
client.run(my_secret)
