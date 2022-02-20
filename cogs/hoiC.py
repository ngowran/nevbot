#!/usr/bin/env python3

import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=discord.Intents().all())



class hoiC(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

    self.hoi_players = []
    self.hoi_countries = []
    self.countries_tmp = []
    self.teams = {}


  def reset(self):
    self.teams.clear()
    self.countries_tmp.clear()
    self.hoi_players.clear()
  
  @commands.command(name="addp", help="Add player(s) to the HOI teams list")
  async def addp(self, ctx, *args):
    add_players = list(args)
    for player in add_players:
      if player not in self.hoi_players:
        self.hoi_players.append(player)
    await ctx.send(f"The players are: {', '.join(self.hoi_players)}.")
  
  @commands.command(name="addc", help="Add country(s) to the HOI teams list")
  async def addc(self, ctx, *args):
    add_country = list(args)
    for country in add_country:
      if country not in self.hoi_countries:
        self.hoi_countries.append(country)
    await ctx.send(f"The countries are: {', '.join(self.hoi_countries)}.")
  
  @commands.command(name="hoi", help="Makes a HOI teams list")
  async def hoi(self, ctx):
    self.teams.clear()
    if len(self.teams) == 0:
      for country in self.hoi_countries:
        self.countries_tmp.append(country)
      for player in self.hoi_players:
        cstr = random.choice(self.countries_tmp)
        self.countries_tmp.remove(cstr)
        self.teams[player] = cstr
      hoi_list = []
      for k, v in self.teams.items():
        hoi_list.append(k + " : " + v)
    await ctx.send(f"The countries are: {', '.join(hoi_list):s}.")


  @commands.command(name="hoiremove", help="Remove user/country from HOI teams")
  async def hoiremove(self, ctx):
    self.reset()
    await ctx.send(f"The teams have been reset {self.teams}")
    
#initalises the hoi cog/
def setup(bot):
  bot.add_cog(hoiC(bot))