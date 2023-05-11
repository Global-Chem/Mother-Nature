# Imports
# -------
import os
import discord

from github import Github
from dotenv import load_dotenv

# Discord Environment
# --------------------

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

intents = discord.Intents.default()
client = discord.Client(intents=intents)

# Github Environment
# ------------------

github = Github(GITHUB_TOKEN)
repo = github.get_repo("Global-Chem/private-workers")

# Discord Commands
# ----------------

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):

    if 'thank you' in message.content.lower():
        await message.channel.send('No Problem')

    # Cannabis

    if 'create new cannabis chemicals' in message.content.lower():
        await message.channel.send('Generating New Cannabis Compounds Now..')
        label = repo.get_label("run_cannabis")
        repo.create_issue(title="Cannabis Run", labels=[label])

    # War

    if 'create new war chemicals' in message.content.lower():
      await message.channel.send('Generating New War Compounds Now..')
      label = repo.get_label("run_war")
      repo.create_issue(title="War Run", labels=[label])

    # Sex

    if 'create new sex chemicals' in message.content.lower():
      await message.channel.send('Generating New Sex Compounds Now..')
      label = repo.get_label("run_sex")
      repo.create_issue(title="Sex Run", labels=[label])

    # Education

    if 'create new education chemicals' in message.content.lower():
      await message.channel.send('Generating New Education Compounds Now..')
      label = repo.get_label("run_education")
      repo.create_issue(title="Education Run", labels=[label])

    # Medicinal Chemistry

    if 'create new medicinal chemicals' in message.content.lower():
      await message.channel.send('Generating New Medicinal Compounds Now..')
      label = repo.get_label("run_medicinal_chemistry")
      repo.create_issue(title="Medicinal Chemistry Run", labels=[label])

    # Food

    if 'create new food chemicals' in message.content.lower():
      await message.channel.send('Generating New Food Compounds Now..')
      label = repo.get_label("run_food")
      repo.create_issue(title="Food Run", labels=[label])

    # Environment

    if 'create new environment chemicals' in message.content.lower():
      await message.channel.send('Generating New Environment Compounds Now..')
      label = repo.get_label("run_environment")
      repo.create_issue(title="Environment Run", labels=[label])

    # Space

    if 'create new space chemicals' in message.content.lower():
      await message.channel.send('Generating New Space Compounds Now..')
      label = repo.get_label("run_space")
      repo.create_issue(title="Space Run", labels=[label])

    # Materials

    if 'create new materials chemicals' in message.content.lower():
      await message.channel.send('Generating New Materials Compounds Now..')
      label = repo.get_label("run_materials")
      repo.create_issue(title="Materials Run", labels=[label])

    # Narcotics

    if 'create new narcotics chemicals' in message.content.lower():
      await message.channel.send('Generating New Narcotics Compounds Now..')
      label = repo.get_label("run_narcotics")
      repo.create_issue(title="Narcotics Run", labels=[label])

    # Global

    if 'create new global chemicals' in message.content.lower():
      await message.channel.send('Generating New Global Compounds Now..')
      label = repo.get_label("run_global")
      repo.create_issue(title="Global Run", labels=[label])

# Runner
# ------

client.run(DISCORD_TOKEN)
