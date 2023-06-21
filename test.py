# Imports
# -------
import os
import re
import discord
import asyncio
import textwrap
import pandas as pd

from github import Github
from dotenv import load_dotenv

# Defaults
# --------

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
client = discord.Client(intents=intents)


async def retrieve_channel_conversation_history(keyword, after_date, include_mother_nature=False):
  
  # Get text here
  
  contents = []
  channels = client.get_all_channels()
  
  print(dir(channels))
  
  for channel in channels:
    
    print(channel.name)
    contents.append(channel.name)
    
    if channel.name == keyword:
      #contents1 = [message async for message in channel.history(limit=10)]
      
      return list(channel)

  return contents

conversation = asyncio.run(retrieve_channel_conversation_history("cannabis", "2022-2-3 10:11:12"))

client.run(DISCORD_TOKEN)
