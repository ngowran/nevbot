#!/usr/bin/env python3

import discord
import random
from discord.ext import commands
import os


bot = commands.Bot(command_prefix='!', intents=discord.Intents().all())

class Casino(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.raw_deck = [card for card in os.listdir("Other/media/cards")]
    self.deck = []
    self.drawn_cards = []
    self.played = 0
    self.count = 0
  
  def draw_card(self, drawncards):
    card_value = 0
    self.deck = [card for card in os.listdir("Other/media/cards") if card not in self.drawn_cards]
    card = random.choice(self.deck)
    if card == "back.png":
      card = random.choice(self.deck)
    tokens = card.strip(".png").split("_")
    if len(tokens) >= 2:
      card_value = tokens[0]
      if card_value.isdigit():
        card_value = int(tokens[0])
      else:
        card_value = 10
      card_suit = tokens[1]
    if self.count == 10:
      if card_value == 1:
        self.count += 11
    else:
      self.count += int(card_value)
    return card

  def reset(self):
    self.drawn_cards = []
    self.played = 0
    self.count = 0
  
  
  @commands.command(name="blackjack", aliases=["21"], help="Play blackjack")
  async def blackjack(self, ctx):
    if self.played == 0:
      self.played += 1
      i = 0
      while i < 2:
        card = Casino.draw_card(self, self.drawn_cards)
        self.drawn_cards.append(card)
        await ctx.send(file=discord.File(f"Other/media/cards/{card}", spoiler=False))
        i += 1
    else:
        card = Casino.draw_card(self, self.drawn_cards)
        self.drawn_cards.append(card)
        await ctx.send(file=discord.File(f"Other/media/cards/{card}", spoiler=False))
      
    await ctx.send(f"You drew: {self.count}")
    if self.count == 21:
      Casino.reset(self)
      await ctx.send("You win. :)")
    if self.count > 21:
      Casino.reset(self)
      await ctx.send("You went bust. Dealer (me) wins :)")



def setup(bot):
  bot.add_cog(Casino(bot))