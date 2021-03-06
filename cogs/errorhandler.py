#!/usr/bin/env python3

import discord
from discord.ext import commands

class ErrorHandler(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  # listener watches for on_command_error EVENT and then sends an error message when there is no argument passed into a command
  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send("Please enter an existing argument, can be found via !help :)")
    #OR send message if the command is not found
    elif isinstance(error, commands.CommandNotFound):
      await ctx.send("Please enter a valid command :)") 
    elif isinstance(error, commands.BadArgument):
      await ctx.send("Please enter an appropriate argument type :)")
    elif isinstance(error, commands.MissingAnyRole):
      await ctx.send("Sorry, you don't have the correct permissions to do that! :)")
    elif isinstance(error, commands.CommandOnCooldown):
      await ctx.send(f"Try again in {error.retry_after:.2f}s.")
    #else:
      #await ctx.send(f"{error}. Please try again :) {ctx.message.author.mention}.")

#initalises the error cog
def setup(bot):
  bot.add_cog(ErrorHandler(bot))