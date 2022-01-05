#!/usr/bin/env python3

import discord
from discord.ext import commands
from Other.phrase import languages, ftranslate, itranslate

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
  
  @commands.command(name="greeting", help="Greets user in a language of their choice")
  async def greeting(self, ctx, *args):
    if args[0] == "formal":
      if args[1] in languages:
        await ctx.send(f"{ftranslate[args[1]]} {ctx.message.author.mention}!")
      elif args[1] not in languages:
        await ctx.send("I haven't learned that language yet, sorry!!!")
    elif args[0] == "informal":
      if args[1] in languages:
        await ctx.send(f"{itranslate[args[1]]} {ctx.message.author.mention}!")
      elif args[1] not in languages:
        await ctx.send("I haven't learned that language yet, sorry!!!")
    else:
      await ctx.send("Sorry you need to specify if you want a formal or informal greeting!") 

#initalises the greet cog
def setup(bot):
  bot.add_cog(greet(bot))