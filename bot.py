from discord.ext import commands

import os
import discord
import asyncio
import random
import re
import json
import requests

from components.botbrain import BotBrain
from components.warframe import Warframe
from datetime import datetime

bot = commands.Bot(command_prefix=('$', '%', 'd$'), description='''Master Masquerader! Messenger of Memes! CAMERAN!''')


if os.name == 'nt': # Windows
    filename = 'C:\\logs\\log' + str(datetime.now()) + '.txt'
else: # Not Windows
    filename = 'models/logs/log' + str(datetime.now()) + '.txt'

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    # await BotBrain.getDrinks('')
    # print(await BotBrain.getDrinks(''))
    print('------')
    
@bot.command(aliases=['marshalls-fucking-dice-roll-command'])
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

# Dankbot420 Commands - The following commands are programmed and created by DonSpaghetti
@bot.command(aliases=['emily', 'ping'])
async def dankbots(ctx):
    """
    The bots are taking over!!
    """
    msg = ("https://i.imgur.com/9oVJfnm.png" + "\nTHIS IS A TEST OF THE EMERGENCY DANKBOT MEME SYSTEM..."
           + "\nLOUD! BEEPING! NOISES!")
    await ctx.send(msg)
    await asyncio.sleep(1)

@bot.command(aliases=['confused', 'fucking-what'])
async def confus(ctx):
    """
    Randomly express your befuddlement.
    """
    reply = await BotBrain.anconfus('')
    await ctx.send(reply)

@bot.command(aliases=['drink', 'margaritaville'])
async def drincc(ctx, *drink: str):
    """
    Booze recipes
    """
    mixedDrink = ' '.join(drink)

    y = 0
    if mixedDrink == '':
        await ctx.send("You spilled your drink.")
        return

    url = json.loads(requests.get(url='https://www.thecocktaildb.com/api/json/v1/1/search.php?s=' + mixedDrink).text)

    if url['drinks'] == None:
        await ctx.send("404 Drink not found, please try again.")

    else:
        Drinktionary = await BotBrain.drincc(url=url)
        dLength = int(Drinktionary['Drink Length'])
        # I returned more than one drink. Here's a drink menu. But I'll also return Drink 0 as well.
        if dLength > 1:
            drinkString = ''
            for x in range(dLength):
                drinkString += str(Drinktionary['Drink ' + str(x)]) + '\n'
            embed = discord.Embed(title="Drink Menu", value=str(dLength) + ' Drinks', color=0xff69B4)
            embed.add_field(name="I returned these " + str(dLength) + ' Drinks', value=drinkString, inline=False)
            embed.set_thumbnail(url="https://i.imgur.com/XjYRDV1.png")
            await ctx.send(embed=embed)
            await asyncio.sleep(1)

            await ctx.send("I'll return the first drink in the list, maybe you wanted that.")
            await asyncio.sleep(1)

            ingredientString = ''
            drinkIngredients = list(Drinktionary["Drink 0 Ingredients"])
            for x in range(len(drinkIngredients)):
                ingredientString += str(drinkIngredients[x]) + '\n'
            embed = discord.Embed(title=str(Drinktionary['Drink 0']), value=str(Drinktionary['Drink 0']), color=0xff69B4)
            embed.add_field(name="Instructions", value=str(Drinktionary['Drink 0 Instructions']), inline=False)
            embed.add_field(name="Ingredients", value=ingredientString, inline=False)
            embed.set_thumbnail(url=str(Drinktionary["Drink 0 Image"]))
            await ctx.send(embed=embed)
            await asyncio.sleep(1)
        
        else: # originally designed to return all drinks, will just return one now.
            ingredientString = ''
            drinkIngredients = list(Drinktionary["Drink " + str(y) + " Ingredients"])
            for x in range(len(drinkIngredients)):
                ingredientString += str(drinkIngredients[x]) + '\n'
            embed = discord.Embed(title=str(Drinktionary['Drink '+ str(y)]), value=str(Drinktionary['Drink '+ str(y)]), color=0xff69B4)
            embed.add_field(name="Instructions", value=str(Drinktionary["Drink " + str(y) + " Instructions"]), inline=False)
            embed.add_field(name="Ingredients", value=ingredientString, inline=False)
            embed.set_thumbnail(url=str(Drinktionary["Drink " + str(y) + " Image"]))
            await ctx.send(embed=embed)
            y = y + 1

        await asyncio.sleep(1)

# Soma2.0 Commands - the following code / commands are programmed and created by Goldstorm
@bot.command(aliases=['reddit', 'subreddit'])
async def sr(ctx, sbr: str):
    '''
    Searches for a random image in the specified subreddit
    '''
    sbrPic = await BotBrain.srdt(sbr)
    await ctx.send(sbrPic)
    await asyncio.sleep(1)
    
@bot.command(aliases=['cook', 'shokugeki'])
async def food(ctx, *food: str):
    '''
    Searches foodnetwork.com for specified recipe
    '''
    food = ' '.join(food)
    msg = BotBrain.cook(fud=food)
    await ctx.send(msg)
    await asyncio.sleep(1)
    
@bot.command(aliases=['warframe'])
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

@bot.command(aliases=['warframe-market', 'warmarket', 'market'])
async def wfmarket(ctx, *item: str):
    '''
    Returns the top 5 prices from the searched item.
    '''
    item = ' '.join(item)
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
    
@bot.command(aliases=['kitty', 'superior-creature', 'not-dog', 'meow'])
async def cat(ctx):
    '''
    A random cat
    '''
    url = json.loads(requests.get(url='http://aws.random.cat/meow').text)
    await ctx.send(url['file'])
    await asyncio.sleep(1)

@bot.command(aliases=['dog', 'woof'])
async def awoo(ctx):
    '''
    A random inferior creature
    '''
    url = json.loads(requests.get(url='https://random.dog/woof.json').text)
    await ctx.send(url['url'])
    await asyncio.sleep(1)

# CAMERAN on_message custom functions
@bot.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author.id == bot.user.id:
        return
    # Taking out until we can specifically tell it who to do this to.
    # if message.content.startswith('lmao'.lower()):
    #     await message.channel.send('ayy')
    #
    # elif message.content.startswith('ayy'.lower()):
    #     await message.channel.send('lmao')

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

bot.run(BotBrain.secrets['CAMERANToken'])
