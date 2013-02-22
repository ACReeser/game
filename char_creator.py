import os
import random
from random import randint

def explainrace():
  
  racetext = {
  '1' : 'Dwarves usually stand 5 feet high, with a stout build. They pride themselves\n' \
        'on their long head and facial hair. They decorate their beards with clasps\n' \
        'and intricate braids.\n\n' \
        'Dwarves make their homes in sprawling mountain fortresses and cities, where\n' \
        'they pursue their love of stonework, metal craftmanship, architecture, and\n' \
        'drink.\n\n' \
        'Dwarves detest orcs and goblins and generally distrust all other races\n' \
        'save for humans, who can match their industrious nature.',
  '2' : 'Halflings stand only about 3 feet tall and sport hairy feet, which\n' \
        'are usually barefoot, due to their rough and calloused texture. Curly\n' \
        'tufts of hair surround their pointed ears\n\n' \
        'Halflings are nomadic, and claim no homeland, instead living in the\n' \
        'smaller areas of large cities or in small towns.\n\n' \
        'They pride themselves on being all sneaky and stuff, which makes them\n' \
        'really good thieves and other sneaky things like that.',
  '3' : 'Elves suck a dick'
  }

  while 1:
    os.system("clear")
    print """
Enter the number of the race you wish to know about
  Or 'q' to return to the race selection options
---------------------------------------------------
        1 - Dwarf
        2 - Halfling
        3 - Elf
        4 - Human
        5 - Gnome
        6 - Half-Orc
        7 - Half-Elf
        8 - Catfolk
        9 - Goblin
        10 - Orc
    """
    next = raw_input("> ")
    if next in racetext:
      os.system("clear")
      print racetext[(next)]
    elif next == 'q' or next == 'Q':
      break
    raw_input("\nPress ENTER")

class UserMake(object):
  """Wump"""
  def __init__(self, name):
    self.char_abil = [10, 10, 10, 10, 10, 10]
    char_name = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']
    abil_pnts = 15
    go = 0

  def pointbuy(self):
    for i in self.char_abil:
      os.system("clear")
      print "You have %d points left!\n" % abil_pnts
      print char_name[go], "=", self.char_abil[go]
      add = str(raw_input("Add, subtract, or enter 0 "))
      point_list = {'-3':'-4', '-2':'-2', '-1':'-1', '0':'0', '1':'1', '2':'2', '3':'3', '4':'5', '5':'7', '6':'10', '7':'13', '8':'17'}
      if add in point_list.keys():
        if int(add) < abil_pnts or int(add) == abil_pnts:
          abil_pnts = abil_pnts - int(point_list[add])
          self.char_abil[go] = self.char_abil[go] + int(add)
          print "That worked!"
        else:
          print "Number wasn't valid?"
      else:
        print "Number wasn't valid?"
      print char_name[go], "=", self.char_abil[go]
      print self.char_abil
      go += 1
      raw_input("Press ENTER")

  def randroll(self):
    r_nums = range(6)
    for i in r_nums:
      r_fourdsix = range(4)
      go = 0
      for j in r_fourdsix:
        r_fourdsix[go] = randint(1, 6)
        go += 1
      r_nums[i] = (r_fourdsix[0] + r_fourdsix[1] + r_fourdsix[2] + r_fourdsix[3]) - min(r_fourdsix)
    print r_nums
    raw_input("Press ENTER")


mainpc = UserMake(raw_input("Name? "))

while 1:
  print """
Which kind of ability score system would you like to use?
---------------------------------------------------------
1 - Point Buy
2 - Standard
  """
  next = raw_input("> ")
  if int(next) == 1:
    mainpc.pointbuy()
    break
  elif int(next) == 2:
    mainpc.randroll()
    break
  else:
    print "Sorry?"

while 1:
  os.system("clear")
  print """
\nRace Selection
'^^^^^__^^^^^'
-..---::---..-
1 - Dwarf
2 - Halfling
3 - Elf
4 - Human
5 - Gnome
6 - Half-Orc
7 - Half-Elf
8 - Catfolk
9 - Goblin
10 - Orc
-..---::---..-
_vvvvv--vvvvv_
Race Info: 'h'
"""
  next = raw_input("> ")

  if next == "h" or next == "H":
    explainrace()
