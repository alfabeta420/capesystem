import discord
from client import client
import config
import asyncio

@client.event
async def on_message(ctx):
    if ctx.author.bot:
        return
    if (ctx.channel.id == config.registerchannelid):
        await asyncio.sleep(0.1)
        await ctx.delete()
    if (ctx.channel.id == config.capechannelid):
        await asyncio.sleep(0.1)
        await ctx.delete()