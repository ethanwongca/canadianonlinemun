#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import discord 
import nest_asyncio
nest_asyncio.apply()

TOKEN = 'MTA2MzYwMzIzMzkxMTc0MjUyNQ.GGDN5u.KwZeJfZuwYhRETGFO-e5ohtUhcxhEbo9kgSVnA'

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents = intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    
welcome_message = "Welcome to Canadian Online Model United Nations! "
                    
@client.event
async def on_member_join(member):
    channel = member.guild.system_channel
    await channel.send(welcome_message)

client.run(TOKEN)