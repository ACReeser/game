import sys
from random import randint
import os
import time
import title
import rand_gen

def countdown(message):
  os.system("clear")
  count = 0
  taunts = [
    "I blew a guy, once.",
    "Suck a dick!",
    "I buried them under the north-west corner of the house",
    "2/10 would not play again",
    "Wimp wamp womp.",
    "Beep boop bop.",
    "I'm in love with Ryan Gosling."
  ]
  while count < 3:
    count = count + 1
    message = message + "."
    print message
    time.sleep(0.7)
    os.system("clear")
  print taunts[randint(0, len(taunts)-1)]
  time.sleep(0.5)
  os.system("clear")
  quit()

def import_char():
  from_file = raw_input("What is your character's first name? ")
  from_file = from_file.capitalize() + ".py"
  in_file = open(from_file)
  char_data = in_file.read()
  in_file.close()
  return char_data

def charstats():
    # - This gives the player a text description of their character
    # Needs to be fleshed out to include clothing and equipment
  def descript():
    os.system("clear")
    print "%s is a %s human. %s stands %s, sporting a(n) %s build." % (full_name, gender, p_nom.capitalize(), height, weight)
    print "\nIf you were to ask a lay-person to describe", first_name, "they'd"
    print "say that", p_nom, "has grown", hair, "and that", p_gen, eyes, "pierce"
    print "the soul of anyone around."
  
  # - This prints out the numeric values of the user's stats
  # ... needs to account for worn items and other status effects
  # .... needs vast expansion for skills
  def print_stats():
    os.system("clear")
    print "Here are %s's current stats: " % first_name
    # TK
    # TK

  while 1:
    next = raw_input("Would you like to see your character description, or your stats?\n[1] - Description\n[2] - Stats")
    if next in ['1', '2', "q", "Q"]: break

  if next == '1':
    descript()
  elif next == '2':
    print_stats()
  elif next == "q" or next == "Q":
    pass

def room():
  stuff = {
    'a chair' : 'a wooden chair, with eyeballs carved all up in it',
    'corn' : 'a small pile of corn. It smells delicious and you want to eat it',
    'a sword' : 'a thick sword, that glistens and shit',
  }

  while 1:
    print "You see:\n*  %s\n*  %s\n*  %s" % (stuff.keys()[0], stuff.keys()[1], stuff.keys()[2])
    examine = raw_input("Whaddaya want to examine? ")
    if examine in stuff or examine in ["q", "Q"]: break

  if examine not in ["q", "Q"]:
    print stuff[examine].capitalize()
  else:
    print "Quitting?"

def town():
  print rand_gen.rand_town()

def talk():
  rand_gen.npc_print()

os.system("clear")
title.printtitle()

try:
  exec import_char()
  print first_name +".py", "successfully loaded!"
except:
  os.system("clear")
  print "\n\n\n\n\n\n\n                        Your character has no save file!"
  raw_input()
  os.system("clear")
  quit()

while 1:
  next = raw_input("> ")
  if next in ["room", "charstats", "town", "talk"]:
    exec next + "()"
  elif next in ["Q", "q"]: break
  elif next in ["H", "h"]:
    print title.help()
