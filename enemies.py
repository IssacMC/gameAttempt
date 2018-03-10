import items

class Enemy:
	name = "Do not create raw enemies!"
	description = "There is no description here because you should not create raw Enemy objects!"
	attack_description = "There is no attack_description here because you should not create raw Enemy objects!"
	
	hp = 0
	damage = 0
	weakness = 0
	
	loot = []
	
	agro = True	# Used to cause enemies to attack spontaneously.
	
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
		
		if(len(self.loot) > 0):
			for item in loot:
				self.loot.append(item)
		else:
			self.loot = loot

	def __str__(self):
		return self.name
		
	def check_text(self):
		text = ""
		if(self.direction):
			text = "A %s is blocking your progress to the %s." % (self.name, self.direction)
		text += " " + self.description			
		return text

	def take_damage(self, amount):
		if(self.weakness == amount):
			self.hp = 0
			defeat_text = "The %s is defeated." % self.name
			if(len(self.loot) > 0):
				defeat_text += " It dropped the following items: "
				for item in self.loot:
					defeat_text += "* " + str(item)
			return defeat_text
		else:
			return "It didn't have much of an effect."

			
	def is_alive(self):
		return self.hp > 0
		
	def handle_input(self, verb, noun1, noun2, inventory):
		return [False, None, inventory]


class Two(Enemy):
	agro = False
	name = "girl"
	description = "A girl stands here. She seems to not want to kill you."
	hp = 1
	damage = 1
	weakness = 1
	loot = [items.Mirror("A mirror appears to have been on her person")]

class Three(Enemy):
	name = "Blind Bandit"
	description = """Silhouetted against the flame, there is a man. He introduces himself as a superhero, the Blind Bandit, 
			and says that despite being blind, his other senses are quite sensitive.
			He also tells you that he is going to punish you for your evil deeds, despite you having never committed an evil deed,
			or met the man before"""  
	hp = 1
	damage = 1
	weakness = 2

class Four(Enemy):
	name = "Elemental"
	description = "A form wreathed in flames stands before you it. It appears to be a fire elemental."
	hp = 1
	damage = 2
	weakness = 4

class Eight(Enemy):
	name = "contraption"
	description = "A strange contraption flails around wildy shooting energy beams. It doesn't look very safe..."
	hp = 1
	damage = 4
	weakness = 3

class Sorry(Enemy):
	name = "Sorry"
	description = "Something runs out of the darkness and mauls you."
	agro = True
	hp = 1
	damage = 10

