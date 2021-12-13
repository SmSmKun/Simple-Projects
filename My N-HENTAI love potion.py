import random
import os
import discord
import pyperclip
from bs4  import BeautifulSoup
import urllib.request
from urllib.request import Request, urlopen
from dotenv import load_dotenv
load_dotenv()
TOKEN = "blahblahblah"
client = discord.Client()

#saying HI
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

#start
@client.event
async def on_message(message):
    if message.author == client.user:
        return
#get the random dojin
    x = random.randrange(start = 0, stop = 380000)
    y = "https://nhentai.net/g/" + str(x)
#start soup using a broweser as n-hentai has bot firewall
    req = Request(y, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, "html.parser")
#open a txt file to save the upcoming links   
    wholestack = open('desktop/htmlcode.txt', 'w') 
#find only links with "img" tag and containing "scr" direct link
    for link in soup.findAll('img'):
         x = link.get('src')
#write them in separate lines in a file
         wholestack.writelines(x + '\n')
#open the file to search for the cover link
    wholestack = open('desktop/htmlcode.txt', 'r')
#starting a loop to search for a line contaiting "cover" in it
    for z in wholestack:
     if 'cover.jpg' in z:
#double check on the link
        print(z)
#copy link to clipboard
        pyperclip.copy(z)
#setting the command
    if message.content == '/nh':
#here we send the dojin link
       await message.channel.send(y)
#here we send the dojin cover
       await message.channel.send(pyperclip.paste())
#run
client.run(TOKEN)