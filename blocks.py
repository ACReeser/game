from random import randint

#for k in range(3):
#            traits_orig.append(raw_input("> "))

class drone(object):
    # makes an object and then gives that object a random list of traits
    
    traits_orig = ['is crazy', 'loves music obsessively', 
        'is just waiting for the end of the world', 
        'wants butt seks',
        'loves to cook',
        'hates themself', 'once owned a snake', 'is ugly', 'sucks',
        'killed a man, once', 'thinks life is pointless',
        'loves getting fucked really hard', 'listens to porn',
        'hates old people', 'buried an old guy in their back yard']

    def __init__(self, name):
        self.name = name
        self.temp = drone.traits_orig[:]
        self.odds = []
        self.stress = 0
        self.happy = 0
        self.mood = 'neutral'
        for i in range(4):
            self.odds.append(self.temp.pop(randint(0, len(self.temp) - 1)))

    def change_mood(self, stress_i=0, happy_i=0):
        self.stress += stress_i
        self.happy += happy_i

    def print_mood(self):
        print self.name, "is", self.mood + "."

# makin' babies
bob = drone('Bob')
jane = drone('Jane')

# using list comprehension to copy shared traits into a common list
shared = [x for x in bob.odds if x in jane.odds]

# shows console if any traits are shared
for x in shared:
    print "%s %s, too." % (jane.name, x)

# sets relationship booleans according to shared traits
if len(shared) >= 3:
    compatible = True
    soul_mates = True
elif len(shared) == 2:
    compatible = True
    soul_mates = False
else:
    compatible = False
    soul_mates = False


# prints relationship string based on relationship booleans
if compatible and soul_mates:
    print "We're in love!"
    bob.change_mood(-2, 5)
elif compatible:
    print "We're getting along great!"
    bob.change_mood(-1, 2)
else:
    print "This is ok, i guess..."
    bob.change_mood(0, 0)

bob.print_mood()