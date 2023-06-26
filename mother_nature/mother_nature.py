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
from discord import app_commands
from discord.ext.commands import Bot

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

bot = commands.Bot(command_prefix='$', intents=intents)
bot = app_commands.CommandTree(client)

@bot.command(name='tester', description='testing', guild=discord.Object(id=996592811887579317))
async def test(ctx, msg: str):
  await ctx.send(msg)

@client.event
async def on_ready():
    await bot.sync(guild=discord.Object(id=996592811887579317))
    print("Ready!")

@bot.command(name='history', description='gets the history of the channel and takes out common words from each message', guild=discord.Object(id=996592811887579317))
async def get_history(ctx, year: int, month: int, day: int, include_mother_nature: bool):
  stop_words = set(stopwords.words('english'))
  channel = ctx.channel

  msg = [message async for message in channel.history(after=datetime.datetime(year, month, day))]
  for text in msg:
    filtered_sentence = []
    word_tokens = word_tokenize(text.content)
    for w in word_tokens:
      if w not in stop_words:
          filtered_sentence.append(w)
    await channel.send(' '.join(str(x) for x in filtered_sentence))

@bot.command(name='commands', description='prints all commands', guild=discord.Object(id=996592811887579317))
async def get_commands(ctx):
  for command in list_commands:
      await ctx.channel.send(command)

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
    
  
@bot.command(name='is_color_legal', description='checks if a food coloring is legal according to the FDA', guild=discord.Object(id=996592811887579317))
async def color_legal(ctx):
    bot = BotColourAdditiveList()
    bot.get_fda_reported_lists()
    bot.get_global_chem_lists()
    response = bot.check_list_status()
    await ctx.channel.send(response)

@bot.command(name='make_github_issue', description='creates a github issue', guild=discord.Object(id=996592811887579317))
async def github_issue(ctx, message: str):
    for role in message.author.roles:
      if role.name == "Nature Lorax":
        text_message = ctx.message.content.lower()
        if any(word in text_message for word in action_keywords):
          for keyword in category_keywords:
            if keyword in text_message:
              await ctx.channel.send('Creating %s Chemicals Now...' % keyword)
              await create_issue(keyword=keyword)
      else:
        ctx.channel.send("You do not have permissions for this")

async def create_issue(*keyword):

  keyword = '_'.join(keyword.split())

  label = repo.get_label("run_%s" % keyword)
  repo.create_issue(title="%s Run" %keyword, labels=[label], assignee="Sulstice")

  return

client.run(DISCORD_TOKEN)

