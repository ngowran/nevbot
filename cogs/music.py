#!/usr/bin/env python3

import discord
from discord.ext import commands
#import youtube_dl

bot = commands.Bot(command_prefix='!', intents=discord.Intents().all())

class music(commands.Cog):
  def __init__(self, bot):
    self.bot = bot


  @commands.command(name="join", help="Make the bot join VC.")
  async def join(self, ctx):
    await ctx.author.voice.channel.connect()
    await ctx.send("I'm here bitches")

  @commands.command(name="leave", help="Make the bot leave VC.")
  async def leave(self, ctx):
    await ctx.voice_client.disconnect()
    await ctx.send("Bye bitches") 

#initalises the music cog
def setup(bot):
  bot.add_cog(music(bot))