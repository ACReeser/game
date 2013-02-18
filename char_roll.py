import os


class Character(object):
  """Creates a thing"""
  def __init__(self, name):
    
    # This will set up the player's ability scores and return it as a list
    self.name = name
    i = [0, 1, 2, 3, 4, 5]
    self.char_abil = [10, 10, 10, 10, 10, 10]
    char_name = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']
    abil_pnts = 15
    go = 0
  
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
          print "Successfully Added!"
        else:
          print "You suuuck"
      else:
        print "you suuuuck"
      print char_name[go], "=", self.char_abil[go]
      print self.char_abil
      go = go + 1
      raw_input("\nPress ENTER")

  def race(self):
    race_dict = {'1':'Dwarf', '2':'Halfling', '3':'Elf', '4':'Human', '5':'Gnome', '6':'Half-Orc', '7':'Half-Elf'}
    print """
Now pick a race!
----------------
1 - Dwarf
2 - Halfling
3 - Elf
4 - Human
5 - Gnome
6 - Half-Orc
7 - Half-Elf
  """
    self.char_race = race_dict[str(raw_input("> "))]
    print self.char_race
    return self.char_race

    if self.char_race == 'Dwarf':
      char_abil[2] = char_abil[2] + 1 # Dwarves get a +1 bonus to CON
    # TK TK TK
  
def make():
  name = raw_input("Name? > ")
  mainpc = Character(name)
  mainpcname = mainpc.name
  mainpcstats = mainpc.char_abil
  print "STR: %d\nDEX: %d\nCON: %d\nINT: %d\nWIS: %d\nCHA: %d" % (mainpcstats[0], mainpcstats[1], mainpcstats[2], mainpcstats[3], mainpcstats[4], mainpcstats[5])
  mainpc_race = mainpc.race()
  if mainpc_race != "Elf":
    print mainpcname, "is a", mainpc_race.lower() + "."
  elif mainpc_race == "Elf":
    print mainpcname, "is an", mainpc_race.lower() + "."

  print mainpcname, "has a STR score of %d." % (mainpcstats[0])

make()
make()
