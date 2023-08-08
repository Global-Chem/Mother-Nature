# -*- coding: utf-8 -*-
#
# Testing content definitions.
#
# ------------------------------------------------

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

from mother_nature.mother_nature import MotherNatureCommands

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

def test_initialize_class():

    '''

    Test the intialize of the class, with parameters if it extends to that

    '''

    mother_nature = MotherNatureCommands(
      github=github,
      repo=repo,
      global_chem_repo=global_chem_repo,
      client=client,
      bot=bot
    )

    assert mother_nature

def test_get_channel():

    '''

    Test the Retrieval of the Channel From Discord

    '''

    mother_nature = MotherNatureCommands(
      github=github,
      repo=repo,
      global_chem_repo=global_chem_repo,
      client=client,
      bot=bot
    )

    mother_nature.get_channel('cannabis')

def test_get_channel_history():

    '''

    Test The Retrieval of the Channel History

    '''

    mother_nature = MotherNatureCommands(
      github=github,
      repo=repo,
      global_chem_repo=global_chem_repo,
      client=client,
      bot=bot
    )

    history = mother_nature.get_channel_history('cannabis', '01/01/2000', False)

def test_get_commands():

    '''

    Test the Commands Retrieval To What is Available to Users from Mother Nature

    '''

    mother_nature = MotherNatureCommands(
      github=github,
      repo=repo,
      global_chem_repo=global_chem_repo,
      client=client,
      bot=bot
    )

    mother_nature.get_commands('playground-tests')

def test_check_fda_status():

    '''

    Test The Check For the FDA Status

    '''

    mother_nature = MotherNatureCommands(
      github=github,
      repo=repo,
      global_chem_repo=global_chem_repo,
      client=client,
      bot=bot
    )

    mother_nature.check_fda_color_status()

def test_edit_smile():

    '''

    Test the Editing of the Smiles

    '''

    mother_nature = MotherNatureCommands(
      github=github,
      repo=repo,
      global_chem_repo=global_chem_repo,
      client=client,
      bot=bot
    )

def test_is_color_legal():

    '''

    Test Whether the Color is Legal accoridng to the FDA

    '''

    mother_nature = MotherNatureCommands(
      github=github,
      repo=repo,
      global_chem_repo=global_chem_repo,
      client=client,
      bot=bot
    )

def test_make_issue_arbitrer():

    '''

    Test The Making of The Issue of the Role Arbiterer

    '''

    mother_nature = MotherNatureCommands(
      github=github,
      repo=repo,
      global_chem_repo=global_chem_repo,
      client=client,
      bot=bot
    )

def test_make_issue_lorax():

    '''

    Test The Making of The Issue of the Role Lorax

    '''

    mother_nature = MotherNatureCommands(
      github=github,
      repo=repo,
      global_chem_repo=global_chem_repo,
      client=client,
      bot=bot
    )

def test_create_issue():

    '''

    Test The Creating Issue Function of Mother Nature

    '''

    mother_nature = MotherNatureCommands(
      github=github,
      repo=repo,
      global_chem_repo=global_chem_repo,
      client=client,
      bot=bot
    )

def test_create_graph_node():

    '''

    Test the Making of a Graph Node

    '''

    mother_nature = MotherNatureCommands(
      github=github,
      repo=repo,
      global_chem_repo=global_chem_repo,
      client=client,
      bot=bot
    )
    
    mother_nature.create_graph_node('Test', 'test')

def test_add_smile_file():

    '''

    Test The Addition of a SMILES from the training set

    '''

    mother_nature = MotherNatureCommands(
      github=github,
      repo=repo,
      global_chem_repo=global_chem_repo,
      client=client,
      bot=bot
    )

def test_remove_smile_file():

    '''

    Test The Removal of a SMILES from the training set

    '''

    mother_nature = MotherNatureCommands(
      github=github,
      repo=repo,
      global_chem_repo=global_chem_repo,
      client=client,
      bot=bot
    )

def test_retraining():

    '''

    Test The Retraining of the Mother Nature on a Channel

    '''

    mother_nature = MotherNatureCommands(
      github=github,
      repo=repo,
      global_chem_repo=global_chem_repo,
      client=client,
      bot=bot
    )

def test_fetching_training_data():

    '''

    Test The Fetching of a Training Data

    '''

    mother_nature = MotherNatureCommands(
      github=github,
      repo=repo,
      global_chem_repo=global_chem_repo,
      client=client,
      bot=bot
    )

def test_filing_issue():

    '''

    Test The Filing of an Issue

    '''

    mother_nature = MotherNatureCommands(
      github=github,
      repo=repo,
      global_chem_repo=global_chem_repo,
      client=client,
      bot=bot
    )
