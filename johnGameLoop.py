import sys
import os
from xml.dom.minidom import *
from random import randint
import pickle
import string

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
	def __init__(self, dest, type, cmd, signpost):
		self.destination = dest #the exposed name of the locale.
		self.type = type #the str CLASSNAME of the locale. this won't be exposed to the user
		self.signpost = signpost #the description of the 'path' to the locale, not the description of the locale itself. This will be exposed
		self.command = cmd #usually the way to invoke a move to there. Can be paired with goto or go. Example: NORTH or DOWN or UP or TAVERN
		#self.path = path #the path to find the data in XML if we use that for data, or the path to the file we'll be loading

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
	def __init__(self, name, desc):
		#todo load the data for this locale from the path
		self.name = name
		self.description = desc
		#we'll probably want to 
		self.refs = {}
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
		for k in self.refs.keys():
			print(str(self.refs[k].command)+": "+str(self.refs[k].signpost))
	def dance(self):
		print("You wiggle about erratically. You should take dancing lessons.")
	
#Two specific instances are example'd here: Town and TreasureTrove. Still working on how to hook them together
class TownCenter(Locale):
	def __init__(self, townName, desc):
		Locale.__init__(self,townName, desc)
		self.addValids(["buy", "sell"])
	def buy(self):
		print("You bought all the things!")
	def sell(self):
		print("You receive a bunch of money from your wares")
		
class Tavern(Locale):
	def __init__(self, tavernName, desc):
		Locale.__init__(self,tavernName, desc)
		self.addValids(["beer"])
	def beer(self):
		print("The barmaid doesn't even flinch.")
		
class Tunnel(Locale):
	def __init__(self, tunnelName, desc):
		Locale.__init__(self,tunnelName, desc)
		self.addValids(["fear"])
	def beer(self):
		print("You piss your pants. Weenie.")
		
class TreasureTrove(Locale):
	def __init__(self, troveName, desc):
		Locale.__init__(self,troveName, desc)
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
		self.currentLocale = None
		#currentEnemy will have the opposing force. (may need to be a list if you want multiple monsters)
		self.currentEnemy = None
		#currentNPC will have the person you're talking or interacting with
		self.currentNPC = None
		self.loadMap()
	#testing out pickle for serialization
	def save(self):
		saveFile = open("currentLocale.pkl", 'w')
		pickle.dump(self.currentLocale, saveFile)
	def load(self):
		loadFile = open("currentLocale.pkl", 'r')
		self.currentLocale = pickle.load(loadFile)
		self.currentLocale.enter()
	def findRoom(self, type, name):
		candidateKey = str(type)+"|"+str(name)
		if candidateKey in self.rooms.keys():
			return self.rooms[candidateKey]
	def loadMap(self):
		self.doc = xml.dom.minidom.parse("vanyaville.xml")
		self.rooms = {}
		self.lastRoom = None
		rootNodes = self.doc.getElementsByTagName("rooms")
		for root in rootNodes:
			print('root '+root.tagName)
			for room in root.childNodes:
				print('traversing '+room.tagName)
				self.recurseNode(room, None)
	def recurseNode(self, room, parent):
		if (room.tagName == "link"):
			parent.refs[room.getAttribute("cmd")] = (LocaleReference(room.getAttribute("dest"), room.getAttribute("type"), room.getAttribute("cmd"),  room.getAttribute("signpost")))
		elif (room.tagName =="links"):
			for subRoom in room.childNodes:
				self.recurseNode(subRoom, parent)
		else:
			roomClass = globals()[room.tagName]
			newRoom = roomClass(room.getAttribute("name"), room.getAttribute("desc"))
			if self.currentLocale == None:
				self.currentLocale = newRoom
			self.rooms[room.tagName+"|"+room.getAttribute("name")] = newRoom
			for subRoom in room.childNodes:
				self.recurseNode( subRoom, newRoom)
			
		
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
			#game.save()
			return True
		elif(nextCommand == "load"):
			#game.load()
			return True
		elif nextCommand in game.currentLocale.refs.keys():
			nextLink = game.currentLocale.refs[nextCommand]
			print("You go to "+nextLink.destination)
			game.currentLocale = game.findRoom(nextLink.type, nextLink.destination)
			game.currentLocale.enter()
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