#!/usr/bin/env python3

import discord
from discord.ext import commands
import random
from Other.phrase import sentences

bot = commands.Bot(command_prefix="!", intents=discord.Intents().all())

class events(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

#initalises the event cog
def setup(bot):
  bot.add_cog(events(bot))