import discord
from discord.ext import commands
import asyncio
import random
import re
import json
import requests

from components.botbrain import BotBrain
from components.warframe import Warframe
from datetime import datetime


description = '''Master Masquerader! Messenger of Memes! CAMERAN!'''

bot = commands.Bot(command_prefix=('$', '%', 'd$'), description=description)
filename = 'models/logs/log' + str(datetime.now()) + '.txt'

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

#The following two commands are examples from the discord.py rewrite - will be expanded upon later.
@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

#Dankbot420 Commands
@bot.command()
async def dankbots(ctx):
    """
    The bots are taking over!!
    """
    msg = ("https://i.imgur.com/9oVJfnm.png" + "\nTHIS IS A TEST OF THE EMERGENCY DANKBOT MEME SYSTEM..."
           + "\nLOUD! BEEPING! NOISES!")
    await ctx.send(msg)
    await asyncio.sleep(1)

@bot.command()
async def confus(ctx):
    """
    Randomly express your befuddlement.
    """
    reply = await components.anconfus()
    await ctx.send(reply)
    

#Soma2.0 Commands
@bot.command()
async def sr(ctx, sbr: str):
    '''
    Searches for a random image in the specified subreddit
    '''
    sbrPic = await BotBrain.srdt(sbr)
    await ctx.send(sbrPic)
    await asyncio.sleep(1)
    
@bot.command()
async def food(ctx, food: str):
    '''
    Searches foodnetwork.com for specified recipe
    '''
    msg = BotBrain.cook(food)
    await ctx.send(msg)
    await asyncio.sleep(1)
    
@bot.command()
async def war(ctx, subCommand: str):
    '''
    Command to get Warframe data. %help war for a list of sub commands.
    %war cetus - Returns if it's Day or Night in Cetus.
    %war alerts - Returns current list of alerts. (WIP)
    %war chance - Are you feeling lucky?
    '''

    try:
        subCommand
    except discord.ext.commands.errors.MissingRequiredArgument:
        await ctx.send("This isn't a valid command. Do you expect me to work using this?")
        await asyncio.sleep(1)

    if subCommand.lower() == "cetus":
        subCommand = await Warframe.cetus('')
        await ctx.send(subCommand)
        await asyncio.sleep(1)
    elif subCommand.lower() == "alerts":
        subCommand = await Warframe.alerts('')
        await ctx.send(subCommand)
        await asyncio.sleep(1)
    elif subCommand.lower() == "weapon":
        subCommand = await Warframe.randomWeapon('')
        await ctx.send(subCommand)
        await asyncio.sleep(1)
    elif subCommand.lower() == "frame":
        subCommand = await Warframe.randomFrame('')
        await ctx.send(subCommand)
        await asyncio.sleep(1)
    elif subCommand.lower() == "chance":
        subCommand = await Warframe.randomWar('')
        await ctx.send(subCommand)
        await asyncio.sleep(1)
    else:
        await ctx.send("This isn't a valid command. Do you expect me to work using this?")
        await asyncio.sleep(1)

@bot.command()
async def wfmarket(ctx, item: str):
    '''
    Returns the top 5 prices from the searched item.
    '''
    itemOriginal = item
    itemMod = item.replace(' ', '_')
    itemModLow = itemMod.lower()
    itemUrl = 'http://api.warframe.market/v1/items/' + itemModLow + '/orders'
    itemLoad = requests.get(url=itemUrl)
    if itemLoad.status_code == 404:
        await ctx.send("This isn't a valid item. You expect me to serve food using this?")

    else:
        # I was high when i did this. Sorry. (> )>
        x = 0
        y = 0
        top5 = []
        itemLoad = itemLoad.text
        url = json.loads(itemLoad)
        item = await Warframe.bestPriceFor(url)
        itemList = re.split("{|}", item)
        while x < len(itemList):
            top5.append(itemList[x])
            x = x + 1
        t5str = str(top5)
        tSub5str = re.sub("[\"/!@#$':]", '', t5str)
        t5fix = tSub5str.replace("[[, ", "").replace(", ]]", "")
        top10 = list(t5fix.split(","))
        embed = discord.Embed(title="Top 5", description="Top 5 Prices for " + itemOriginal, color=0xff69B4)

        while y < len(top10):
            embed.add_field(name=str(top10[y].replace('Username ', '')), value=str(top10[y+1]), inline=False)
            y = y + 4

        await ctx.send(embed=embed)
    await asyncio.sleep(1)
    
@bot.command()
async def cat(ctx):
    '''
    A random cat
    '''
    cat = await BotBrain.rcat('')
    await ctx.send(cat + ' :ramen: おあがりよ!')
    await asyncio.sleep(1)

@bot.command()
async def awoo(ctx):
    '''
    A random inferior creature
    '''
    awoo = await BotBrain.rdog('')
    await ctx.send(awoo + ' :ramen: おあがりよ!')
    await asyncio.sleep(1)

# CAMERAN on_message custom functions
@bot.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author.id == bot.user.id:
        return

    if message.content.startswith('hello'):
        await message.channel.send('Hello {0.author.mention}'.format(message))

    elif message.content.startswith('lmao'.lower()):
        await message.channel.send('ayy')

    elif message.content.startswith('ayy'.lower()):
        await message.channel.send('lmao')

    elif 'move to austin' in message.content.lower():
        await message.channel.send('https://us.v-cdn.net/6025735/uploads/editor/88/lsb0v3uh7swy.gif')

    elif 'i like attack on titan' in message.content.lower():
        await message.channel.send('https://i.imgur.com/4dznW7t.png')

    elif 'good bot' in message.content.lower():
        await message.channel.send('arigato gozaimasu senpai <3 uwu')

    elif 'eat cheese live forever' in message.content.lower():
        await message.channel.send('EAT CHEESE NEVER DIE')

    elif 'drink seltzer live forever' in message.content.lower():
        await message.channel.send('DRINK SELTZER NEVER DIE')
    print(f"{message.channel}, {message.author}, {message.author.name}, {message.content}", file=open(filename, 'a'))


    await bot.wait_until_ready()
    await bot.process_commands(message)

token = BotBrain.secrets['CAMERANToken']
bot.run(token)
