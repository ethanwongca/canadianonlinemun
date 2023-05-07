import discord
from discord.ext import commands
import nest_asyncio 
import time 
nest_asyncio.apply()

TOKEN = "your_token"

#Just in case some intents possibly needed 

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.guild_messages = True
intents.reactions = True
intents.message_content = True

bot = commands.Bot(command_prefix = "/", intents = intents)

@bot.command()
@commands.has_role('Admin')
async def timer(ctx, seconds: int):
    embed = discord.Embed(title="Timer", description=f"{seconds} seconds", color=0x00ff00)
    message = await ctx.send(embed=embed)
    for i in range(seconds, 0, -1):
        embed.description = f"{i} seconds left"
        await message.edit(embed=embed)
        time.sleep(1)
    embed.description = "Time's up!"
    await message.edit(embed=embed)

bot.run(TOKEN)
