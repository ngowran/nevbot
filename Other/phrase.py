#!/usr/bin/env python3

sentences = ["bippity boppity. nevbot is on the property.", "hola! nevbot is here.", "nevbot is online! beep boop.", "skyne-- i mean nevbot.. is alive.", "yassss girlies i'm here."]

languages = ["French", "Spanish", "Russian", "Chinese", "Italian", "Japanese", "German", "Portuguese", "Korean", "Arabic", "Danish", "Swahili", "Greek", "Polish", "Indonesian", "Hindi", "Turkish", "Hebrew"]

greetingFormal = ["Bonjour", "Hola", "Zdravstvuyte", "Nǐn hǎo", "Salve", "Konnichiwa", "Guten Tag", "Olá", "Anyoung haseyo", "Asalaam alaikum", "Goddag", "Shikamoo", "Yassas", "Dzień dobry", "Selamat siang", "Namaste", "Merhaba", "Shalom"]

greetingInFormal = ["Salut", "¿Qué tal?", "Privet", "Nǐ hǎo", "Ciao", "Yā, Yō", "Hallo", "Oi", "Anyoung", "Ahlan", "Hej", "Habari", "Yassou", "Cześć", "Halo", "Hai", "Selam", "Hey"]

ftranslate = {}
i = 0
while i < len(languages):
  ftranslate[languages[i]] = greetingFormal[i]
  i = i + 1

itranslate = {}
i = 0
while i < len(languages):
  itranslate[languages[i]] = greetingInFormal[i]
  i = i + 1
