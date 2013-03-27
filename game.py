from random import randint
import os

class Room(object):
    def __init__(self, col, row, items):
        self.items = items
        self.grid = []
        self.size = [col, row]
        for i in range(0, self.size[1]):
            self.grid.append(["O"] * self.size[0])

    def draw_grid(self):
        os.system("clear")
        print "\n\n\n"
        print ("-"* ((self.size[0] * 2) + 1)).center(80)
        for i in self.grid:
            print " ".join(i).center(80)
        print ("-"* ((self.size[0] + 2) + 1)).center(80)
        print "\n\n\n"

    def update_grid(self, coor):
        self.grid = []
        for i in range(0, self.size[1]):
            self.grid.append(["O"] * self.size[0])
        self.grid[coor[1]][coor[0]] = "X"

dungeon = Room(5, 5, ['corn'])
dungeon.draw_grid()

class Character(object):
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.position = [0, 0]

    def attack(self, x):
        dam = randint(0, 5)
        x.damage(dam)

    def move(self, direction):
        dirdic = {'8':-1, '2':1, '4':-1, '6':1}
        if direction == '4' or direction == '6':
            test = self.position[0] + dirdic[direction]
            if 4 >= test >= 0:
                self.position[0] = test
            else:
                pass
        elif direction == '8' or direction == '2':
            test = self.position[1] + dirdic[direction]
            if 4 >= test >= 0:
                self.position[1] = test
            else:
                pass

class Item(object):
    def __init__(self, name, descrip, hp, condition):
        self.name = name
        self.descrip = descrip
        self.hp = hp
        self.condition = condition

    def look(self):
        print "You see a " + self.descrip + "."
        print "It is in %s condition." % self.condition
        print "It has %d hit points." % self.hp

    def damage(self, atk):
        if self.hp == 0:
            print "You beat the dead %s like a psychopath." % self.name
        elif (self.hp - atk) <= 0:
            self.hp = 0
            print "You kill the", self.name + "."
        else:
            self.hp -= atk
            print "You hurt the", self.name + "."

in_room = {}
hat = Item("hat", "a black tophat", 5, "terrible")
in_room[hat.name] = hat

player = Character("Jack", 15)

while 1:
    next = raw_input("> ")
    if next == "look":
        print "What would you like to look at?"
        for item in in_room:
            print item
        next1 = raw_input("> ")
        if next1 in in_room:
            in_room[next1].look()
    elif next == "attack":
        print "What would you like to attack?"
        for item in in_room:
            print item
        next2 = raw_input("> ")
        if next2 in in_room:
            player.attack(in_room[next2])
        else:
            print "There is no %s in this room." % next2
    elif next == "move":
        print "Where would you like to move?"
        next3 = raw_input("> ")
        player.move(next3)
        dungeon.update_grid(player.position)
        dungeon.draw_grid()
    elif next.lower() == 'q':
        quit()
