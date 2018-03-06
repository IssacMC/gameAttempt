import items


class Enemy:
	name = "Do not create raw enemies!"
	description = "There is no description here because you should not create raw Enemy objects!"
	attack_description = "There is no attack_description here because you should not create raw Enemy objects!"
	
	hp = 0
	damage = 0
	
	loot = []

	weakness = 0
	
	agro = False	# Used to cause enemies to attack spontaneously.
	
	def __init__(self, direction = None, loot = []):
		if(direction == 'n'):
			self.direction = 'north'
		elif(direction == 's'):
			self.direction = 'south'
		elif(direction == 'e'):
			self.direction = 'east'
		elif(direction == 'w'):
			self.direction = 'west'
		else:
			self.direction = None


	def __str__(self):
		return self.name
		
	def check_text(self):
		text = ""
		if(self.direction):
			text = "A %s is blocking your progress to the %s." % (self.name, self.direction)
		text += " " + self.description			
		return text

	def take_damage(self, amount):
		self.hp -= amount
		if(self.hp <= 0):
			self.hp = 0
			defeat_text = "The %s is defeated." % self.name
			if(len(self.loot) > 0):
				defeat_text += " It dropped the following items: "
				for item in self.loot:
					defeat_text += "* " + str(item)
			return defeat_text
		else:
			return "The %s took %d damage." % (self.name, amount)
			
	def is_alive(self):
		return self.hp > 0
		
	def handle_input(self, verb, noun1, noun2, inventory):
		return [False, None, inventory]

	
	def take_damage(self, amount):
		self.hp -= amount
		if(self.hp <= 0):
			self.hp = 0
			defeat_text = "The %s is defeated." % self.name
			if(len(self.loot) > 0):
				defeat_text += " It dropped the following items: "
				for item in self.loot:
					defeat_text += "* " + str(item)
			return defeat_text
		else:
			return "The %s took %d damage." % (self.name, amount)

class Two(Enemy):
	name = "Two"
	description = "A girl stands here. She seems to not want to kill you."
	hp = 1
	damage = 1


class Three(Enemy):
	name = "Three"
	description = "A man confronts you. He weilds some sort of blade."
	hp = 1
	damage = 1
	

class Four(Enemy):
	name = "Four"
	#if(TurnCount>40):
	description = "A police detective. He seems to mean you harm"
	hp = 1
	damage = 1
	#else:
	#	desription = "A police detective. He says that he's on the side of the law, and means you no harm"
	#	hp = 1
	#	damage = 0

class Five(Enemy):
	name = "Five"
	description = "A small child. He seems innocent enough."
	hp = 1
	damage = 1


class Six(Enemy):
	name = "Five"
	description = "A small child. He seems innocent enough."
	hp = 1
	damage = 1	
	
class Seven(Enemy):
	name = "Five"
	description = "A small child. He seems innocent enough."
	hp = 1
	damage = 1

class Eight(Enemy):
	name = "Five"
	description = "A small child. He seems innocent enough."
	hp = 1
	damage = 1

class Nine(Enemy):
	name = "Five"
	description = "A small child. He seems innocent enough."
	hp = 1
	damage = 1
class Ten(Enemy):
	name = "Five"
	description = "A small child. He seems innocent enough."
	hp = 1
	damage = 1
class Eleven(Enemy):
	name = "Five"
	description = "A small child. He seems innocent enough."
	hp = 1
	damage = 1
class Twelve(Enemy):
	name = "Five"
	description = "A small child. He seems innocent enough."
	hp = 1
	damage = 1

