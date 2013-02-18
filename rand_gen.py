import random
from random import randint
#Pathfinder gen tables

def npc_print():
  def npc_phy(): #add params for generating just stats/just phys
      # a big-ass table of npc physical characteristics, to be rolled
    npc_phys_list = [
    
    "has warts", "has bad breath", "has a big nose", "has long fingers",
    "has stubby fingers", "has boils", "is very clean", "has very white teeth",
    "has dazzling eyes", "has a sweet smile", "has beautiful curves",
    "has dirty nails", "has dirty hands", "has calloused hands",
    "wears an eye patch", "has a glass eye", "has enormous sideburns",
    "has yellowed teeth", "scratches frequently", "sneezes constantly",
    "blinks compulsively", "is a nervous nail-biter", "has a hair color that is obviously fake",
    "avoids eye contact", "sweats a lot", "giggles all the time",
    "has a hobbled gait", "is jolly looking", "is an incessant knuckle-cracker",
    "whistles when talking", "is cross-eyed", "is harelipped", "has rotten teeth",
    "is generally filthy", "is tattooed all over", "has a face tattoo",
    "has one pierced ear", "has a pierced nose", "has pierced ears",
    "has a pierced lip", "has a tribal forearm tattoo", "winks a lot",
    "has a hacking cough", "spits constantly", "has dreadlocks",
    "has different colored eyes", "is missing teeth", "is scarred",
    "twitches all the time", "laughs nervously", "has a lisp",
    "has a limp", "is missing an eye", "is missing a finger",
    "has a scarred face", "has no teeth", "is missing all fingers on one hand",
    "is bald", "is slightly balding", "has a combed-over bald patch",
    "has a shaved head", "has curly hair", "has long hair", "has short hair",
    "has blonde hair", "has black hair", "has red hair", "has grey hair",
    "has big ears", "is fat", "is tall", "is thin", "is short",
    "is homely", "is handsome", "is beautiful", "has a moustache",
    "has a beard", "is stubbly", "is obscenely fat", "is strangely tall",
    "is unusually short", "is double-chinned", "is thin-lipped",
    "is very hairy", "has a unibrow", "is wide-mouthed", "is missing a hand",
    "is club-footed", "is missing a leg", "is missing an arm", "has horrible facial scars",
    "has clawed hands", "has webbed hands", "is scarred from pox",
    "has terrible facial disease", "is covered in cysts",
    "is covered in pustules", "has a major deformity that no one mentions",
    "always brings a friend to parties, but never brings beer",
  
    ]

    npc_stats = [
  
    randint(1, 8),
    randint(1, 8),
    randint(1, 8),
    randint(1, 8)

    ]

    npc_gend = randint(0, 1)
    npctrait1 = npc_phys_list[randint(0, len(npc_phys_list) - 1)]
    npctrait2 = npc_phys_list[randint(0, len(npc_phys_list) - 1)]
  
    if npc_gend == 0:
      npc_nom = "she"
      npc_acc = "her"
      npc_gen = "her"
      npc_sex = "female"
    elif npc_gend == 1:
      npc_nom = "he"
      npc_acc = "him"
      npc_gen = "his"
      npc_sex = "male"
  
    return [npc_nom, npc_acc, npc_gen, npc_sex, npctrait1, npctrait2, npc_stats]
  
  rand_npc = npc_phy()
  print rand_npc[0].capitalize(), rand_npc[4], "and", rand_npc[5] + "."
  print """
STR: %d
DEX: %d
CON: %d
INT: %d""" % (rand_npc[6][0], rand_npc[6][1], rand_npc[6][2], rand_npc[6][3])

  # FUTURE SHIT: PAY ATTENTION
  # Maybe make this so that the function will write out this info
  #  to a file, so that you can revisit the same person. Like, give
  #  em a name and everything. Save it under PLAYER.NPCS.py or smth


# This returns a string that describes a random town with 2
# distinguishing features, and that's it. Should output town_dec
# keys, too, but that'll come later, when towns decorations
# have an effect on which objects and characters the player can
# interact with

def rand_town():
  town_dec = {

  "a three-headed gargoyle fountain" : "This fountain depicts a ferocious three-headed gargoyle, mouth gaping open, vomiting out water.",
  "two giant stone feet" : "Two enormous stone feet lay broken off at the ankle. A large statue once stood here, but it is long gone",
  "a 15 meter high iron column" : "A perfectly cast column of iron stabs 15 meters into the heavens, signifying gods-know-what.",
  "an unused guillotine" : "Ancient blood clings to a nearby guillotine, which has been in disuse for a very, very long time, it would seem.",
  "an ornate fresco" : "Scenes of death and destruction streak across an ornate fresco. Women and children can be seen screaming and running away from terrifying monsters",
  "colorless streets" : "Across the entire town, barely a speck of color can be seen.",
  "a unicorn hologram" : "Upon closer inspection, this hologram shows a nude godess riding atop a mighty unicorn.",
  "a rainbow unicorn hologram" : "Upon closer inspection, this hologram shows a nude god atop a mighty unicorn.",
  "a pile of dead bodies" : "A pile of dead bodies cooks in the sun, letting off a ridiculously bad aroma.",
  "bustling crowds" : "You can barely make your way through the town, it's so crowded.",
  "a giant flying penis" : "Above the city you spot an enormous levitating dick. It makes you feel uneasy."

  }
  towntrait1 = random.choice(town_dec.keys())
  towntrait2 = random.choice(town_dec.keys())
  return "This town has %s and %s.\n" % (towntrait1, towntrait2) + town_dec[towntrait1] + "\n" + town_dec[towntrait2]
  # town is holding election but no one cares cuz haha politics same person wins
  # other funny satirical shit

def rand_enem():
  enem_list = {

  "butts" : "ayo butts", 

  }

npc_print()
print rand_town()
