# Python Internals
# ----------------
import os
import re
import ast

# Python Externals
# ----------------

import nltk
import discord
import asyncio
import requests
import datetime
import textwrap
import pandas as pd
from dotenv import load_dotenv

# NLTK Download Data
# ------------------
nltk.download('stopwords')
nltk.download('punkt')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Discord Imports
# ---------------

from discord.ext import commands
from discord import app_commands
from discord.ext.commands import Bot

# Github Imports
# --------------

from git import Repo
from github import Github

# Bot Imports
# -----------

from color_legal import BotColourAdditiveList