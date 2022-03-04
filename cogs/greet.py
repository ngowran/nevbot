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
    if len(args) < 2:
      await ctx.send("Please speficy if you want me to greet you formal or informal and which language to greet you in!")
    lang = args[1].capitalize()
    if args[0].capitalize() == "Formal":
      if lang in languages:
        await ctx.send(f"{ftranslate[lang]} {ctx.message.author.mention}!")
      elif lang not in languages:
        await ctx.send("I haven't learned that language yet, sorry!!!")
    elif args[0].capitalize() == "Informal":
      if lang in languages:
        await ctx.send(f"{itranslate[lang]} {ctx.message.author.mention}!")
      elif lang not in languages:
        await ctx.send("I haven't learned that language yet, sorry!!!")
    else:
      await ctx.send("Sorry you need to specify if you want a formal or informal greeting!") 

#initalises the greet cog
def setup(bot):
  bot.add_cog(greet(bot))