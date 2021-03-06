import items
import enemies
import barriers


from random import randint 	# Used to generate random integers.

Two = enemies.Two()			# I'm attempting a global enemy, may God help us all.
Three = enemies.Three()
Four = enemies.Four()
Eight = enemies.Eight()

Sorry = enemies.Sorry()

Mirror = items.Mirror()
Rock = items.Rock()

class MapTile:
	description = "Do not create raw MapTiles! Create a subclass instead!"
	barriers = []
	enemies = []
	items = []

	
	def __init__(self, x=0, y=0, barriers = [], items = [], enemies = []):
		self.x = x
		self.y = y
		for barrier in barriers:
			self.add_barrier(barrier)
		for item in items:
			self.add_item(item)
		for enemy in enemies:
			self.add_enemy(enemy)
	
	def intro_text(self):
		text = self.description
		directions_blocked = []
		
		for enemy in self.enemies:
			if (enemy.direction):
				if(enemy.direction not in directions_blocked):
					directions_blocked.append(enemy.direction)
			text += " " + enemy.check_text()
		for barrier in self.barriers:
			if (barrier.direction):
				if(barrier.direction not in directions_blocked):
					if(barrier.verbose):
						text += " " + barrier.description()
		
		for item in self.items:
			text += " " + item.room_text()

		return text
		
	def handle_input(self, verb, noun1, noun2, inventory):
		if(not noun2):
			if(verb == 'check'):
				for barrier in self.barriers:
					if(barrier.name):
						if(barrier.name.lower() == noun1):
							return [True, barrier.description(), inventory]
				for item in self.items:
					if(item.name.lower() == noun1):
						return [True, item.check_text(), inventory]
				for enemy in self.enemies:
					if(enemy.name.lower() == noun1):
						return [True, enemy.check_text(), inventory]
				
			elif(verb == 'take'):
				for index in range(len(self.items)):
					if(self.items[index].name.lower() == noun1):
						if(isinstance(self.items[index], items.Item)):
							pickup_text = "You picked up the %s." % self.items[index].name
							inventory.append(self.items[index])
							self.items.pop(index)
							return [True, pickup_text, inventory]
						else:
							return [True, "The %s is too heavy to pick up." % self.items[index].name, inventory]
			elif(verb == 'drop'):
				for index in range(len(inventory)):
					if(inventory[index].name.lower() == noun1):
						inventory[index].is_dropped = True
						drop_text = "You dropped the %s." % inventory[index].name
						self.add_item(inventory[index])
						inventory.pop(index)
						return [True, drop_text, inventory]

		
			
		return [False, "", inventory]
		
	def add_barrier(self, barrier):
		if(len(self.barriers) == 0):
			self.barriers = [barrier]		# Initialize the list if it is empty.
		else:
			self.barriers.append(barrier)	# Add to the list if it is not empty.
			
	def add_item(self, item):
		if(len(self.items) == 0):
			self.items = [item]		# Initialize the list if it is empty.
		else:
			self.items.append(item)	# Add to the list if it is not empty.
			
	def add_enemy(self, enemy):
		if(len(self.enemies) == 0):
			self.enemies = [enemy]		# Initialize the list if it is empty.
		else:
			self.enemies.append(enemy)	# Add to the list if it is not empty.
			
	
			
	def random_spawn(self):
		pass						# Update this for your specific subclass if you want randomly spawning enemies.
			
	def update(self, player):
		dead_enemy_indices = []
		for index in range(len(self.enemies)):
			if (not self.enemies[index].is_alive()):
				dead_enemy_indices.append(index)
				for item in self.enemies[index].loot:
					self.add_item(item)
		for index in reversed(dead_enemy_indices):
			self.enemies.pop(index)
		if(self.x == player.x and self.y == player.y):
			for enemy in self.enemies:
				if(enemy.agro):
					agro_text = "The %s seems very aggitated. It attacks! " % enemy.name
					agro_text += player.take_damage(enemy.damage)
					print()
					print(agro_text)



	
	def __init__(self, x=0, y=0, barriers = [], items = [], enemies = []):	# Since this tile appears so much, I gave it its own __init__() function to add random flavor text to some of the tiles.
		self.x = x
		self.y = y
		for barrier in barriers:
			self.add_barrier(barrier)
		for item in items:
			self.add_item(item)
		for enemy in enemies:
			self.add_enemy(enemy)

	
	def intro_text(self):	# Since this tile appears so much, I gave it its own intro_text function to make its text more descriptive.
		text = self.description
			
		directions_clear = ['north', 'south', 'east', 'west']
		for barrier in self.barriers:
			try:
				directions_clear.pop(directions_clear.index(barrier.direction))		# Attempt to remove the barrier's direction from the list of clear directions.
			except:
				pass		# If the barrier direction is not in the list of clear directions already, then we ignore it.
		#for enemy in self.contents['enemies']:
		#	text += " " + enemy.description()
		
		if(len(directions_clear) == 1):
			text += " There is a clear pathway leading to the %s." % directions_clear[0]
		elif(len(directions_clear) == 2):
			text += " There are clear pathways leading to the %s and %s." % (directions_clear[0], directions_clear[1])
		elif(len(directions_clear) == 3):
			text += " There are clear pathways leading to the %s, %s, and %s." % (directions_clear[0], directions_clear[1], directions_clear[2])
		elif(len(directions_clear) == 4):
			text += " It appears that your path is clear in all directions." 
		
		directions_blocked = []
		
		for enemy in self.enemies:
			if (enemy.direction):
				if(enemy.direction not in directions_blocked):
					directions_blocked.append(enemy.direction)
			text += " " + enemy.check_text()
		for barrier in self.barriers:
			if (barrier.direction):
				if(barrier.direction not in directions_blocked):
					if(barrier.verbose):
						text += " " + barrier.description()
		
		for item in self.items:
			text += " " + item.room_text()
		return text
	
		
class StartingTile(MapTile):
	items = [items.Darts()]
	description = "You find yourself surrounded by nothing."

class Street(MapTile):
	description = "There is nothing here. Literally nothing. Its an empty void. You don't even know how you're traversing it honestly"

class ZoneTwo(MapTile):
	global Two
	global Mirror
	enemies = [Two]
	description = "A... normal setting? It seems to be a street corner."
	items = [Mirror]
class ZoneThree(MapTile):
	global Three
	global Rock
	enemies = [Three]
	description = "A bright light fills your vision. There appears to be a massive bonfire."
	items = [Rock]
class ZoneFour(MapTile):
	global Water
	global Four
	enemies = [Four]
	description = "A room filled with massive pillars of marble. It looks pretty cool, honestly."

class Field(MapTile):
	description = "An open field. Its quite peaceful here."

class Refuge(MapTile):
	description = "A plain building, seems like it would be a nice place to rest"
	items = [items.Water()]	

class Final(MapTile):
	global Eight
	description = "There appears to be a room further beyond."
	enemies = [Eight]

class Hmm(MapTile):
	global Sorry
	description = "You've made a mistake."
	enemies = [Sorry]

class VictoryTile(MapTile):
	description = "You've reached the end. Victory is yours!"

class World:	
	map = [
		[VictoryTile(),Hmm()    ,ZoneFour(),ZoneFour(),Street()  ,Street()    ,Street() ,Street(),Street() ,Hmm()],
		[Final()      ,Final()  ,ZoneFour(),ZoneFour(),Street()  ,Street()    ,Street() ,Street(),Street() ,Street()],
		[Street()     ,Street() ,Street()  ,ZoneFour(),Street()  ,Street()    ,Street() ,Street(),Street() ,Street()],
		[ZoneFour()     ,ZoneFour() ,Street()  ,ZoneFour(),ZoneThree(),ZoneThree(),Street() ,Street(),Street() ,Street()],
		[Street()     ,Hmm()    ,Street()  ,ZoneFour(),ZoneThree(),ZoneThree(),Street() ,Street(),Street() ,Street()],
		[Street()     ,Street() ,Street()  ,ZoneFour(),ZoneThree(),ZoneThree(),Street() ,Street(),ZoneTwo(),ZoneTwo()],
		[Street()     ,Street() ,Street()  ,ZoneFour(),Street()  ,Street()    ,Street() ,Street(),ZoneTwo(),ZoneTwo()],
		[Field()      ,Field()  ,Field()   ,Street()  ,Street()  ,Street()    ,Street() ,Street(),Street() ,Street()],
		[Field()      ,Field()  ,Field()   ,Street()  ,Street()  ,Street()    ,Street() ,Street(),Street() ,Street()],
		[Refuge()     ,Field()  ,Field()   ,Street()  ,Hmm()     ,Street()    ,Street() ,Street(),Street() ,StartingTile()]
	]

	def __init__(self):
		for i in range(len(self.map)):			# We want to set the x, y coordinates for each tile so that it "knows" where it is in the map.
			for j in range(len(self.map[i])):	# I prefer to handle this automatically so there is no chance that the map index does not match
				if(self.map[i][j]):				# the tile's internal coordinates.
					self.map[i][j].x = j
					self.map[i][j].y = i
					
					self.add_implied_barriers(j,i)	# If there are implied barriers (e.g. edge of map, adjacent None room, etc.) add a Wall.
						
					
	def tile_at(self, x, y):
		if x < 0 or y < 0:
			return None
		try:
			return self.map[y][x]
		except IndexError:
			return None
			
	def check_north(self, x, y):
		for enemy in self.map[y][x].enemies:
			if(enemy.direction == 'north'):
				return [False, enemy.check_text()]		
		for barrier in self.map[y][x].barriers:
			if(barrier.direction == 'north' and not barrier.passable):
				return [False, barrier.description()]				
				
		if y-1 < 0:
			room = None
		else:
			try:
				room = self.map[y-1][x]
			except IndexError:
				room = None
		
		if(room):
			return [True, "You head to the north."]
		else:
			return [False, "There doesn't seem to be a path to the north."]
			
	def check_south(self, x, y):
		for enemy in self.map[y][x].enemies:
			if(enemy.direction == 'south'):
				return [False, enemy.check_text()]		
		for barrier in self.map[y][x].barriers:
			if(barrier.direction == 'south' and not barrier.passable):
				return [False, barrier.description()]	
				
		if y+1 < 0:
			room = None
		else:
			try:
				room = self.map[y+1][x]
			except IndexError:
				room = None
		
		if(room):
			return [True, "You head to the south."]
		else:
			return [False, "There doesn't seem to be a path to the south."]

	def check_west(self, x, y):
		for enemy in self.map[y][x].enemies:
			if(enemy.direction == 'west'):
				return [False, enemy.check_text()]		
		for barrier in self.map[y][x].barriers:
			if(barrier.direction == 'west' and not barrier.passable):
				return [False, barrier.description()]	
	
		if x-1 < 0:
			room = None
		else:
			try:
				room = self.map[y][x-1]
			except IndexError:
				room = None
		
		if(room):
			return [True, "You head to the west."]
		else:
			return [False, "There doesn't seem to be a path to the west."]
			
	def check_east(self, x, y):
		for enemy in self.map[y][x].enemies:
			if(enemy.direction == 'east'):
				return [False, enemy.check_text()]		
		for barrier in self.map[y][x].barriers:
			if(barrier.direction == 'east' and not barrier.passable):
				return [False, barrier.description()]	
				
		if x+1 < 0:
			room = None
		else:
			try:
				room = self.map[y][x+1]
			except IndexError:
				room = None
		
		if(room):
			return [True, "You head to the east."]
		else:
			return [False, "There doesn't seem to be a path to the east."]
			
	def add_implied_barriers(self, x, y):

		[status, text] = self.check_north(x,y)
		barrier_present = False
		if(not status):
			for enemy in self.map[y][x].enemies:
				if enemy.direction == 'north':
					barrier_present = True
			for barrier in self.map[y][x].barriers:
				if barrier.direction == 'north':
					barrier_present = True
			if(not barrier_present):
				self.map[y][x].add_barrier(barriers.Wall('n'))	
				
		[status, text] = self.check_south(x,y)
		barrier_present = False
		if(not status):
			for enemy in self.map[y][x].enemies:
				if enemy.direction == 'south':
					barrier_present = True
			for barrier in self.map[y][x].barriers:
				if barrier.direction == 'south':
					barrier_present = True
			if(not barrier_present):
				self.map[y][x].add_barrier(barriers.Wall('s'))	
			
		[status, text] = self.check_east(x,y)
		barrier_present = False
		if(not status):
			for enemy in self.map[y][x].enemies:
				if enemy.direction == 'east':
					barrier_present = True
			for barrier in self.map[y][x].barriers:
				if barrier.direction == 'east':
					barrier_present = True
			if(not barrier_present):
				self.map[y][x].add_barrier(barriers.Wall('e'))	
			
		[status, text] = self.check_west(x,y)
		barrier_present = False
		if(not status):
			for enemy in self.map[y][x].enemies:
				if enemy.direction == 'west':
					barrier_present = True
			for barrier in self.map[y][x].barriers:
				if barrier.direction == 'west':
					barrier_present = True
			if(not barrier_present):
				self.map[y][x].add_barrier(barriers.Wall('w'))	
		
	def update_rooms(self, player):
		for row in self.map:
			for room in row:
				if(room):
					room.update(player)
	
