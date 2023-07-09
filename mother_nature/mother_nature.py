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
import requests
import datetime
import textwrap
import pandas as pd

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from discord.ext import commands
from discord import app_commands
from discord.ext.commands import Bot

from github import Github
from git import Repo
from dotenv import load_dotenv


# Bot Imports
# -----------
from color_legal import BotColourAdditiveList

# Defaults
# --------

list_commands = ["history", "commands", "help", "is_color_legal", "create_issue_lorax", "create_issue_arbiter", "check_fda_color_status", "edit_smile_file"]

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
    await ctx.channel.send(' '.join(str(x) for x in filtered_sentence))
  await ctx.response.send_message("Done")

@bot.command(name='commands', description='prints all commands', guild=discord.Object(id=996592811887579317))
async def get_commands(ctx):
  await ctx.response.send_message("\n".join(list_commands))    
  
@bot.command(name='is_color_legal', description='checks if a food coloring is legal according to the FDA', guild=discord.Object(id=996592811887579317))
async def color_legal(ctx, chemical_name: str):
  chemical_name = chemical_name.lower().strip()
  bot = BotColourAdditiveList()
  fda_list = bot.get_fda_reported_lists()
  fda_list = sum(fda_list, [])
  if chemical_name in fda_list:
    await ctx.response.send_message(chemical_name + " is legal in the United States")
  else:
     await ctx.response.send_message(chemical_name + " is not in the FDA color list")

@bot.command(name='check_fda_color_status', description='checks if a food coloring is legal according to the FDA', guild=discord.Object(id=996592811887579317))
async def check_color_status(ctx):
  bot = BotColourAdditiveList()
  bot.get_fda_reported_lists()
  bot.get_global_chem_lists()
  response = bot.check_list_status()
  await ctx.response.send_message(response)
   
@bot.command(name='edit_smile_file', description='edits the smile file for training mother nature', guild=discord.Object(id=996592811887579317))
async def edit_smile_file(ctx, smile: str):
  await ctx.response.send_message("Editing file now...")
  label = repo.get_label("enhancement")
  repo.create_issue(title="SMILE_edit Run", labels=[label], body=smile, assignee="Sulstice")

@bot.command(name='make_github_issue_lorax', description='creates new chemical compounds', guild=discord.Object(id=996592811887579317))
async def github_issue(ctx, message: str):
    text_message = message.lower()
    for keyword in category_keywords:
      if keyword in text_message:
        if keyword == "war" or keyword == "narcotics":
            await ctx.response.send_message("You do not have the requisite permissions to use these keywords. You must have the role 'Arbiter of Nature' for the categories 'war' and 'narcotics'.")
        else:
          await create_issue(ctx.channel, keyword=keyword)

@bot.command(name='make_github_issue_arbiter', description='creates new chemical compounds', guild=discord.Object(id=996592811887579317))
async def github_issue(ctx, message: str):
    text_message = message.lower()
    for keyword in category_keywords:
      if keyword in text_message:
        await create_issue(ctx.channel, keyword=keyword)

async def create_issue(channel, keyword):
  await channel.send('Creating %s Chemicals Now...' % keyword)

  keyword = '_'.join(keyword.split())

  label = repo.get_label("run_%s" % keyword)
  repo.create_issue(title="%s Run" %keyword, labels=[label], assignee="Sulstice")

  return

client.run(DISCORD_TOKEN)

