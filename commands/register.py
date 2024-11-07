import discord
import sqlite3
from client import client
import config

@client.slash_command()
async def register(ctx, nick):
    """Register your Minecraft nickname"""
    if (ctx.channel.id != config.registerchannelid):
        embed = discord.Embed(title="❌ Error!", colour=discord.Colour(config.embedcolor), description=f"You used the `/register` command in wrong channel!\nTry here: <#{config.registerchannelid}>")
        embed.set_thumbnail(url=config.embedthumbnail)
        embed.set_footer(text=config.embedfootertext, icon_url=config.embedfootericon)
        await ctx.response.send_message(embed=embed, ephemeral=True)
        return
    connection = sqlite3.connect('db.db')
    cursor = connection.cursor()
    ifid = cursor.execute(f"SELECT id FROM users WHERE id = {ctx.author.id}").fetchone()
    ifnick = cursor.execute(f"SELECT nick FROM users WHERE nick = '{nick}'").fetchone()
    thisnick = cursor.execute(f"SELECT nick FROM users WHERE id = {ctx.author.id}").fetchone()
    if ifid == None:
        if ifnick == None:
            if((len(nick) > 2) and (len(nick)<17) and (nick.isalnum())):
                cursor.execute(f'INSERT INTO users VALUES ({ctx.author.id}, "{nick}", 0)')
                connection.commit()
                connection.close()
                print(f'User {ctx.author} ({ctx.author.id}) registered as {nick}')
                embed = discord.Embed(title="✅ Success!", colour=discord.Colour(config.embedcolor), description=f"Registered successfully!\nUser: `{nick}`")
                embed.set_thumbnail(url=f"https://mc-heads.net/head/{nick}")
                embed.set_footer(text=config.embedfootertext, icon_url=config.embedfootericon)
                await ctx.response.send_message(embed=embed, ephemeral=True)
            else:
                embed = discord.Embed(title="❌ Error!", colour=discord.Colour(config.embedcolor), description=f"Minecraft nickname has to be `3-16` characters and it has to be `alphanumeric`! Try again!")
                embed.set_thumbnail(url=config.embedthumbnail)
                embed.set_footer(text=config.embedfootertext, icon_url=config.embedfootericon)
                await ctx.response.send_message(embed=embed, ephemeral=True)
        else:
            if thisnick == None:
                embed = discord.Embed(title="❌ Error!", colour=discord.Colour(config.embedcolor), description=f"This user is already in our database!\nUser: `{nick}`")
                embed.set_thumbnail(url=f"https://mc-heads.net/head/{nick}")
                embed.set_footer(text=config.embedfootertext, icon_url=config.embedfootericon)
                await ctx.response.send_message(embed=embed, ephemeral=True)
            else:
                embed = discord.Embed(title="❌ Error!", colour=discord.Colour(config.embedcolor), description=f"You are already in our database!\nUser: `{thisnick[0]}`")
                embed.set_thumbnail(url=f"https://mc-heads.net/head/{thisnick[0]}")
                embed.set_footer(text=config.embedfootertext, icon_url=config.embedfootericon)
                await ctx.response.send_message(embed=embed, ephemeral=True)
    else:
        if thisnick == None:
                embed = discord.Embed(title="❌ Error!", colour=discord.Colour(config.embedcolor), description=f"This user is already in our database!\nUser: `{nick}`")
                embed.set_thumbnail(url=f"https://mc-heads.net/head/{nick}")
                embed.set_footer(text=config.embedfootertext, icon_url=config.embedfootericon)
                await ctx.response.send_message(embed=embed, ephemeral=True)
        else:
            embed = discord.Embed(title="❌ Error!", colour=discord.Colour(config.embedcolor), description=f"You are already in our database!\nUser: `{thisnick[0]}`")
            embed.set_thumbnail(url=f"https://mc-heads.net/head/{thisnick[0]}")
            embed.set_footer(text=config.embedfootertext, icon_url=config.embedfootericon)
            await ctx.response.send_message(embed=embed, ephemeral=True)