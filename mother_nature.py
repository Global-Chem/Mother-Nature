# Imports
# -------
import os
import re
import discord
import textwrap
import pandas as pd

from github import Github
from dotenv import load_dotenv

# LangChain Imports
# -------------------

from langchain.agents import create_pandas_dataframe_agent
from langchain.memory import ConversationBufferWindowMemory
from langchain import OpenAI, ConversationChain, LLMChain, PromptTemplate

# Defaults
# --------

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_GLOBALCHEM_TOKEN = os.getenv('GITHUB_TOKEN')
OPENAI_API_KEY= os.getenv('OPENAI_API_KEY')

# Devops Environment
# ------------------

intents = discord.Intents.default()
client = discord.Client(intents=intents)

github = Github(GITHUB_TOKEN)
repo = github.get_repo("Global-Chem/private-workers")

global_chem_github = Github(GITHUB_GLOBALCHEM_TOKEN)
global_chem_repo = github.get_repo("Global-Chem/global-chem")

# Key Word Defaults
# -----------------

langchain_keywords = ['chatgpt']
action_keywords = ['create', 'generate']
category_keywords = [
  'solar cells', 'cannabis', 'war', 'sex', 'education', 'medicinal chemistry', 'food', 'environment',
  'space', 'narcotics', 'global', 'contraceptives', 'materials'
]

template = """Welcome to a prototype version of a GlobalChem Linked to ChatGPT we coined 'Mother Nature'"""

# Core Functions
# --------------

def create_issue(keyword):

  keyword = '_'.join(keyword.split())

  label = repo.get_label("run_%s" % keyword)
  repo.create_issue(title="%s Run" %keyword, labels=[label], assignee="Sulstice")

  return

def create_graph_node(node_class_name, text_message):

  node_name = node_class_name.lower()
  entries = str(re.findall('{(.+?)}', text_message))

  template_string = '''

Node to be added to the Knowledge Graph

```python
      class %s(object):

          def __init__(self):

              self.name == '%s'

          @staticmethod
          def get_smiles():

            smiles = {
                %s
            }

            return smiles
```
    ''' % (
    node_class_name,
    node_name,
    entries
  )

  global_chem_repo.create_issue(
    title='Create Graph Node: %s' % node_class_name,
    body=template_string,
    assignee="Sulstice"
  )


# Routine Startup Commands
# ------------------------

# 1. Log into Server

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord! \n {template}')

# 2. Load the LangChains

df = pd.read_csv(
  'https://raw.githubusercontent.com/Global-Chem/global-chem/development/global_chem/global_chem_outputs/global_chem.tsv',
  sep='\t',
  header=None,
  names=['name', 'smiles', 'node', 'predicate', 'path']
)

prompt = PromptTemplate(
  template=template,
  input_variables=[]
)

chatgpt_chain = LLMChain(
  llm=OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY),
  prompt=prompt,
  verbose=True,
  memory=ConversationBufferWindowMemory(k=100),
)

agent = create_pandas_dataframe_agent(
  OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY), df,verbose=True
)

# 3. Load Commands

@client.event
async def on_message(message):

  text_message = message.content.lower()

  if 'thank you' in text_message:
    await message.channel.send('No Problem')

  # Generating New Chemicals

  if any(word in text_message for word in action_keywords):
    for keyword in category_keywords:
      if keyword in text_message:
        await message.channel.send('Creating %s Chemicals Now...' % keyword)
        create_issue(keyword=keyword)

  # Talk to Our Graph Network

  if 'add node' in text_message:
    node_class_name = message.content.split('Node Name:')[1].split()[0]
    await message.channel.send('Creating Graph Node...')
    create_graph_node(node_class_name, text_message)
    await  message.channel.send('Graph Node Created')

  # Global-Chem Integration

  if 'dataframe' in message.content.lower():
    question = text_message.split(':')[1]
    output = agent.run(question)
    await message.channel.send(str(output))

  # Language Chaining Chemicals

  if any(word in text_message for word in langchain_keywords):

    output = chatgpt_chain.predict(
      human_input=message.content.lower()
    )

    await message.channel.send(output)
    
# 4. Execute the Runner

client.run(DISCORD_TOKEN)
