import json
from discord import Object
from bs4 import BeautifulSoup
import urllib.request
import re
import asyncio
import random
import requests
import praw


class BotBrain():
    secrets = json.load(open('components/supersecretfiletopconfidential.json', 'r'))
    reddit = praw.Reddit(client_id=secrets['RedditId'],
                         client_secret=secrets['RedditSecret'],
                         password=secrets['RedditPassword'],
                         user_agent='testscript by /u/Goldstorm',
                         username='SomaBot')
    
    print(str(reddit.user.me()) + ' has made a successful connection to Reddit!')
    
    # room numbers
    swr = Object(id='195577376812433408')
    bs = Object(id='193787360071254018')
    nl = Object(id='313166514524258304')
    flavor = Object(id='265627071718359040')
    art = Object(id='318607996454436874')
    lol = Object(id='332269522524438529')
    war = Object(id='352212926477631489')
    nsfw = Object(id='194616310682877952')
    holes = Object(id='320388745092399105')
    gameru = Object(id='363477346784903168')
    
    # for the %cook command
    async def cook(fud: str):
        result = ''
        search = "http://www.foodnetwork.com/search/"
        food = fud.replace(' ', '-')
        url = search + food + "-"
        with urllib.request.urlopen(url) as response:
            html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        hot_soup = soup.h3
        for link in hot_soup.find_all('a'):
            result = link.get('href')
        return ("http:" + result)
    
    
    #for the $confus command
    async def anconfus(self):
        ion = [
        'https://i.kym-cdn.com/photos/images/original/000/012/974/cat_im_confus20110724-22047-q16ber.jpg',
        'https://media.giphy.com/media/l3q2K5jinAlChoCLS/200w.gif',
        'https://media1.tenor.com/images/5b034e96d84c6c6b57a9a04ca14aac02/tenor.gif',
        'https://media1.tenor.com/images/4cb306a83b1b41da055f47a8071a1934/tenor.gif',
        ]
        reply = (random.choice(ion))
        return reply
    
    async def drincc(url):
        z = 0
        y = 1
        drinkLength = len(url['drinks'])
        Drinktionary = {}
        for x in range(drinkLength):
            drinkinstructions = url['drinks'][x]['strInstructions']
            drinkName = url['drinks'][x]['strDrink']
            drinkImage = url['drinks'][x]['strDrinkThumb']
            drinkIL = []
            drinkMS = []
            drinkILMS = []
            Drink = {}
            while y <= 15:
                if (url['drinks'][x]['strIngredient' + str(y)] is '') or (
                        url['drinks'][x]['strIngredient' + str(y)] is ' ') or (
                        url['drinks'][x]['strIngredient' + str(y)] is None):
                    y = y + 1
                else:
                    drinkMS.append(url['drinks'][x]['strMeasure' + str(y)])
                    drinkIL.append(url['drinks'][x]['strIngredient' + str(y)])
                    drinkILMS.append(drinkMS[z] + " " + drinkIL[z])
                    y = y + 1
                    z = z + 1
                Drink = { "Drink " + str(x) : drinkName,
                          "Drink " + str(x) + " Instructions": drinkinstructions,
                          "Drink " + str(x) + " Ingredients": drinkILMS,
                          "Drink " + str(x) + " Image" : drinkImage,
                          "Drink Length" : drinkLength,
                         }
            Drinktionary.update(Drink)
            y = 1
            z = 0
        return Drinktionary

    async def rdog(self):
        url = json.loads(requests.get(url='https://random.dog/woof.json').text)
        dog = url['url']
        return dog
    
    async def srdt(sbr):
        sub = BotBrain.reddit.subreddit(sbr)
        posts = [post for post in sub.hot(limit=100)]
        random_post_number = random.randint(0, len(posts) - 1)
        random_post = posts[random_post_number]
        return random_post.url
    
    async def getDrinks(drinks: str):
        alcohol = json.loads(requests.get(url='https://www.thecocktaildb.com/api/json/v1/1/filter.php?a=Alcoholic').text)
        noAlcohol = json.loads(requests.get(url='https://www.thecocktaildb.com/api/json/v1/1/filter.php?a=Non_Alcoholic').text)
        with open('components/drinks/alcoholic.json', 'w') as f:
            json.dump(alcohol, f, indent=4, sort_keys=True)
            f.close()
        with open('components/drinks/non_alcoholic.json', 'w') as f:
            json.dump(noAlcohol, f, indent=4, sort_keys=True)
            f.close()
        
        return 'Drinks Ordered!'