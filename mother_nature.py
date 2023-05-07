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

    if 'generate new terpenes' in message.content.lower():
        await message.channel.send('Generating New Cannabis Compounds Now..')
        label = repo.get_label("run_cannabis")
        repo.create_issue(title="Cannabis Run", labels=[label])

# Runner
# ------

client.run(DISCORD_TOKEN)
