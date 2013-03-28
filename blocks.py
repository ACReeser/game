from random import randint

traits_orig = ['is crazy', 'loves music obsessively', 
        'is just waiting for the end of the world', 
        'loves you Jesus Chriiiiiiiiiiiiist', 'wants butt seks',
        'loves to cook', 'has a little black book with his poems in',
        'hates themself', 'once owned a snake', 'is ugly', 'sucks',
        'killed a man, once', 'thinks life is pointless']

class drone(object):
    def __init__(self):
        traits = traits_orig
        self.odds = []
        for i in range(3):
            got = randint(0, len(traits) - 1)
            self.odds.append(traits[got])
            traits.remove(traits[got])

bob = drone()
for i in range(len(bob.odds)):
    print "Bob %s." % bob.odds[i]

