import discord
from discord.ext import commands
import asyncio
import random
import components

description = '''Master Masquerader! Messenger of Memes! CAMERAN!'''
bot = commands.Bot(command_prefix='$', description=description)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def confus(ctx):
    """
    Randomly express your befuddlement.
    """
    reply = await components.anconfus()
    await ctx.send(reply)


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


@bot.group()
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send('No, {0.subcommand_passed} is not cool'.format(ctx))


@bot.command()
async def dankbots(ctx):
    """
    The bots are taking over!!
    """
    msg = ("https://i.imgur.com/9oVJfnm.png" + "\nTHIS IS A TEST OF THE EMERGENCY DANKBOT MEME SYSTEM..."
           + "\nLOUD! BEEPING! NOISES!")
    await ctx.send(msg)
    await asyncio.sleep(1)


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

    await bot.wait_until_ready()
    await bot.process_commands(message)

token = open('token.txt', 'r').read()
bot.run(token)
