#!/usr/bin/env python3

import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=discord.Intents().all())

class teams_rando(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

    self.hoi_players = []
    self.hoi_countries = []
    self.countries_tmp = []
    self.teams = {}


  def reset(self):
    self.teams.clear()
    self.hoi_countries.clear()
    self.countries_tmp.clear()
    self.hoi_players.clear()

  def remove(self, player):
    for k in self.teams.keys():
      if k == player:
            self.hoi_countries.remove(self.teams[k])
            del self.teams[k]
            self.hoi_players.remove(k)
            return f"Removed {player}" 
    return "Could not find player to remove."   
  
  @commands.command(name="addp", help="Add player(s) to the teams list.")
  async def addp(self, ctx, *args):
    add_players = list(args)
    for player in add_players:
      if player not in self.hoi_players:
        self.hoi_players.append(player)
    if len(self.hoi_players) > 0:
      await ctx.send(f"The players are: {', '.join(self.hoi_players)}.")
    else:
      await ctx.send("No players currently exist.")
  
  @commands.command(name="addv", help="Add value(s) to the teams list.")
  async def addv(self, ctx, *args):
    add_country = list(args)
    for country in add_country:
      if country not in self.hoi_countries:
        self.hoi_countries.append(country)
    if len(self.hoi_countries) > 0:
      await ctx.send(f"The values are: {', '.join(self.hoi_countries)}.")
    else:
      await ctx.send("No values currently exist.")
  
  @commands.command(name="tmake", aliases=["maket", "teams"], help="Makes teams.")
  async def teams(self, ctx):
    self.teams.clear()
    hoi_list = []
    if len(self.teams) == 0:
      for country in self.hoi_countries:
        self.countries_tmp.append(country)
      for player in self.hoi_players:
        cstr = random.choice(self.countries_tmp)
        self.countries_tmp.remove(cstr)
        self.teams[player] = cstr
      for k, v in self.teams.items():
        hoi_list.append(k + " : " + v)
    if len(hoi_list) > 0:
      await ctx.send(f"The teams are: {', '.join(hoi_list):s}.")
    else:
      await ctx.send("No teams currently exist.")

  @commands.command(name="treset", help="Reset all teams.")
  async def treset(self, ctx):
    self.reset()
    await ctx.send(f"The teams have been reset {self.teams}")

  @commands.command(name="tremove", aliases=["rmplayer", "removep", "removet"], help="Remove specific player.")
  async def tremove(self, ctx, arg):
    a = self.remove(arg)
    await ctx.send(f"{a}.")

  @commands.command(name="addallies", aliases=["addally", "adda"], help="Adds Hearts of Iron ally countries.")
  async def adddallies(self, ctx):
    if ["United Kingdom", "United States", "France", "Poland"] not in self.hoi_countries:
      self.hoi_countries += ["United Kingdom", "United States", "France", "Poland"]
      await ctx.send(f"Added United Kingdom, United States, France, Poland.")
    else:
      await ctx.send(f"Those teams have already been added.")

  @commands.command(name="addaxis", help="Adds Hearts of Iron axis countries.")
  async def addaxis(self, ctx):
    if ["Germany", "Slovakia", "Italy", "Romania"] not in self.hoi_countries:
      self.hoi_countries += ["Germany", "Slovakia", "Italy", "Romania"]
      await ctx.send(f"Added Germany, Slovakia, Italy, Romania.")
    else:
      await ctx.send(f"Those teams have already been added.")

  @commands.command(name="addcomitern", aliases=["addcomi", "addcommies"], help="Adds Hearts of Iron comitern countries.")
  async def addcomitern(self, ctx):
    if ["Soviet Union"] not in self.hoi_countries:
      self.hoi_countries += ["Soviet Union"]
      await ctx.send(f"Added Soviet Union.")
    else:
      await ctx.send(f"That country is already in the list.")


#initalises the hoi cog/
def setup(bot):
  bot.add_cog(teams_rando(bot))