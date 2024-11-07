import discord
from client import client
import config
import os

@client.slash_command()
async def cache(ctx):
    """Clear cached capes folder"""
    listdir = os.listdir('cached_capes')
    for images in listdir:
        if images.endswith(".png"):
            os.remove(os.path.join('cached_capes', images))
    files = len(listdir) - 1
    embed = discord.Embed(title="✅ Success!", colour=discord.Colour(config.embedcolor), description=f"Successfully cleared `{files}` files!")
    embed.set_thumbnail(url=config.embedthumbnail)
    embed.set_footer(text=config.embedfootertext, icon_url=config.embedfootericon)
    await ctx.response.send_message(embed=embed, ephemeral=True)
    return