# Python Internals
# ----------------
import os
import re

# Python Externals
# ----------------

import nltk
import asyncio
import discord

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

# Github Imports
# --------------

from github import Github
from color_legal import BotColourAdditiveList

class MotherNatureCommands(object):

    __GUILD_ID__ = 996592811887579317

    __list_commands__ = [
      "history",                    # Fetches the History of All The Messages
      "commands",                   # Gets the List of Commands
      "help",                       # Gets a Help Message
      "is_color_legal",             # Checks to see if a color is in the  legal color list
      "create_issue_lorax",         # Creates a Github Issue with the Lorax
      "create_issue_arbiter",       # Creates a Github Issue with Arbitrer Status
      "check_fda_color_status",     # Checks the FDA Color Status
      "edit_smile_file"             # Edit a Smile File
    ]

    __langchain_keywords__ = [
      'chatgpt'
    ]

    __category_keywords__ = [
      'solar cells', 'cannabis', 'war', 'sex',
      'education', 'medicinal chemistry', 'food',
      'environment',  'space', 'narcotics', 'global',
      'contraceptives', 'materials', 'performance enhancements'
    ]

    def __init__(self, github, repo, global_chem_repo, client, bot):

        self.github = github
        self.repo = repo
        self.global_chem_repo = global_chem_repo

        self.client = client
        self.bot = bot

    def get_channel(self, channel_name):

      '''

      Gets the Channel Object

      Arguments:
          channel_name (String): Gets the Channel Name

      Returns:
          channel (Discord Channel Object): The Discord Channel Object wit the associated name.

      '''

      for channel in self.client.get_all_channels():
        if channel_name == channel.name:
          return channel

    async def get_channel_history(self, channel_name, date, include_mother_nature):

      '''

      Gets the Channel History

      Arguments:
          channel_name (String): The channel name on the discord server
          date (String): The Datetime that the user wants the history up too.
          include_mother_nature (Bool): Whether you want the user Mother Nature History.

      Returns:
          Discord Message (String): The History of the Channel.

      '''

      channel = self.get_channel(channel_name)

      if not channel:
        return

      stop_words = set(stopwords.words('english'))
      msg = [ message async for message in channel.history(after=date) ]

      for text in msg:
        if include_mother_nature == False and text.author.name == "Mother Nature":
          continue

        filtered_sentence = []
        word_tokens = word_tokenize(text.content)

        for w in word_tokens:
          if w not in stop_words:
              filtered_sentence.append(w)

        await channel.send(' '.join(str(x) for x in filtered_sentence))
      await channel.send("Done")

    async def get_commands(self, channel_name):

      '''

      Arguments:
        channel_name (String): The channel name on the discord server

      Returns:
        Discord Message (String): The List of Commands on to the String.

      '''

      channel = self.get_channel(channel_name)
      if not channel:
        return

      await channel.send("\n".join(self.__list_commands__))

    async def check_fda_color_status(self):

      '''

      Checks the FDA Colour Status

      Returns:
          list_status (List): List of Chemicals Missing or Changed.

      '''

      bot = BotColourAdditiveList()
      bot.get_fda_reported_lists()
      bot.get_global_chem_lists()

      return bot.check_list_status()

    async def edit_smile_file(self, smile):

      '''

      Edits and Removes a SMILES based on the index.

      Arguments:
          smile (Int): Number Index of which smiles to remove from the list.

      Event:
          Create issue
      '''

      label = self.repo.get_label("enhancement")
      self.repo.create_issue(title="SMILE_edit Run", labels=[label], body=smile, assignee="Sulstice")

    async def is_color_legal(self, channel_name, chemical_name):

      '''

      Checks to see if a specific color is legal in the FDA List.

      Arguments:
          channel_name (String): String of the Channel Name
          chemical_name (String): String of the Chemical to Check.

      Returns:
          Discord Message (String): Whether the Chemical Name is part of the List.

      '''

      channel = self.get_channel(channel_name)

      if not channel:
        return

      chemical_name = chemical_name.lower().strip()
      bot = BotColourAdditiveList()
      fda_list = bot.get_fda_reported_lists()
      fda_list = sum(fda_list, [])

      if chemical_name in fda_list:
        return (chemical_name + " is legal in the United States")
      else:
        return (chemical_name + " is not in the FDA color list")

    async def make_issue_arbiter(self, channel_name, message):

      '''

      Allows the ability to make an issue and use the generative AI to build molecules.

      Arguments:
          channel_name (String): String of the Channel Name
          message (String):  Which action to take in terms of creating or retraining the AI system for that branch.

      Returns:
          Discord Message (String): Whether the Chemical Name is part of the List.

      '''

      channel = self.get_channel(channel_name)
      text_message = message.lower()
      if not channel:
          return

      for keyword in self.__category_keywords__:
        if keyword in text_message:
          await self.create_issue(channel, keyword=keyword)


    async def make_issue_lorax(self, channel_name, message):

      '''

      Allows the ability to make an issue and use the generative AI to build molecules without War or Narcotics.

      Arguments:
          channel_name (String): String of the Channel Name
          message (String):  Which action to take in terms of creating or retraining the AI system for that branch.

      Returns:
          Discord Message (String): Whether the Chemical Name is part of the List.

      '''

      channel = self.get_channel(channel_name)
      if not channel:
        return

      text_message = message.lower()
      for keyword in self.__category_keywords__:
        if keyword in text_message:
          if keyword == "war" or keyword == "narcotics" or keyword == "performance enhancements":
              await channel.send("You do not have the requisite permissions to use the %s keyword. You must have the role 'Arbiter of Nature' for the categories 'war', 'narcotics', and 'performance enhancements'." %keyword)
          else:
            await self.create_issue(channel, keyword=keyword)

    async def create_issue(self, channel, keyword):

      '''

      Creates the Github Issue

      Arguments:
          channel (Discord Object): Discord Channel Object.
          keyword (String): String of which branch to file under etc. Cannabis, War.

      '''

      await channel.send('Creating %s Chemicals Now...' % keyword)

      keyword = '_'.join(keyword.split())

      label = self.repo.get_label("run_%s" % keyword)
      self.repo.create_issue(title="%s Run" %keyword, labels=[label], assignee="Sulstice")

    smiles = {'arachidic': '', 'arachidic': '',}


    async def create_graph_node(self, node_class_name, text_message):
      node_name = node_class_name.lower()
      entries = {}
      _ = [ entries.setdefault(i.strip(), '') for i in text_message.split(",") ]
      template_string = '''
      Node to be added to the Knowledge Graph
      ```python
            class %s(object):
                def __init__(self):
                    self.name == '%s'
                @staticmethod
                def get_smiles():
                  smiles =  %s
                  return smiles
      ```
          ''' % (node_class_name,
      node_name,
      entries
      )

      self.global_chem_repo.create_issue(
      title='Create Graph Node: %s' % node_class_name,
      body=template_string,
      assignee="Sulstice"
    )
      
    async def add_smile_file(self, smile_index, channel_name):
      channel = self.get_channel(channel_name)
      label = self.repo.get_label("add_smile_%s" % channel_name)
      self.repo.create_issue(title="SMILE edit Run", labels=[label], body=smile_index, assignee="Sulstice")

    async def remove_smile_file(self, smile_index, channel_name):
      label = self.repo.get_label("remove_smile_%s" % channel_name)
      self.repo.create_issue(title="SMILE edit Run", labels=[label], body=smile_index, assignee="Sulstice")
      
    async def retrain(self, channel_name, retrain_again):
      channel = self.get_channel(channel_name)
      label = self.repo.get_label("retrain_%s" % channel_name)
      self.repo.create_issue(title="SMILE edit Run", labels=[label], assignee="Sulstice")
      if retrain_again == False:
        return
      await asyncio.sleep(518400)
      allowed_mentions = discord.AllowedMentions(everyone = True)
      await channel.send(content = "@everyone Mother Nature will retrain in 1 day", allowed_mentions = allowed_mentions)
      await asyncio.sleep(86400)
      await channel.send("Retraining...")
      self.retrain(channel_name, retrain_again)

    async def fetch_training_set(self, training_set):
      label = self.repo.get_label("fetch_%s" % training_set)
      self.repo.create_issue(title="Fetch_Training_Set", labels=[label], assignee="Sulstice")

    async def file_issue(self, title, issue):
      label = self.repo.get_label("user_reported")
      self.repo.create_issue(title=title, labels=[label], body=issue, assignee="Sulstice")