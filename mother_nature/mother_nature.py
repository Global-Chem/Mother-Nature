# Imports
# -------
import os
import re
import ast
import nltk
nltk.download('stopwords')
nltk.download('punkt')
import discord
import asyncio
import datetime
import textwrap
import pandas as pd

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from discord.ext import commands
#from discord.ext.commands import Bot

from github import Github
from dotenv import load_dotenv


# Bot Imports
# -----------
from color_legal import BotColourAdditiveList

# Defaults
# --------

list_commands = ["history: (number) year month day (True/False) include_mother_nature", "commands", "help", "iscolorlegal", "createissue"]

langchain_keywords = ['chatgpt']
action_keywords = ['create', 'generate']
category_keywords = [
  'solar cells', 'cannabis', 'war', 'sex', 'education', 'medicinal chemistry', 'food', 'environment',
  'space', 'narcotics', 'global', 'contraceptives', 'materials'
]

load_dotenv()
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

github = Github(GITHUB_TOKEN)
repo = github.get_repo("Global-Chem/private-workers")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


channel = discord.utils.get(client.get_all_channels(), name='cannabis')

bot = commands.Bot(command_prefix='$', intents=intents, guild=discord.Object(id=996592811887579317))

@bot.command(name='test', description='testing', guild=discord.Object(id=996592811887579317))
async def test(ctx, msg1):
  await ctx.send(msg1)

@bot.command(name='history', description='gets history of the channel')
async def get_history(channel, year, month, day, include_mother_nature):
  stop_words = set(stopwords.words('english'))
  
  msg = [message async for message in channel.history(after=datetime.datetime(year, month, day))]
  for text in msg:
    filtered_sentence = []
    word_tokens = word_tokenize(text.content)
    for w in word_tokens:
      if w not in stop_words:
          filtered_sentence.append(w)
    await channel.send(' '.join(str(x) for x in filtered_sentence))

@client.event
async def on_message(message):
  if message.author == "Mother Nature" or not message.content.startswith("!mn"):
    return
 
  words = message.content.split()

  if words[1] == "history":
    year = int(words[2])
    month = int(words[3])
    day = int(words[4])
    include_mother_nature = False
    if len(words) > 5:
      # must be capital first letter of True/False
      include_mother_nature = ast.literal_eval(words[5])
    await get_history(message.channel, year, month, day, include_mother_nature)

  elif words[1] == "commands":
    for command in list_commands:
      await message.channel.send(command)

  elif words[1] == "iscolorlegal":
    await color_legal(message)
    return

  elif words[1] == "createissue":
    for role in message.author.roles:
      if role.name == "Nature Lorax":
        text_message = message.content.lower()
        if any(word in text_message for word in action_keywords):
          for keyword in category_keywords:
            if keyword in text_message:
              await message.channel.send('Creating %s Chemicals Now...' % keyword)
              await create_issue(keyword=keyword)
      else:
        message.channel.send("You do not have permissions for this")
  
@bot.command(name='iscolorlegal')
async def color_legal(message):
    bot = BotColourAdditiveList()
    bot.get_fda_reported_lists()
    bot.get_global_chem_lists()
    response = bot.check_list_status()
    await message.channel.send(response)

@bot.command(name='createissue')
async def create_issue(keyword):

  keyword = '_'.join(keyword.split())

  label = repo.get_label("run_%s" % keyword)
  repo.create_issue(title="%s Run" %keyword, labels=[label], assignee="Sulstice")

  return

client.run(DISCORD_TOKEN)

