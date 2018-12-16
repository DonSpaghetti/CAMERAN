import discord
from discord.ext import commands
import asyncio
import random
from components.botbrain import BotBrain
from components.warframe import Warframe
import uuid
from datetime import datetime


description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''
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

# CAMERAN on_message custom functions.
@bot.event
async def on_message(message):
    log = open('log.txt', 'w')
    # we do not want the bot to reply to itself
    if message.author.id == bot.user.id:
        return
    if message.author.id == bot.user.id:
        return
    elif message.content.startswith('lmao'.lower()):
        await message.channel.send('ayy')
    elif message.content.startswith('ayy'.lower()):
        await message.channel.send('lmao')
    if message.content.startswith('hello'):
        await message.channel.send('Hello {0.author.mention}'.format(message))
    
    print(f"{message.channel}, {message.author}, {message.author.name}, {message.content}", file=open(filename, 'a'))

    await bot.wait_until_ready()
    await bot.process_commands(message)

token = BotBrain.secrets['CAMERANToken']
bot.run(token)