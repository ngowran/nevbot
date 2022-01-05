#!/usr/bin/env python3

import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=discord.Intents().all())

#roshambo dictionary
rsp = {
  "rock": True,  
  "paper": True, 
  "scissors": True }

class games(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.command(name="roshambo", help="Plays Rock-Paper-Scissors with the user")
  async def roshambo(self, ctx, arg):
    botans = random.choice(list(rsp))
    if arg not in rsp:
      await ctx.send("Invalid argument. Please use a suitable one.")
    else:
      await ctx.send(f"i got {botans}.")
    if botans == arg:
      await ctx.send("its a tie!!!")
    elif botans == "rock" and arg == "paper":
      await ctx.send("i lose :(")
    elif botans == "rock" and arg == "scissors":
      await ctx.send("i win :)")
    elif botans == "paper" and arg == "rock":
      await ctx.send("i win :)")
    elif botans == "paper" and arg == "scissors":
      await ctx.send("i lose :(")
    elif botans == "scissors" and arg == "rock":
      await ctx.send("i lose :(")
    elif botans == "scissors" and arg == "paper":
      await ctx.send("i win :)")
  

  @commands.command(name="cflip", help="Flips a coin.")
  async def cflip(self, ctx):
    coin = ["heads", "tails"]
    await ctx.send(f"the coin flipped to {random.choice(coin)}.")

  @commands.command(name="hulkbust", help="Hulkbust.")
  async def hulkbust(self, ctx):
    await ctx.send(file=discord.File("Other/media/hulkbuster.gif", spoiler=False))


#initalises the game cog
def setup(bot):
  bot.add_cog(games(bot))