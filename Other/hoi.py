#!/usr/bin/env python3

import random

players = ["The Romanian", "Kevin MC", "Ben", "Lucas", "Alex", "Nev", "Yaraslav", "Niall"]

countries = ["Germany", "Italy", "Sweden", "France", "England", "America", "Romania", "Japan", "Soviet Union"]

dic_1 = {} 

def hoi_randomiser():
  i = 0
  while i < len(players):
    for player in players:
      player_choice = random.choice(players)
      countries_choice = random.choice(countries)

      if player_choice not in dic_1 and countries_choice not in dic_1.values():
        dic_1[player_choice] = countries_choice
      
      while player_choice in dic_1 and countries_choice in dic_1.values():
        if player_choice not in dic_1 and countries_choice not in dic_1.values():
          dic_1[player_choice] = countries_choice
        
        player_choice = random.choice(players)
        countries_choice = random.choice(countries)
    
    if len(dic_1) == len(players):
      i == len(players)
    i = i + 1
  return(dic_1)

hoi_randomiser()

dic = {}
for x in players:   
  pstr = random.choice(players)
  cstr = random.choice(countries)
  if pstr not in dic and cstr not in dic:
    dic[pstr] = cstr

print(dic)