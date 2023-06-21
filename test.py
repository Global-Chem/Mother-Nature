# Imports
# -------
import os
import re
import discord
import asyncio
import textwrap
import pandas as pd
from discord.ext import commands
from discord.ext.commands import Bot

from github import Github
from dotenv import load_dotenv

# Defaults
# --------

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


channel = discord.utils.get(client.get_all_channels(), name='cannabis')

bot = commands.Bot(command_prefix='?', intents=intents)

async def which_func(message):
  await get_history(message)

@bot.command(name='history')
async def get_history(message):
  await message.channel.send("test worked")

@client.event
async def on_message(message):
 if message.author == client.user:
   return
 
 if message.content.startswith("!mn"):
   await which_func(message)

client.run(DISCORD_TOKEN)

