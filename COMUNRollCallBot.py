import discord
from discord.ext import commands 
import nest_asyncio
nest_asyncio.apply() 

TOKEN = "your_token"

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.guild_messages = True
intents.reactions = True
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)


@bot.command(name='rollcall')
async def rollcall(ctx, *, status: str = None):
    if not status and not ctx.author.guild_permissions.administrator:
        await ctx.send("You must be an administrator to start a roll call without a status.")
        return
    
    if status and status.lower() not in ('present', 'present and voting'):
        await ctx.send("Invalid status. Please use 'present' or 'present and voting'.")
        return
    
    if not status:
        status = 'present and voting'
    
    # List of members on the server
    members = ctx.guild.members
    
    # Filters out the bots
    members = filter(lambda member: not member.bot, members)
    
    # Send a message to each member regarding status
    for member in members:
        await ctx.send(f"{member.mention}, please respond with your status: {status}")
        
        # Checking members response
        def check(message):
            return message.author == member and message.channel == ctx.channel
        
        try:
            response = await bot.wait_for('message', check=check, timeout=60.0)
        except nest_asyncio.TimeoutError:
            await ctx.send(f"{member.mention} did not respond.")
        else:
            if response.content.lower() == status.lower():
                await ctx.send(f"{member.mention} is {status}.")
            else:
                await ctx.send(f"{member.mention} responded with an incorrect status.")
                
bot.run(TOKEN)



