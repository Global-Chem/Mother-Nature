# Imports
# -------
import os
import re
import discord
import asyncio
import datetime
import textwrap
import pandas as pd
from discord.ext import commands
from discord.ext.commands import Bot

from github import Github
from dotenv import load_dotenv

# Defaults
# --------

list_commands = ["history: (int) year month day", "words", "commands", "help"]

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


channel = discord.utils.get(client.get_all_channels(), name='cannabis')

bot = commands.Bot(command_prefix='?', intents=intents)

@bot.command(name='history')
async def get_history(channel, year, month, day, include_mother_nature=False):
  msg = [message async for message in channel.history(after=datetime.datetime(year, month, day))]
  for text in msg:
    await channel.send(text.content)

@client.event
async def on_message(message):
  if message.author == "Mother Nature" or not message.content.startswith("!mn"):
    return
 
  words = message.content.split()

  if words[1] == "history":
    year = int(words[2])
    month = int(words[3])
    day = int(words[4])
    await get_history(message.channel, year, month, day)
  
  elif words[1] == "words":
    await message.channel.send(words)

  elif words[1] == "commands":
    for command in list_commands:
      await message.channel.send(command)
   
  

client.run(DISCORD_TOKEN)

