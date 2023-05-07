import discord
from discord.ext import commands 
import nest_asyncio
nest_asyncio.apply() 

TOKEN = "your_token"

intents = discord.Intents.default()
intents.guild_messages = True
intents.reactions = True
intents.message_content = True
bot = commands.Bot(command_prefix = "/", intents = intents)

message = None

@bot.command()
@commands.has_role('Admin')
async def start_poll(ctx, question):
    options = ["🤔 Abstain", "👍 Yes", "👎 No"] 
    embed = discord.Embed(title=question, description='\n'.join([f"{i+1}. {option}" for i, option in enumerate(options)]))
    message = await ctx.send(embed=embed)
    for i in range(3):
        await message.add_reaction(options[i][0])
    await bot.process_commands(message)

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
    options = ["🤔 Abstain", "👍 Yes", "👎 No"]
    results = [0, 0, 0]
    for reaction in message.reactions:
        index = options.index(str(reaction.emoji) + " " + options[index])
        results[index] = reaction.count - 1
        
    summary = discord.Embed(title="Voting Results", description=f"Results for {message.embeds[0].title}:\n\nAbstain: {results[0]}\nYes: {results[1]}\nNo: {results[2]}")
    await ctx.send(embed=summary)
    message = None 

bot.run(TOKEN)

