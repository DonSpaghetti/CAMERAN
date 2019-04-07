import json
import requests
import random
from operator import itemgetter


# r = requests.get(url='http://content.warframe.com/dynamic/worldState.php')

# pprint.pprint(r.json())

class Warframe:

    async def cetus(url):
        url = json.loads(requests.get(url="https://api.warframestat.us/pc/cetusCycle").content)
        # r = json.loads(requests.get(url='https://drops.warframestat.us/data/all.json').text)
        return url['shortString']

    async def nightwave(url):# WIP - will just give a basic list of what's new this week.
        what_they_want = []
        x = 0
        url = json.loads(requests.get(url="https://api.warframestat.us/pc/nightwave").content)
        missions = len(url['activeChallenges'])
        mission = 0
        while mission < missions:
            quest = url['activeChallenges'][mission]
            what_they_want.append({mission : quest['desc']})
            mission = mission+1
        return str(what_they_want)

    async def randomWar(url):
        url = json.loads(requests.get(url='https://ws.warframestat.us/warframes').text)
        xFrame = random.randint(0, len(url))
        frameName = url[xFrame]['name']
        url = json.loads(requests.get(url='https://ws.warframestat.us/weapons').text)
        xWeapon = random.randint(0, len(url))
        weaponName = url[xWeapon]['name']
        randChance = "Use " + frameName + " with the weapon " + weaponName + "!"
        
        return randChance
    
    async def randomFrame(url):
        url = json.loads(requests.get(url='https://ws.warframestat.us/warframes').text)
        xFrame = random.randint(0, len(url))
        frameName = url[xFrame]['name']
        randChance = "Use " + frameName + " this mission!"
        
        return randChance
    
    async def randomWeapon(url):
        url = json.loads(requests.get(url='https://ws.warframestat.us/weapons').text)
        xWeapon = random.randint(0, len(url))
        weaponName = url[xWeapon]['name']
        randChance = "Use the weapon " + weaponName + "!"
        
        return randChance
    
    async def bestPriceFor(url):
        sortList = []
        sortedList = []
        x = 0
        
        for pl in url['payload']['orders']:
            userName = pl['user']['ingame_name']
            itemPrice = pl['platinum']
            lastSeen = pl['user']['status']
            orderType = pl['order_type']
            # sentence = userName + " was last seen as" + lastSeen + ". He is selling " + item + " for " + str(itemPrice) + "."
            if (lastSeen == 'ingame' and orderType == 'sell'):
                jsonPayload = {'Username': userName,
                               'Price': itemPrice,
                               }
                sortList.append(jsonPayload)
                sortedList = sorted(sortList, key=itemgetter('Price'))
                x = x + 1
        
        return str(sortedList[:5])
