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

@bot.command()
@commands.has_permissions(manage_roles=True)
async def setup(ctx):
    guild = ctx.guild
    # Insert the committees that you want
    committees = ["WHO", "UNSC", "UNHCR"] 
    for committee in committees:
        await guild.create_role(name=committee)
    await ctx.send("Committee roles are implemented. React to this message to assign yourself a committee role.")
    
    # Send the message to the general channel
    general_channel = discord.utils.get(guild.channels, name="general")
    message = await general_channel.send("React to this message to assign yourself a committee role.")
    await message.add_reaction('🩺')
    await message.add_reaction('🔒')
    await message.add_reaction('🛃')

@bot.event 
async def on_ready():
    print(f"{bot.user.name} is present and voting")

@bot.event
async def on_reaction_add(reaction, user):
    guild = reaction.message.guild
    member = guild.get_member(user.id)
    #This subsection just insert for more committees or delete for other committes
    if reaction.emoji == '🩺':
        role = discord.utils.get(guild.roles, name='WHO')
        await member.add_roles(role)
        await reaction.message.channel.send(f'Added {member.name} to {role.name} committee.')
    elif reaction.emoji == '🔒':
        role = discord.utils.get(guild.roles, name='UNSC')
        await member.add_roles(role)
        await reaction.message.channel.send(f'Added {member.name} to {role.name} committee.')
    elif reaction.emoji == '🛃':
        role = discord.utils.get(guild.roles, name='UNHCR')
        await member.add_roles(role)
        await reaction.message.channel.send(f'Added {member.name} to {role.name} committee.')

bot.run(TOKEN)
