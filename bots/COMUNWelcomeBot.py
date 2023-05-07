import discord 
# Allows async to work
import nest_asyncio
nest_asyncio.apply()

TOKEN = 'your_token'

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    
welcome_message = "Welcome to Canadian Online Model United Nations! "
                    
@client.event
async def on_member_join(member):
    channel = member.guild.system_channel
    await channel.send(welcome_message)

client.run(TOKEN)
