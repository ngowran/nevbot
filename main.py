#!/usr/bin/env python3

import discord
import os
from discord.ext import commands
import random
from Other.phrase import sentences
import Host

# prefix to be inputed for bot command
# intents is what the bot is allowed to do on the server
bot = commands.Bot(command_prefix='!', intents=discord.Intents().all())
client = discord.Client()

# bot startup event actions
@bot.event
async def on_ready():
  channel = bot.get_channel(931949653283451004)
  await channel.send(random.choice(sentences))
  await bot.change_presence(activity=discord.Game(name="Type !help to use me ;)"))

# loads each cog class as a cog
for filename in os.listdir("./cogs"):
  if filename.endswith('.py'): 
    bot.load_extension(f"cogs.{filename[:-3]}")

# uses the token to run the bot on the server
Host.host()
token = "OTIyNDQ4NDkzMzIxMjgxNTM2.YcBnGw.30ysz7Zpqh7xikybPzyo_rj27zg"
bot.run(token)