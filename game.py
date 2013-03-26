from random import randint

class Room(object):
    def __init__(self, col, row, items):
        self.items = items
        self.grid = []
        for i in range(row):
            self.grid.append("O" * col)

    def draw_grid(self):
        for i in self.grid:
            print i.center(80)

dungeon = Room(5, 5, ['corn'])
dungeon.draw_grid()

class Character(object):
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def attack(self, x):
        dam = randint(0, 5)
        x.damage(dam)

    def move(self, direction):
        self.position

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
    elif next.lower() == 'q':
        quit()
