import discord
from discord.ext import commands 
import nest_asyncio
nest_asyncio.apply() 

TOKEN = "MTA2ODk3NTI3MTkzMzM3ODY2MQ.GkDC-B.Fm6M42DuyPNHKnsG0MlMA_vn7ZzjzcGDndMKw0"

intents = discord.Intents.default()
intents.guild_messages = True
intents.reactions = True
intents.message_content = True
bot = commands.Bot(command_prefix = "/", intents = intents) # Sets the prefix for bots command 

@bot.command()
@commands.has_role('Admin') #Admins can use this
async def start_poll(ctx, question): #Abstain, For, Against
    options = ["Abstain", "Yes", "No"] 
    # Allows for the message to go through         
    embed = discord.Embed(title=question, description='\n'.join([f"{i+1}. {option}" for i, option in enumerate(options)]))
    #Waiting for the message to send 
    message = await ctx.send(embed = embed)
    for i in range(3):
        await message.add_reaction(chr(0x31 + i))

@bot.command()
@commands.has_role('Admin')
async def end_poll(ctx):
    global message
    if message is None:
        await ctx.send("No one voted")
        return 
    try:
        message = await message.channel.fetch_message(message.id)
    except discord.NotFound:
        await ctx.send("Poll message not found")
        return
    options = ["Abstain", "Yes", "No"]
    results = [0, 0, 0]
    for reaction in message.reactions:
        index = ord(str(reaction.emoji)) - 0x31
        results[index] = reaction.count - 1
        
    summary = discord.Embed(title = "Voting Results", description = f"Results for {message.embeds[0].title}:\n\nAbstain: {results[0]}\nYes: {results[1]}\nNo: {results[2]}")
    await ctx.send(embed = summary)
    message = None 

bot.run(TOKEN)
