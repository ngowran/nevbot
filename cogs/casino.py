#!/usr/bin/env python3

import discord
import random
from discord.ext import commands
import os


bot = commands.Bot(command_prefix='!', intents=discord.Intents().all())

class Deck(object):
  def __init__(self):
    self.raw_deck = [card for card in os.listdir("../other/media/cards")]
    self.count = 0
  
  def draw_card(self):
    card = random.choice(self.raw_deck)
    tokens = card.strip(".png").split("_")
    if len(tokens) > 2:
      card_value = tokens[0]
      if card_value.isdigit():
        card_value = int(tokens[0])
      else:
        card_value = 10
      card_suit = tokens[1]
    self.count += int(card_value)
    return card

class Casino(commands.Cog):
  def __init__(self, bot):
    self.bot = bot




def setup(bot):
  bot.add_cog(Casino(bot))