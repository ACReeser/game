from random import randint

traits_orig = ['is crazy', 'loves music obsessively', 
        'is just waiting for the end of the world', 
        'wants butt seks',
        'loves to cook',
        'hates themself', 'once owned a snake', 'is ugly', 'sucks',
        'killed a man, once', 'thinks life is pointless',
        'loves getting fucked really hard', 'listens to porn',
        'hates old people', 'buried an old guy in their back yard']

#for k in range(3):
#            traits_orig.append(raw_input("> "))

class drone(object):
    # makes an object and then gives that object a random list of traits
    def __init__(self):
        self.temp = traits_orig[:]
        self.odds = []
        for i in range(4):
            self.odds.append(self.temp.pop(randint(0, len(self.temp) - 1)))

# makin' babies
bob = drone()
jane = drone()

# using list comprehension to copy shared traits into a common list
shared = [x for x in bob.odds if x in jane.odds]

# shows console if any traits are shared
for x in shared:
    print "Jane", x + ", too."

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
elif compatible:
    print "We're getting along great!"
else:
    print "This is ok, i guess..."