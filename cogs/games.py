#!/usr/bin/env python3

import discord
import random
from discord.ext import commands
import os


bot = commands.Bot(command_prefix='!', intents=discord.Intents().all())

#roshambo dictionary
rsp = {
  "rock": True,  
  "paper": True, 
  "scissors": True }

class games(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.keeper = ""
    self.b_counter = 0

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

  @commands.command(name="droll", help="Rolls a dice. Can also specify range of roll.")
  async def droll(self, ctx, arg=6):
      number = random.randint(1, arg)
      await ctx.send(f"{ctx.message.author.mention} rolled: {number}")
    
  @commands.command(name="gcode", help="Saves an inputed game code")
  async def gcode(self, ctx, *arg):
    if self.keeper:
      await ctx.send(f"Your game code is: {self.keeper}")
    else:
      self.keeper = " ".join(arg)
      await ctx.send(f"Your game code is: {self.keeper}")

  @commands.command(name="rgcode", help="Resets the game code command")
  async def rgcode(self, ctx):
    self.keeper = ""
    await ctx.send("Your game code is reset!!")

#initalises the game cog
def setup(bot):
  bot.add_cog(games(bot))