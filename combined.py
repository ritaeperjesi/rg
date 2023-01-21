#bot_discord
import discord
import responses_discord


#main2
#import random_responses
import json
import re

# Load JSON data
def load_json(file):
    with open(file) as bot_responses:
        print(f"Loaded '{file}' successfully!")
        return json.load(bot_responses)


# Store JSON data
response_data = load_json("responses.json")

#BOT

def run_discord_bot():
    TOKEN = 'MTA2NjAyMjY4Mjg2MjMwMTI2NQ.GKQJL9._nSysqqRcWP2UTkNHLHojYw9TQv6IDEpzs8leg'
    intents = discord.Intents.default()
    intents.messages = True
    #intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)


while True:
    #our merge
    user_message = input("You: ")
    print("Bot:", get_response(user_input))

    #video chatbot
    #user_input = input("You: ")
    #print("Bot:", get_response(user_input))