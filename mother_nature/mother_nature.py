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
    if include_mother_nature == False and text.author.name == "Mother Nature":
      continue
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
  
@bot.command(name='is_color_legal', description='checks if a food coloring is legal according to the FDA', guild=discord.Object(id=996592811887579317))
async def color_legal(ctx):
    bot = BotColourAdditiveList()
    bot.get_fda_reported_lists()
    bot.get_global_chem_lists()
    response = bot.check_list_status()
    await ctx.channel.send(response)

@bot.command(name='make_github_issue', description='creates a github issue', guild=discord.Object(id=996592811887579317))
async def github_issue(ctx, message: str):
    user_role = ""
    if "Arbiter of Nature" in ctx.user.roles:
        user_role = "Arbiter of Nature"
    elif "Nature Lorax" in ctx.user.roles:
        user_role = "Nature Lorax"
    else:
      await ctx.channel.send("You do not have permissions for this")
      return

    text_message = message.lower()
    for keyword in category_keywords:
      if keyword in text_message:
        if keyword == "war" or keyword == "narcotics":
          if user_role == "Arbiter of Nature":
            await ctx.channel.send("here")
            await create_issue(ctx.channel, keyword=keyword)
          else:
            await ctx.channel.send("You do not have the requisite permissions. You must have the role 'Arbiter of Nature' for the categories 'war' and 'narcotics'.")
        else:
          await create_issue(ctx.channel, keyword=keyword)

async def create_issue(channel, keyword):
  await channel.send('Creating %s Chemicals Now...' % keyword)

  keyword = '_'.join(keyword.split())

  label = repo.get_label("run_%s" % keyword)
  repo.create_issue(title="%s Run" %keyword, labels=[label], assignee="Sulstice")

  return

client.run(DISCORD_TOKEN)

