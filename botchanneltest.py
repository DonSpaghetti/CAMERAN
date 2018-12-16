from discord.ext.commands import Bot
import asyncio
import logging
import random
import requests
import discord
import json

logging.basicConfig(level=logging.INFO)
client = discord.Client()
Dankbot420 = Bot(description="Dankbot420 - Meme Master - Bot by DonSpaghetti and Goldstorm", command_prefix="d$",
                 pm_help=False)


@Dankbot420.command()
async def dankbots():
    """
    The bots are taking over!!
    """
    msg = ("https://i.imgur.com/9oVJfnm.png" + "\nTHIS IS A TEST OF THE EMERGENCY DANKBOT MEME SYSTEM..."
                         + "\nLOUD! BEEPING! NOISES!")
    await Dankbot420.say(msg)
    await asyncio.sleep(1)


@Dankbot420.command()
async def why():
    """
    WHY WON'T THE CODE WORK?!?!
    :return:
    """
    await Dankbot420.say("https://i.kym-cdn.com/photos/images/newsfeed/000/821/232/4c5.gif")
    await asyncio.sleep(1)


@Dankbot420.command()
async def bball(*args):
    """
    Sports people have the best reactions; a random selection
    """
    possible_responses = [
        'https://i.imgur.com/joDXg0B.gif',
        'https://i.imgur.com/9CzeQmB.jpg',
        'https://media.giphy.com/media/3o7bu8K1BVxUEUIXyU/giphy.gif',
    ]
    await Dankbot420.say(random.choice(possible_responses))
    await asyncio.sleep(1)


@Dankbot420.command()
async def confus(*args):
    """
    Randomly express your befuddlement
    """
    possible_responses = [
        'https://i.kym-cdn.com/photos/images/original/000/012/974/cat_im_confus20110724-22047-q16ber.jpg',
        'https://media.giphy.com/media/l3q2K5jinAlChoCLS/200w.gif',
        'https://media1.tenor.com/images/5b034e96d84c6c6b57a9a04ca14aac02/tenor.gif',
        'https://media1.tenor.com/images/4cb306a83b1b41da055f47a8071a1934/tenor.gif',
    ]
    await Dankbot420.say(random.choice(possible_responses))
    await asyncio.sleep(1)

# Experimental weatherbot5000 - pull from API? - Make comments based on temperature for each location #


@Dankbot420.command()
async def weather(*, temp: str):  # 11/25/18; it's garbage fix everything #
    """
    OH YOU THINK YOU'VE GOT BAD WEATHER YOU SHOULD SEE THE WEATHER IN MY LOCATION
    """
    url = json.loads(requests.get(url='api.openweathermap.org/data/2.5/weather?q=Baltimore,us&APPID=e527cd8c21edada01ca57844a9ec492b' + temp).text)
    temp1 = url['temps'][0]['temp']

    await Dankbot420.say(temp1)
    await asyncio.sleep(1)

# End experimental weatherbot5000 #


# Experimental bartender5000 - still needs work but getting there #


@Dankbot420.command()
async def drincc(*, drink: str):
    """
    Booze recipes
    """
    url = json.loads(requests.get(url='https://www.thecocktaildb.com/api/json/v1/1/search.php?s=' + drink).text)
    if url['drinks'] == None:
        await Dankbot420.say("404 Drink not found, please try again")
    else:
        drinkinstructions = url['drinks'][0]['strInstructions']

        drinkingredient1 = url['drinks'][0]['strIngredient1']    # Hi.
        drinkingredient2 = url['drinks'][0]['strIngredient2']    # I promise I'm not a madman.
        drinkingredient3 = url['drinks'][0]['strIngredient3']    # There's probably an easier way to do this.
        drinkingredient4 = url['drinks'][0]['strIngredient4']    # However, I'm not clever enough to think of it.
        drinkingredient5 = url['drinks'][0]['strIngredient5']    # Maybe in the future, I'll figure something out.
        drinkingredient6 = url['drinks'][0]['strIngredient6']    # Right now, this works...
        drinkingredient7 = url['drinks'][0]['strIngredient7']    # ...ish
        drinkingredient8 = url['drinks'][0]['strIngredient8']    #
        drinkingredient9 = url['drinks'][0]['strIngredient9']    # I really appreciate you staying with me here
        drinkingredient10 = url['drinks'][0]['strIngredient10']  # You're a good listener!

        drinkmeasure1 = url['drinks'][0]['strMeasure1']          # ...
        drinkmeasure2 = url['drinks'][0]['strMeasure2']          # You deserve a haiku:
        drinkmeasure3 = url['drinks'][0]['strMeasure3']          #
        drinkmeasure4 = url['drinks'][0]['strMeasure4']          # What is with this code?
        drinkmeasure5 = url['drinks'][0]['strMeasure5']          # Oh my, looks like I wrote it
        drinkmeasure6 = url['drinks'][0]['strMeasure6']          # What was I thinking?
        drinkmeasure7 = url['drinks'][0]['strMeasure7']          #
        drinkmeasure8 = url['drinks'][0]['strMeasure8']          # ...I didn't even write that haiku
        drinkmeasure9 = url['drinks'][0]['strMeasure9']          # I just googled for it
        drinkmeasure10 = url['drinks'][0]['strMeasure10']        # =) top 10 anime betrayals

        ingredientlist = {drinkmeasure1 + drinkingredient1, drinkmeasure2 + drinkingredient2,
                          drinkmeasure3 + drinkingredient3, drinkmeasure4 + drinkingredient4,
                          drinkmeasure5 + drinkingredient5, drinkmeasure6 + drinkingredient6,
                          drinkmeasure7 + drinkingredient7, drinkmeasure8 + drinkingredient8,
                          drinkmeasure9 + drinkingredient9, drinkmeasure10 + drinkingredient10
                          }

        await Dankbot420.say(str(drinkinstructions))

        for x in ingredientlist:
            if x != "":  # should drop null values
                await Dankbot420.say(x)  # Attempt parse for rate limit in response headers?
        await asyncio.sleep(1)


# End Experimental bartender5000 #

@Dankbot420.command(pass_context=True)
async def madlibs(ctx):
    await Dankbot420.say("Please enter a noun")
    message = Dankbot420.wait_for_message(author=ctx.message.author, timeout=30)
    myvar = message.content
    await Dankbot420.say(f'I wish I had a purple {myvar}')
    await asyncio.sleep(1)


@Dankbot420.event
async def on_message(message):
    # Meme response based on keywords
    message.content = message.content.lower()

    if 'move to austin' in message.content:
        await Dankbot420.send_message(message.channel,
                                      'https://us.v-cdn.net/6025735/uploads/editor/88/lsb0v3uh7swy.gif')

    elif 'i like attack on titan' in message.content:
        await Dankbot420.send_message(message.channel, 'https://i.imgur.com/4dznW7t.png')

    elif 'good bot' in message.content:
        await Dankbot420.send_message(message.channel, 'arigato gozaimasu senpai <3 uwu')

    elif 'eat cheese live forever' in message.content:
        await Dankbot420.send_message(message.channel, 'EAT CHEESE NEVER DIE')

    elif 'drink seltzer live forever' in message.content:
        await Dankbot420.send_message(message.channel, 'DRINK SELTZER NEVER DIE')

    await Dankbot420.process_commands(message)

Dankbot420.run('NTA5ODg2ODY1OTEwNzkyMjA3.DsUVbQ.W85ta_FdBohwzpbCh2BJVMW4U6E')
