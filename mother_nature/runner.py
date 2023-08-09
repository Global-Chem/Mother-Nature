# Python Internals
# ----------------
import os

# Python Externals
# ----------------

import nltk
import discord
import datetime
from dotenv import load_dotenv

# Discord Imports
# ---------------

from discord.ext import commands
from discord import app_commands

# Github Imports
# --------------

from github import Github

# Mother Nature Imports
# ---------------------

from mother_nature import MotherNatureCommands

'''

Mother Nature Interactions

  Event:
    on_ready (Action): When the "Mother Nature" Bot Signs on the Discord Server

  Commands:
    get_history (Command): Get's the History of the a Channel Based on Name and Date Time.
    get_commands (Command): Get's the List of Commands available to the user.
    color_legal (Command): Determine if the color is legal in the United States FDA
    check_fda_status (Command): Check the FDA Colour status
    github_issue (Command): Issue a Github Issue
    make_issue_lorax (Command): Make a issue for the Generative AI without permissions for War and Narcotics
    make_issue_arbitrer (Command): If you have this role then it's the issue including All chemical lists as well as General.
    add_smile_file (Command): 
    remove_smile_file (Command): 

'''

load_dotenv()
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

github = Github(GITHUB_TOKEN)
repo = github.get_repo("Global-Chem/private-workers")
global_chem_repo = github.get_repo("Global-Chem/global-chem")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

channel = discord.utils.get(client.get_all_channels(), name='cannabis')

bot = commands.Bot(command_prefix='$', intents=intents)
bot = app_commands.CommandTree(client)

# ---------------    Events    -------------------------------

@client.event
async def on_ready():
  await bot.sync(guild=discord.Object(id=996592811887579317))
  print("Ready!")

# ---------------    Commands    -----------------------------

command_names = {
  'history': 'gets the history of the channel and takes out common words from each message',
  'commands': 'prints all commands',
  'is_color_legal': 'checks if a food coloring is legal according to the FDA',
  'check_fda_color_status': 'checks if a food coloring is legal according to the FDA',
  'make_github_issue_lorax': 'creates new chemical compounds',
  'make_github_issue_arbiter': 'creates new chemical compounds',
  'add_smile_file': 'adds a smile to the smile file for training mother nature',
  'remove_smile_file': 'removes a smile from the smile file for training mother nature',
  'retrain': 'retrains mother nature bot ',
  'create_graph_node': 'creates a new node in the global chem graph',
  'fetch_training_set': 'fetches the training set and sends the image to the corresponding channel',
  'file_issue': 'creates a github issue for something that needs fixing'
}

mother_nature = MotherNatureCommands(
  github=github, 
  repo=repo, 
  global_chem_repo=global_chem_repo,
  client=client, 
  bot=bot
)

guild_object = discord.Object(id=mother_nature.__GUILD_ID__)

@bot.command(name='history', description=command_names['history'], guild=guild_object)
async def get_history(ctx, year: int, month: int, day: int, include_mother_nature: bool):
  await ctx.response.send_message("Compiling history now...")
  await mother_nature.get_channel_history(ctx.channel.name, datetime.datetime(year, month, day), include_mother_nature)

@bot.command(name='commands', description=command_names['commands'], guild=guild_object)
async def get_commands(ctx):
  await ctx.response.send_message("Here is a list of all commands:")
  await mother_nature.get_commands(ctx.channel.name)

@bot.command(name='is_color_legal', description=command_names['is_color_legal'], guild=guild_object)
async def color_legal(ctx, chemical_name: str):
  await ctx.response.send_message(await mother_nature.is_color_legal(ctx.channel.name, chemical_name))

@bot.command(name='check_fda_color_status', description=command_names['check_fda_color_status'], guild=guild_object)
async def check_color_status(ctx):
  await ctx.response.send_message(await mother_nature.check_fda_color_status())

@bot.command(name='remove_smile_file', description=command_names['remove_smile_file'], guild=guild_object)
async def remove_smile_file(ctx, smile_index: int):
  await ctx.response.send_message("Editing file now...")
  await mother_nature.remove_smile_file(smile_index, ctx.channel.name)

@bot.command(name='add_smile_file', description=command_names['add_smile_file'], guild=guild_object)
async def add_smile_file(ctx, smile: str):
  await ctx.response.send_message("Editing file now...")
  await mother_nature.add_smile_file(smile, ctx.channel.name)

@bot.command(name='retrain_mother_nature', description=command_names['retrain'], guild=guild_object)
async def retrain(ctx, retrain_again: bool):
  await ctx.response.send_message("Retraining now...")
  await mother_nature.retrain(ctx.channel.name, retrain_again)

@bot.command(name='make_github_issue_lorax', description=command_names['make_github_issue_lorax'], guild=guild_object)
async def make_github_issue_lorax(ctx, channel_name: str):
  await ctx.response.send_message("Do you speak for the trees, profound lorax?")
  await mother_nature.make_issue_lorax(ctx.channel.name, channel_name)

@bot.command(name='make_github_issue_arbiter', description=command_names['make_github_issue_arbiter'], guild=guild_object)
async def make_github_issue_arbiter(ctx, channel_name: str):
  await ctx.response.send_message("Have you discovered your secret power, o mighty arbiter?")
  await mother_nature.make_issue_arbiter(ctx.channel.name, channel_name)

@bot.command(name='create_graph_node', description=command_names['create_graph_node'], guild=discord.Object(id=996592811887579317))
async def create_graph_node(ctx, node_class_name: str, text_message: str):
  await ctx.response.send_message("Creating a new node now...")
  await mother_nature.create_graph_node(node_class_name, text_message)

@bot.command(name='fetch_training_set', description=command_names['fetch_training_set'], guild=discord.Object(id=996592811887579317))
async def fetch_training_set(ctx, category: str):
  await ctx.response.send_message("Fetching data...")
  await mother_nature.fetch_training_set(category)

@bot.command(name='file_issue',description=command_names['file_issue'], guild=discord.Object(id=996592811887579317))
async def file_issue(ctx, title: str, issue: str):
  await ctx.response.send_message("Filing issue now...")
  await mother_nature.file_issue(title, issue)

client.run(DISCORD_TOKEN)
