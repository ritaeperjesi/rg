import discord
import responses_discord
#import os

#References
#for server
#https://www.youtube.com/watch?v=SPTfmiYiuok&ab_channel=freeCodeCamp.org


async def send_message(message, user_message, is_private):
    try:
        response = responses_discord.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'MTA2NjAyMjkyNzAwNDM0ODQ1Nw.Gy4pw_.iKXbpOyMc8JhkpZ6hBYsHsu1sVJC0EzfmmjqXg'
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

        #if message.content.startswith('$commands'):
            #await message.channel.send('This is a list of commands that I can say: ')

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)


    client.run(TOKEN)
    #client.run(os.getenv('TOKEN'))
