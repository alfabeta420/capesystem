import discord
import sqlite3
from client import client
import config
from os.path import exists

@client.slash_command()
async def cape(ctx, id):
    """Change your cape"""
    if(ctx.channel.id != config.capechannelid):
        embed = discord.Embed(title="❌ Error!", colour=discord.Colour(config.embedcolor), description=f"You used the `/cape` command in wrong channel!\nTry here: <#{config.capechannelid}>")
        embed.set_thumbnail(url=config.embedthumbnail)
        embed.set_footer(text=config.embedfootertext, icon_url=config.embedfootericon)
        await ctx.response.send_message(embed=embed, ephemeral=True)
        return
    if(id.isnumeric() == False):
        embed = discord.Embed(title="❌ Error!", colour=discord.Colour(config.embedcolor), description=f"The cape id has to be a number! ex. 3 or 8")
        embed.set_thumbnail(url=config.embedthumbnail)
        embed.set_footer(text=config.embedfootertext, icon_url=config.embedfootericon)
        await ctx.response.send_message(embed=embed, ephemeral=True)
        return
    connection = sqlite3.connect('db.db')
    cursor = connection.cursor()
    cape = cursor.execute(f"SELECT cape FROM users WHERE id = {ctx.author.id}").fetchone()
    
    fileexists = exists(f'capes/{id}.png')
    if(cape != None):
        if(fileexists):
            cursor.execute(f'UPDATE users SET cape = {id} WHERE id = {ctx.author.id}')
            nick = cursor.execute(f"SELECT nick FROM users WHERE id = {ctx.author.id}").fetchone()
            nick = nick[0]
            connection.commit()
            connection.close()
            print(f'User {ctx.author} ({ctx.author.id}) changed the cape to {id} for {nick}')
            embed = discord.Embed(title="✅ Success!", colour=discord.Colour(config.embedcolor), description=f"Set the cape successfully!\nID: `{id}`")
            embed.set_thumbnail(url=f"https://mc-heads.net/head/{nick}")
            embed.set_footer(text=config.embedfootertext, icon_url=config.embedfootericon)
            await ctx.response.send_message(embed=embed, ephemeral=True)
        else:
            embed = discord.Embed(title="❌ Error!", colour=discord.Colour(config.embedcolor), description=f"This cape doesn't exist!\nTry a cape listed here: <#{config.capelistchannelid}>")
            embed.set_thumbnail(url=config.embedthumbnail)
            embed.set_footer(text=config.embedfootertext, icon_url=config.embedfootericon)
            await ctx.response.send_message(embed=embed, ephemeral=True)
    else:
        embed = discord.Embed(title="❌ Error!", colour=discord.Colour(config.embedcolor), description=f"You are not registered!\nRegister here: <#{config.registerchannelid}>")
        embed.set_thumbnail(url=config.embedthumbnail)
        embed.set_footer(text=config.embedfootertext, icon_url=config.embedfootericon)
        await ctx.response.send_message(embed=embed, ephemeral=True)