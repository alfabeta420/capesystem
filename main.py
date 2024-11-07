import discord
from client import client
import config
import os

@client.event
async def on_ready():
    print('''

     Capesystem bot logged in.
   ->   Alfabeta.solutions   <-   



Logs:

    ''')

listdir = os.listdir('cached_capes')
for images in listdir:
    if images.endswith(".png"):
        os.remove(os.path.join('cached_capes', images))

import status
import commands.register
import commands.cape
import commands.cache
import deleter
import webserver

client.run(config.token)