import os
import random
from random import randint

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

def pointbuy():
  points_l = {
    '-3':'-4', '-2':'-2', '-1':'-1', '0':'0', '1':'1', '2':'2', 
    '3':'3', '4':'5', '5':'7', '6':'10', '7':'13', '8':'17'
  }

  names = ('STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA')
  
  points = 15
  abils = [10] * 6

  for i in range(6):
    os.system("clear")
    
    print """
ABILITY SCORE : POINT COST
--------------------------
-3             -4
-2             -2
-1             -1
 0              0
 1              1
 2              2
 3              3
 4              5
 5              7
 6              10
 7              13
 8              17
    """
    
    print "Points:", points
    
    while 1:
      next = raw_input(names[i] + " = ")

      if next in points_l and int(points_l[next]) <= points:
        abils[i] += int(next)
        points -= int(points_l[next])
        break
      else:
        print "You chose an invalid number!"
      
  os.system("clear")
  return abils

def randroll():
  os.system("clear")
  abils = [0] * 6

  for j in range(6):
    rands = [0] * 4
  
    for i in range(4):
      rands[i] = randint(1, 6)

    abils[j] = rands[0] + rands[1] + rands[2] + rands[3] - min(rands)

  return abils

def assignabils():
  names = ('STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA')
  abilsnew = [0] * 6
  
  for i in range(6):
    while 1:
      os.system("clear")
      print "Assign one of these numbers to your", names[i], "score.\n"
      print abils
      
      next = raw_input("> ")

      try:
        if int(next) in abils:
          abilsnew[i] = int(next)
          abils.remove(int(next))
          break
        elif int(next) not in abils:
          print "You picked a number that's not in the list!"
          raw_input("PRESS ENTER")
      except ValueError:
        if next == 'h' or next == 'H':
          showhelp()
        else:
          print "You picked a number that's not in that list!"
          raw_input("PRESS ENTER")

  return abilsnew

def showabils():
  print """
STR = %d
DEX = %d
CON = %d
INT = %d
WIS = %d
CHA = %d
  """ % (abils[0], abils[1], abils[2], abils[3], abils[4], abils[5])

def showhelp():
  os.system("clear")
  print """
STR measures muscle and physical power
DEX measures agility, reflexes, and balance
CON measures health and stamina
INT determines how well your character learns and reasons
WIS describes a character's willpower, common sense, awareness and intuition
CHA measures a character's personality, personal magnetism, ability to lead, and appearance
  """
  raw_input("PRESS ENTER")

def racebonus():
  def race_c(q,w,e,r,t,y):
    bonus_l = (q, w, e, r, t, y)
    for i in range(6):
      abils[i] += bonus_l[i]

    return abils

  def race_p():
    os.system("clear")
    print "Your current ability scores"
    print "---------------------------"
    showabils()
    print """
Pick One Ability Score To Increase By 2
---------------------------------------
1 - STR
2 - DEX
3 - CON
4 - INT
5 - WIS
6 - CHA
    """
    while 1:
      next = raw_input("> ")
      
      if int(next) - 1 in range(6):
        abils[int(next) - 1] += 2
        break
      else:
        print "You picked an invalid number!"

    return abils

  race_l = ('dwarf', 'halfling', 'elf', 'human', 'gnome', 'half-orc',
    'half-elf', 'catfolk', 'goblin', 'orc')

  while 1:
    os.system("clear")
    
    print """
Race Selection
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
    elif race_l[int(next) - 1] in race_l:
      race = race_l[int(next) - 1]
      if race == "dwarf":
        abilsnew = race_c(0, 0, 2, 0, 2, -2)
      elif race == "halfling":
        abilsnew = race_c(-2, 2, 0, 0, 0, 2)
      elif race == "elf":
        abilsnew = race_c(0, 2, -2, 2, 0, 0)
      elif race == "human":
        abilsnew = race_p()
      elif race == "gnome":
        abilsnew = race_c(-2, 0, 2, 0, 0, 2)
      elif race == "half-orc":
        abilsnew = race_p()
      elif race == "half-elf":
        abilsnew = race_p()
      elif race == "catfolk":
        abilsnew = race_c(0, 2, 0, 0, -2, 0)
      elif race == "goblin":
        abilsnew = race_c(-2, 4, 0, 0, 0, -2)
      elif race == "orc":
        abilsnew = race_c(4, 0, 0, -2, -2, -2)
      break
    else:
      print "You chose an invalid number!"
      raw_input("")

  return abilsnew

while 1:
  os.system("clear")
  print "Which method of ability score generation would you like?"
  print "Enter 'h' for an explanation ability scores"
  print "1 - Point-Buy\n2 - Standard Random Roll"

  next = raw_input("> ")

  if next == "1":
    abils = pointbuy()
    showabils()
    break
  elif next == "2":
    abils = sorted(randroll())
    abils = assignabils()
    showabils()
    break
  elif next == "h" or next == "H":
    showhelp()

os.system("clear")
abils = racebonus()
showabils()