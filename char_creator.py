import os


class Character(object):
  """Wump"""
  def __init__(self, name):
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
          print "That worked!"
        else:
          print "Number wasn't valid?"
      else:
        print "Number wasn't valid?"
      print char_name[go], "=", self.char_abil[go]
      print self.char_abil
      go += 1
      raw_input("Press ENTER")
