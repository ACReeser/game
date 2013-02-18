import os

def test():
  
  # This will set up the player's ability scores and return it as a list
  
  i = [0, 1, 2, 3, 4, 5]
  char_abil = [10, 10, 10, 10, 10, 10]
  char_name = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']
  abil_pnts = 15
  go = 0

  for i in char_abil:  
    os.system("clear")
    print "You have %d points left!\n" % abil_pnts
    print char_name[go], "=", char_abil[go]
    add = str(raw_input("Add, subtract, or enter 0 "))
    point_list = {'-3':'-4', '-2':'-2', '-1':'-1', '0':'0', '1':'1', '2':'2', '3':'3', '4':'5', '5':'7', '6':'10', '7':'13', '8':'17'}
    if add in point_list.keys():
      if int(add) < abil_pnts or int(add) == abil_pnts:
        
        abil_pnts = abil_pnts - int(point_list[add])
        char_abil[go] = char_abil[go] + int(add)
        print "Successfully Added!"
      else:
        print "You suuuck"
    else:
      print "you suuuuck"
    print char_name[go], "=", char_abil[go]
    print char_abil
    go = go + 1
    raw_input("\nPress ENTER")
  
  return char_abil

def race():
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
  char_race = race_dict[str(raw_input("> "))]
  print char_race

  if char_race == 'Dwarf':
    char_abil[2] = char_abil[2] + 1 # Dwarves get a +1 bonus to CON
  # TK TK TK
  
char_abil = test()
print "STR: %d\nDEX: %d\nCON: %d\nINT: %d\nWIS: %d\nCHA: %d" % (char_abil[0], char_abil[1], char_abil[2], char_abil[3], char_abil[4], char_abil[5])
char_race = race()

