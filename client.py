import discord
import config


intents = discord.Intents.all()
client = discord.Bot(intents=intents, fetch_offline_members=True, sync_commands=True)