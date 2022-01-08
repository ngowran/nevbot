#!/usr/bin/env python3

import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=discord.Intents().all())

hoi_players = []
hoi_countries = []
countries_tmp = []

class hoiC(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    global teams
    teams = {
      1 : True,
    }

  @commands.command(name="addp", help="Add player(s) to the HOI teams list")
  async def addp(self, ctx, *args):
    add_players = list(args)
    for player in add_players:
      if player not in hoi_players:
        hoi_players.append(player)
    await ctx.send(f"The players are: {hoi_players}.")
  
  @commands.command(name="addc", help="Add country(s) to the HOI teams list")
  async def addc(self, ctx, *args):
    add_country = list(args)
    for country in add_country:
      if country not in hoi_countries:
        hoi_countries.append(country)
    await ctx.send(f"The countries are: {hoi_countries}.")
  
  @commands.command(name="hoi", help="Makes a HOI teams list")
  async def hoi(self, ctx):
    global countries_tmp
    teams.clear()
    if len(teams) == 0:
      for country in hoi_countries:
        countries_tmp.append(country)
      for player in hoi_players:
        cstr = random.choice(countries_tmp)
        countries_tmp.remove(cstr)
        teams[player] = cstr
      await ctx.send(f"The countries are: {teams}.")
    else:
      await ctx.send(f"The countries are: {teams}.")

  @commands.command(name="hoiremove", help="Remove user/country from HOI teams")
  async def hoiremove(self, ctx):
    teams.clear()
    countries_tmp = []
    hoi_players = []
    await ctx.send(f"The teams have been reset {countries_tmp}")
    
#initalises the hoi cog
def setup(bot):
  bot.add_cog(hoiC(bot))