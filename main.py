import re
import requests
import math
from bs4 import BeautifulSoup
from minion import Minion

allminions = []

def initializeminions():
    with open("miniondata", "r") as file:
        while True:
            lines = [file.readline() for _ in range(4)]

            if not any(lines):
                break

            tempobj = Minion()
            subline = 0

            for line in lines:
                if line.strip():
                    if subline == 0 :
                        tempobj.miniontype = line.strip()
                    if subline == 1 :
                        tempobj.miniongreatestmaterial = line.strip()
                    if subline == 2 :
                        tempobj.minionspeed = line.strip()
                    if subline == 3:
                        tempobj.matmagnitude = line.strip()
                    subline += 1

            allminions.append(tempobj)
    return

def getcurrentmatprice(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    meta_tag = soup.find('meta', property='og:description')

    storage_string = ""
    price_string = ""

    if meta_tag:
        content = meta_tag.get('content')
        index = content.index("Instasell Price")
        storage_string = content[index + 17 : index + 27]

    for c in storage_string:
        if c.isdigit() or c == '.':
            price_string = price_string + c

    return price_string

def calcprofit():
    for m in allminions:
        url = "https://www.skyblock.bz/product/" + m.miniongreatestmaterial
        price = float(getcurrentmatprice(url))
        production = ((86400 / (2 * float(m.minionspeed))) / (160 ** int(m.matmagnitude)))
        profit = math.floor(price * production)
        print("Daily " + m.miniontype + " raw material profit is: " + str(profit))
    return

initializeminions()
calcprofit()
#dispallminions()