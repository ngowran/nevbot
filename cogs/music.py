#!/usr/bin/env python3

import discord
from discord.ext import commands
#import youtube_dl

bot = commands.Bot(command_prefix='!', intents=discord.Intents().all())

class music(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="test", help="test command")
  async def test(self, ctx, arg):
    await ctx.send(f"test {arg}")
  
  bot.add_command(test)

#initalises the music cog
def setup(bot):
  bot.add_cog(music(bot))