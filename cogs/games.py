#!/usr/bin/env python3

import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=discord.Intents().all())

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
    await ctx.send(f"i got {botans}.")
    if arg not in rsp:
      await ctx.send("Invalid choice. Please enter rock, paper or scissors.")
    elif botans == arg:
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

def setup(bot):
  bot.add_cog(games(bot))