import sys
import os
from random import randint
import pickle

#Alex's text-adventure engine
#I'm thinking storing the data in XML and using data-based links between rooms will be the way to go
#I'm still struggling with how the best way is to handle this
#My initial reaction is that individual rooms will be grouped into CLASSES with relevant actions, and that fluff descriptions of them will be separate XML or data files
#this means all our logic will be in the actions, and the particulars will be farmed out
#since it's just python I don't see why we would want to embed any logic in the data itself
#we could if we really had to, either by attributes on XML or by strings that can be eval'd or exec'd on certain events
#	^^ and example of the above: <town onEnter="print('this is coming from the XML!')">
#drawbacks to the above is that we'd have to make sure plenty of things were exposed to the xml which is a pretty big security and stability hole
#
#So that means it'll work like this
#you'll have data files like DarkForest, LightAutumnForest, DarkholmMainStreet, MockinghamLane, TheHawkAndLoveTavern, DagronCave, DarkAlley, BackAlley, etc
#but you'll only have classes Forest, TownStreet, Tavern, Cave, Alley for things that require new interactions
#Each data file could have a big impact, like percentages for random encounters, lists of monsters that could be encountered, kinds of loot there, etc
#we could also introduce a blacklist for actions in the XML to allow some customization of the interaction in the data
#That way we could stop Darkholm from allowing the "sell" action because perhaps there isn't a merchant there.
#and always remember that subclassing is super easy, so making WealthyTownStreet that inherits from TownStreet pretty easy

#LocaleRef is used to list what the PC can move to. They are the "signposts" that provide enough info to move to it
class LocaleReference():
	def __init__(self, displayName, type, shorthand, desc, path):
		self.displayName = name #the exposed name of the locale.
		self.type = type #the CLASSNAME of the locale. this won't be exposed to the user
		self.desc = desc #the description of the 'path' to the locale, not the description of the locale itself. This will be exposed
		self.shorthand = shorthand #usually the way to invoke a move to there. Can be paired with goto or go. Example: NORTH or DOWN or UP or TAVERN
		self.path = path #the path to find the data in XML if we use that for data, or the path to the file we'll be loading

#a Locale is a room that is inhabited sequentially
class Locale():
	#this is a generic function that will allow the text-in to call arbitrary functions on the Locale object provided they are in the validCommands list
	def __getitem__(self, command):
		if command in self.validCommands:
			try:
				m = getattr(self, command)
				if callable(m):
					m()
				else:
					print("You can't do that as an action")
			except AttributeError:
				print("You don't know that.")
		else:
			print("You can't do that")
	#this will be used in sub-classes as a convenience wrapper
	def addValids(self, newCommands):
		self.validCommands.extend(newCommands)
	#add Shorthands is just a utility function
	def addShorthands(self):
		self.shorts = {}
		for ref in self.refs:
			self.shorts[string.upper(ref.shorthand)] = ref
	def __init__(self, myPath, refs):
		#todo load the data for this locale from the path
		self.name = myRef.displayName
		self.description = myRef.desc
		#we'll probably want to 
		self.refs = refs
		self.addShorthands()
		self.validCommands = ["look", "dance", "loot"]
	#enter is a basic event that is called when you move into the room
	def enter(self):
		self.look()
	#these next three are ACTIONS that are exposed to the player
	def loot(self):
		print("There is nothing to loot")
	def look(self):
		#print the basic
		print("You are in a "+self.name)
		print(self.description)
		for ref in self.refs:
			print("")
	def dance(self):
		print("You wiggle about erratically. You should take dancing lessons.")
	
#Two specific instances are example'd here: Town and TreasureTrove. Still working on how to hook them together
class Town(Locale):
	def __init__(self, townName):
		Locale.__init__(self,townName)
		self.addValids(["buy", "sell"])
	def buy(self):
		print("You bought all the things!")
	def sell(self):
		print("You receive a bunch of money from your wares")
		
class TreasureTrove(Locale):
	def __init__(self, name):
		Locale.__init__(self,name)
		#make sure to add "swim" as an action
		self.addValids(["swim"])
		self.loot = ["a shiny sword", "chests o' gold", "dat ass"]
	#we're overridding the loot action
	def loot(self):
		print("You looted "+self.loot[random.randint(0, len(self.loot)-1)] +"!")
	def swim(self):
		print("You swam around in the loot. So gratifying!")

#our game class will include the current setting, the PC, any enemies, the inventory, etc
class Game:
	def __init__(self):
		#currentLocale will have the current context
		self.currentLocale = Town("Mockingham")
		#currentEnemy will have the opposing force. (may need to be a list if you want multiple monsters)
		self.currentEnemy = None
		#currentNPC will have the person you're talking or interacting with
		self.currentNPC = None
	#testing out pickle for serialization
	def save(self):
		saveFile = open("currentLocale.pkl", 'w')
		pickle.dump(self.currentLocale, saveFile)
	def load(self):
		loadFile = open("currentLocale.pkl", 'r')
		self.currentLocale = pickle.load(loadFile)
		self.currentLocale.enter()
		
#and of course, we have our simple game loop
def Loop():
	def gameCall():
		#put other non-Locale specific checks here
		#return True to stop the same command from being passed to the currentLocale
		#maybe this can be another <if in dict> call?
		if (nextCommand == "exit"):
			#TODO: save first and cancel options
			sys.exit()
		elif (nextCommand == "save"):
			game.save()
			return True
		elif(nextCommand == "load"):
			game.load()
			return True
		else:
			return False
	running = True
	game = Game()
	game.currentLocale.enter()
	while(running):
		nextCommand = raw_input("> ")
		if not gameCall():
			game.currentLocale[string.replace(nextCommand, " ", "_")]

#make sure to actually call the game loop at the very end!
Loop()