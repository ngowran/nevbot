#!/usr/bin/env python3

import discord
import random
from discord.ext import commands
import os


bot = commands.Bot(command_prefix='!', intents=discord.Intents().all())

face_cards = ["black_joker",
"jack_club.png",
"jack_diamond.png",
"jack_heart.png",
"jack_spade.png",
"king_club.png",
"king_diamond.png",
"king_heart.png",
"king_spade.png",
"queen_club.png",
"queen_diamond.png",
"queen_spade.png",
"red_joker.png"]

special_cards = [
"10_heart.png",
"10_club.png",
"10_diamond.png",
"10_spade.png",
"black_joker",
"jack_club.png",
"jack_diamond.png",
"jack_heart.png",
"jack_spade.png",
"king_club.png",
"king_diamond.png",
"king_heart.png",
"king_spade.png",
"queen_heart.png"
"queen_club.png",
"queen_diamond.png",
"queen_spade.png",
"red_joker.png"
"1_club.png",
"1_diamond.png",
"1_heart.png",
"1_spade.png"]

aces = ["1_club.png",
       "1_diamond.png",
       "1_heart.png",
       "1_spade.png"]

class Casino(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.deck = []
    self.drawn_cards = []
    self.last_drawn = ""
    self.dealer_score = 0
    self.played = 0
    self.test = ""
    self.count = 0
  
  def draw_card(self):
    card_value = 0
    self.deck = [card for card in os.listdir("Other/media/cards") if card not in self.drawn_cards and card != "back.png"]
    card = random.choice(self.deck)
    tokens = card.strip(".png").split("_")
    card_value = tokens[0]
      
    if card_value.isdigit():
      card_value = int(tokens[0])
      self.count += card_value    
    elif card in face_cards:
      self.count += 10

    if card_value == 1 and self.count <= 10:
      self.count += 10
     
    self.dealer_score += random.choice(range(1, 11))
    return card

  def reset(self):
    self.drawn_cards = []
    self.played = 0
    self.dealer_score = 0
    self.count = 0
    self.last_drawn = ""
  
  
  @commands.command(name="blackjack", aliases=["21", "bj"], help="Play blackjack, run command again to hit")
  async def blackjack(self, ctx):
    if self.played == 0:
      self.played += 1
      i = 0
      while i < 2:
        card = Casino.draw_card(self)
        self.drawn_cards.append(card)
        await ctx.send(file=discord.File(f"Other/media/cards/{card}", spoiler=False))
        i += 1
      self.last_drawn = self.drawn_cards[0]
    else:
        card = Casino.draw_card(self)
        self.last_drawn = self.drawn_cards[0]
        self.drawn_cards.append(card)
        await ctx.send(file=discord.File(f"Other/media/cards/{card}", spoiler=False))
      
    await ctx.send(f"You drew: {self.count}")
    if self.count == 21 and self.dealer_score == 21:
      Casino.reset(self)
      await ctx.send("We both got 21. Tie!")
    elif self.count == 21:
      Casino.reset(self)
      await ctx.send("You win! :)")
    elif self.count > 21:
      Casino.reset(self)
      await ctx.send("You went bust. Dealer (me) wins :)")
    elif self.dealer_score > 21:
      await ctx.send(f"Dealer drew {self.dealer_score} and went bust! You win!")
      Casino.reset(self)

  @commands.command(name="bstand", aliases=["stand", "bjs", "bs"], help="Stand on blackjack")
  async def bstand(self, ctx):
    if self.played == 0:
      await ctx.send("Sorry, you haven't played blackjack yet!")
    
    else:
      if self.dealer_score < 17:
        while self.dealer_score <= 17:
          self.dealer_score += random.choice(range(1, 11))
      if self.dealer_score > 21:
        await ctx.send(f"Dealer drew {self.dealer_score} and went bust! You win!")
        Casino.reset(self)
      if self.dealer_score == 21:
        Casino.reset(self)
        await ctx.send("I had 21. Dealer wins :)")
      
      elif self.count > self.dealer_score:
        await ctx.send(f"Dealer had {self.dealer_score}. You win!")
        Casino.reset(self)
      elif self.dealer_score > self.count:
        await ctx.send(f"Dealer had {self.dealer_score}. You lose.")
        Casino.reset(self)

  @commands.command(name="last_draw", aliases=["card", "lastd"], help="Shows second last card drawn [debug tool]")
  async def last_draw(self, ctx):
    if self.played > 0:
      await ctx.send(f"Last card shown: {self.last_drawn}, {self.test}")
    else:
      await ctx.send(f"You haven't played yet you!")

def setup(bot):
  bot.add_cog(Casino(bot))