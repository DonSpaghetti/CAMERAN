import discord
from discord.ext import commands
import random
import asyncio

#permission = 137432256
#bot ID 521413514733158410
#https://discordapp.com/oauth2/authorize?&client_id=521413514733158410&scope=bot&permissions=137432256

token = open('token.txt', 'r').read()

class CAMERAN(discord.Client):
    bot = commands.Bot(command_prefix='$', description='I hunger...f̹͕̞͖̦̗̗̹͜͡o̶͉r͇͖̹̤̣ ̫̜͈̝͡ç͔̻̮̼̬̗̕o͖͕̜͍͙͉̹͎n҉͍̬̩̮̼̗͖́c͔̗̣̤̦į̗̱̝̞̞̱̺͔͡o̻͓̲͢͠u̶̸͔̟͓s̨̬̯͙̭͇͈͝n͇̯͉̳̰̙̕ḙ̵̖̦̘͚͕̼͠ͅs̜̘͕̦̺̪̙̰s̶̴͉͙̤̦͎͓̗.̢͎̞̼̺͎̱͔̰.̹̞̫.̡̥͍̀.̨̹̗')
    
    @bot.event
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        print(self.bot.description)

    @bot.event
    async def on_message(self, message):
        # we do not want the bot to reply to itself
        print(f"{message.channel}, {message.author}, {message.author.name}, {message.content}")
        if message.author.id == self.user.id:
            return
        elif message.content.startswith('lmao'.lower()):
            await message.channel.send('ayy')
        elif message.content.startswith('ayy'.lower()):
            await message.channel.send('lmao')

client = CAMERAN()
client.run(token)