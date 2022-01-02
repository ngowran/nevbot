#!/usr/bin/env python3

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=discord.Intents().all())

class greet(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.command(name='hello', help='Says hello to the user')
  async def hello(self, ctx):
    await ctx.send(f"hola, {ctx.message.author.mention}!")
  
  @commands.command(name='repeat', help='Repeats a message')
  async def repeat(self, ctx, *args):
    await ctx.send(' '.join(args))
 
def setup(bot):
  bot.add_cog(greet(bot))