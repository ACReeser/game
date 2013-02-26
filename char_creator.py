import os
import random
from random import randint

def racebonus(q, w, e, r, t, y):
  mainpc.char_abil[0] += q
  mainpc.char_abil[1] += w
  mainpc.char_abil[2] += e
  mainpc.char_abil[3] += r
  mainpc.char_abil[4] += t
  mainpc.char_abil[5] += y
  char_abilreturn = mainpc.char_abil
  return char_abilreturn

def pickracebonus():
  os.system("clear")
  print """
1 - STR = %d
2 - DEX = %d
3 - CON = %d
4 - INT = %d
5 - WIS = %d
6 - CHA = %d
\nChoose an ability score to increase by 2
""" % (mainpc.char_abil[0], mainpc.char_abil[1], mainpc.char_abil[2], mainpc.char_abil[3], mainpc.char_abil[4], mainpc.char_abil[5])
  b = raw_input("> ")
  mainpc.char_abil[int(b) - 1] = mainpc.char_abil[int(b) - 1] + 2
  char_abilreturn = mainpc.char_abil
  return char_abilreturn


def explainrace():
  
  racetext = {
  '1' : 'Dwarves usually stand 5 feet high, with a stout build. They pride themselves\n' \
        'on their long head and facial hair. They decorate their beards with clasps\n' \
        'and intricate braids.\n\n' \
        'Dwarves make their homes in sprawling mountain fortresses and cities, where\n' \
        'they pursue their love of stonework, metal craftsmanship, architecture, and\n' \
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
  '3' : 'Elves are tall, graceful creatures with long, pointed ears. Most\n' \
        'feel a bond with nature, and as thus look down on manipulating earth\n' \
        'and stone, feeling more inclined towards finer arts, such as wizardry\n\n' \
        'Though they look down on most other races, elves are good judges of\n' \
        'character, and will admit when someone they may not like is right or\n' \
        'even of a certain value.',
  '4' : 'Humans are very versatile creatures, living in all types of environments\n' \
        'and under many different conditions. An average human stands 5 and a half\n' \
        'feet tall, but humans come in all types of shapes and sizes.\n\n' \
        'But to be honest, you are a human, so you know all of this already, so\n' \
        'so why are you even reading this help page about humans in the first place?',
  '5' : 'Straight up, gnomes eat penises.',
  '6' : 'Half-Orcs are vicious creatures, but belong neither to humans nor orcs.',
  '7' : 'Since Half-Elves are looked down on by humans and elves alike, they know\n' \
        'loneliness and are more open to accepting others, as a result.',
  '8' : 'Catfolk are tribal hunter-gatherers who dwell in harmony with nature, though\n' \
        'some have acclimated well to urban environments. They are lithe, catlike\n' \
        'humanoids with long tails and pointed ears. Their feline eyes are vertical.\n' \
        '\nPersonal growth is part of catfolk culture, and they have few taboos.\n' \
        'They often exhibit harmless but strange eccentricities due to this.',
  '9' : 'Goblins are three feet tall, but they are made distinctive by their huge\n' \
        'heads, which dwarf their bodies. They prefer to live in caves, amid large\n' \
        'and dense thickets of thistles and brambles, or in structures built, and\n' \
        'then abandoned by others.\n\n' \
        'Goblins are voracious eaters, and their lairs will usually have storerooms\n' \
        'and larders to fulfill their appetites. They are universally illiterate.',
  '10': 'stuff goes here'
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
    self.name = name

  def pointbuy(self):
    for i in self.char_abil:
      os.system("clear")
      print "You have %d points left!\n" % abil_pnts
      print char_name[go], "=", self.char_abil[go]
      add = str(raw_input("Add, subtract, or enter 0 "))
      point_list = {'-3':'-4', '-2':'-2', '-1':'-1', '0':'0', '1':'1', '2':'2', 
      '3':'3', '4':'5', '5':'7', '6':'10', '7':'13', '8':'17'}
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
      return self.char_abil

  def randroll(self):
    r_nums = range(6)
    for i in r_nums:
      r_fourdsix = range(4)
      go = 0
      for j in r_fourdsix:
        r_fourdsix[go] = randint(1, 6)
        go += 1
      r_nums[i] = (r_fourdsix[0] + r_fourdsix[1] + r_fourdsix[2] + r_fourdsix[3]) - min(r_fourdsix)
    
    print "Assign values to ability scores:"
    raw_input("Press ENTER")
    for i in range(6):
      new_range = [0, 0, 0, 0, 0, 0]
      go = 0
      print """
STR = %d
DEX = %d
CON = %d
INT = %d
WIS = %d
CHA = %d\n\n
      """ % (new_range[0], new_range[1], new_range[2], new_range[3], new_range[4], new_range[5])
      print "Your remaining scores to assign:\n" \
            "1 - %d\n2 - %d\n3 - %d\n4 - %d\n5 - %d\n6 - %d" % (r_nums[0], r_nums[1], r_nums[2], r_nums[3], r_nums[4], r_nums[5])
      print "%s Score: " % go in ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']
      next = int(raw_input("> "))
      if next in r_nums:
        new_range[go] = str(next)
        print new_range
        r_nums[go] = 0
      else:
        print "You blow."

    return r_nums
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
    mainpc.char_abil = mainpc.pointbuy()
    break
  elif int(next) == 2:
    mainpc.char_abil = mainpc.randroll()
    print mainpc.char_abil
    raw_input()
    break
  else:
    os.system("clear")


while 1:
  os.system("clear")
  racematch = {'1':'Dwarf','2':'Halfling','3':'Elf','4':'Human','5':'Gnome',
  '6':'Half-Orc','7':'Half-Elf','8':'Catfolk','9':'Goblin','10':'Orc'}
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
  elif next in racematch:
    race = racematch[next].lower()
    break

print race

if race == 'dwarf':
  char_abil = racebonus(0, 0, 2, 0, 2, -2)
elif race == 'elf':
  char_abil = racebonus(0, 2, -2, 2, 0, 0)
elif race == 'gnome':
  char_abil = racebonus(-2, 0, 2, 0, 0, 2)
elif race == 'half-elf':
  char_abil = pickracebonus()
elif race == 'half-orc':
  char_abil = pickracebonus()
elif race == 'human':
  char_abil = pickracebonus()
elif race == 'halfling':
  char_abil = racebonus(-2, 2, 0, 0, 0, 2)
elif race == 'goblin':
  char_abil = racebonus(-2, 4, 0, 0, 0, -2)
elif race == 'orc':
  char_abil = racebonus(4, 0, 0, -2, -2, -2)
elif race == 'catfolk':
  char_abil = racebonus(0, 2, 0, 0, -2, 2)

char_abil_verbose = """
STR = %d
DEX = %d
CON = %d
INT = %d
WIS = %d
CHA = %d
""" % (char_abil[0], char_abil[1], char_abil[2], char_abil[3], char_abil[4], char_abil[5])

print "%s is a %s." % (mainpc.name.capitalize(), race)
print char_abil_verbose