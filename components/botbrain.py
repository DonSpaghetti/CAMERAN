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
    async def cook(food):
        search = "http://www.foodnetwork.com/search/"
        food = food.replace(' ', '-')
        url = search + food + "-"
        with urllib.request.urlopen(url) as response:
            html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        hot_soup = soup.h3
        for link in hot_soup.find_all('a'):
            result = link.get('href')
        return ("http:" + result)
    
    async def rcat(url):
        url = json.loads(requests.get(url='http://aws.random.cat/meow').text)
        cat = url['file']
        return cat
    
    async def rdog(url):
        url = json.loads(requests.get(url='https://random.dog/woof.json').text)
        dog = url['url']
        return dog
    
    async def srdt(sbr):
        sub = BotBrain.reddit.subreddit(sbr)
        posts = [post for post in sub.hot(limit=100)]
        random_post_number = random.randint(0, len(posts) - 1)
        random_post = posts[random_post_number]
        return random_post.url