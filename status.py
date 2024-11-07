import discord
from client import client
import config

@client.event
async def on_ready():
    # xd
    if(config.activitytype=="PLAYING"):
        if(config.status=="DND"):
            await client.change_presence(status=discord.Status.dnd, activity=discord.Game(name=config.activitytext))
        elif(config.status=="IDLE"):
            await client.change_presence(status=discord.Status.idle, activity=discord.Game(name=config.activitytext))
        elif(config.status=="ONLINE"):
            await client.change_presence(status=discord.Status.online, activity=discord.Game(name=config.activitytext))
        elif(config.status=="INVISIBLE"):
            await client.change_presence(status=discord.Status.invisible)
    elif(config.activitytype=="STREAMING"):
        if(config.status=="DND"):
            await client.change_presence(status=discord.Status.dnd, activity=discord.Streaming(name=config.activitytext), url=config.streamingurl)
        elif(config.status=="IDLE"):
            await client.change_presence(status=discord.Status.idle, activity=discord.Streaming(name=config.activitytext), url=config.streamingurl)
        elif(config.status=="ONLINE"):
            await client.change_presence(status=discord.Status.online, activity=discord.Streaming(name=config.activitytext), url=config.streamingurl)
        elif(config.status=="INVISIBLE"):
            await client.change_presence(status=discord.Status.invisible)
    elif(config.activitytype=="WATCHING"):
        if(config.status=="DND"):
            await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name=config.activitytext))
        elif(config.status=="IDLE"):
            await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name=config.activitytext))
        elif(config.status=="ONLINE"):
            await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=config.activitytext))
        elif(config.status=="INVISIBLE"):
            await client.change_presence(status=discord.Status.invisible)
    elif(config.activitytype=="COMPETING"):
        if(config.status=="DND"):
            await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.competing, name=config.activitytext))
        elif(config.status=="IDLE"):
            await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.competing, name=config.activitytext))
        elif(config.status=="ONLINE"):
            await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.competing, name=config.activitytext))
        elif(config.status=="INVISIBLE"):
            await client.change_presence(status=discord.Status.invisible)
    elif(config.activitytype=="LISTENING"):
        if(config.status=="DND"):
            await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.listening, name=config.activitytext))
        elif(config.status=="IDLE"):
            await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.listening, name=config.activitytext))
        elif(config.status=="ONLINE"):
            await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name=config.activitytext))
        elif(config.status=="INVISIBLE"):
            await client.change_presence(status=discord.Status.invisible)
    elif(config.activitytype=="NONE"):
        if(config.status=="DND"):
            await client.change_presence(status=discord.Status.dnd)
        elif(config.status=="IDLE"):
            await client.change_presence(status=discord.Status.idle)
        elif(config.status=="ONLINE"):
            await client.change_presence(status=discord.Status.online)
        elif(config.status=="INVISIBLE"):
            await client.change_presence(status=discord.Status.invisible)