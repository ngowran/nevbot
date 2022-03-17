#!/usr/bin/env python3

import random
from urllib import request
import os
import discord
from discord.ext import commands

if not os.path.isfile('count_1w.txt'):
    request.urlretrieve(
        "https://norvig.com/ngrams/count_1w.txt",
        "count_1w.txt")

words_list = []

class wordle(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.choice = ""
    self.word_list = []
    self.guess = ["[]", "[]", "[]", "[]", "[]"]
    self.played = 0
    

  def hangemptyman(self, word):
    if word in self.choice:
      self.guess = "[*][*][*][*][*]"
    else:
      words_list.append(word)
      i = 0
      for char in word:
        if char in self.guess:
          self.guess[i] = char
        i += 1
    
    self.played += 1
    return self.guess

  def reset(self):
    self.choice = ""
    self.guess = ["[]", "[]", "[]", "[]", "[]"]

  @commands.command(name="wordle", aliases=["word"], help="play wordle")
  async def wordle(self, ctx, arg):
    i = 0
    with open("count_1w.txt", "r") as f:
      while i <= 5000:
        words = f.readline()
        word, _ = words.strip().split()
        if len(word) == 5:
          words_list.append(word)
        i += 1
        
    if self.played == 0:
      self.choice = random.choice(words_list)
      await ctx.send(f"{''.join(self.choice)}")
      self.played += 1
    
    wordle.hangemptyman(arg)
    await ctx.send({self.guess})
        
    

def setup(bot):
  bot.add_cog(wordle(bot))