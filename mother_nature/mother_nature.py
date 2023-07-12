from package_imports import *

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
  await ctx.response.send_message("Compiling history now...")
  await mother_nature.get_channel_history(ctx.channel.name, datetime.datetime(year, month, day), include_mother_nature)

@bot.command(name='commands', description='prints all commands', guild=discord.Object(id=996592811887579317))
async def get_commands(ctx):
  await ctx.response.send_message("Here is a list of all commands:")
  await mother_nature.get_commands(ctx.channel.name)    
  
@bot.command(name='is_color_legal', description='checks if a food coloring is legal according to the FDA', guild=discord.Object(id=996592811887579317))
async def color_legal(ctx, chemical_name: str):
  await ctx.response.send_message(await mother_nature.is_color_legal(ctx.channel.name, chemical_name))

@bot.command(name='check_fda_color_status', description='checks if a food coloring is legal according to the FDA', guild=discord.Object(id=996592811887579317))
async def check_color_status(ctx):
  await ctx.response.send_message(await mother_nature.check_fda_color_status())
   
@bot.command(name='edit_smile_file', description='edits the smile file for training mother nature', guild=discord.Object(id=996592811887579317))
async def edit_smile_file(ctx, smile: str):
  await ctx.response.send_message("Editing file now...")
  await mother_nature.edit_smile_file(smile)

@bot.command(name='make_github_issue_lorax', description='creates new chemical compounds', guild=discord.Object(id=996592811887579317))
async def github_issue(ctx, message: str):
  await ctx.response.send_message("Do you speak for the trees, profound lorax?")
  await mother_nature.make_issue_lorax(ctx.channel.name, message)

@bot.command(name='make_github_issue_arbiter', description='creates new chemical compounds', guild=discord.Object(id=996592811887579317))
async def github_issue(ctx, message: str):
  await ctx.response.send_message("Have you discovered your secret power, o mighty arbiter?")
  await mother_nature.make_issue_arbiter(ctx.channel.name, message)

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
      'contraceptives', 'materials'
    ]

    def get_channel(self, channel_name):
       for channel in client.get_all_channels():
          if channel_name == channel.name:
             return channel

    async def get_channel_history(self, channel_name, date, include_mother_nature):
      channel = self.get_channel(channel_name)
      if not channel:
        return

      stop_words = set(stopwords.words('english'))

      msg = [message async for message in channel.history(after=date)]
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
      channel = self.get_channel(channel_name)
      if not channel:
        return
    
      await channel.send("\n".join(self.__list_commands__))
        
    async def check_fda_color_status(self):      
      bot = BotColourAdditiveList()
      bot.get_fda_reported_lists()
      bot.get_global_chem_lists()
      return bot.check_list_status()

    async def edit_smile_file(self, smile):
      label = repo.get_label("enhancement")
      repo.create_issue(title="SMILE_edit Run", labels=[label], body=smile, assignee="Sulstice")
      

    async def is_color_legal(self, channel_name, chemical_name):
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
      channel = self.get_channel(channel_name)
      if not channel:
        return
      
      text_message = message.lower()
      for keyword in self.__category_keywords__:
        if keyword in text_message:
          await self.create_issue(channel, keyword=keyword)
          
        
    async def make_issue_lorax(self, channel_name, message):
      channel = self.get_channel(channel_name)
      if not channel:
        return
      
      text_message = message.lower()
      for keyword in self.__category_keywords__:
        if keyword in text_message:
          if keyword == "war" or keyword == "narcotics":
              await channel.send("You do not have the requisite permissions to use the %s keyword. You must have the role 'Arbiter of Nature' for the categories 'war' and 'narcotics'." %keyword)
          else:
            await self.create_issue(channel, keyword=keyword)
      

    async def create_issue(self, channel, keyword):
      await channel.send('Creating %s Chemicals Now...' % keyword)

      keyword = '_'.join(keyword.split())

      label = repo.get_label("run_%s" % keyword)
      repo.create_issue(title="%s Run" %keyword, labels=[label], assignee="Sulstice")

mother_nature = MotherNatureCommands()
client.run(DISCORD_TOKEN)

