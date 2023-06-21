# Imports
# -------
import os
import re
import discord
import asyncio
import textwrap
import pandas as pd
from discord.ext import commands

from github import Github
from dotenv import load_dotenv

# Defaults
# --------

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
client.run(DISCORD_TOKEN)

channel = discord.utils.get(client.get_all_channels(), name='cannabis')

bot = commands.Bot(command_prefix='?', intents=intents)

@bot.command(name='history')
async def get_history(channel_object):
  msg = await discord.utils.get(channel_object.history())
  print (msg)

