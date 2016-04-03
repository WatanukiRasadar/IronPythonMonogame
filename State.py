from Event import *
from itertools import cycle

class Sprite(object):
	def __init__(self,listaImagem,position=[255,255]):
		self.default = State(self, listaImagem)
		self.atual = cycle(self.default.listaImagem)
		self.priority = 10
		self.position = position
	def getTexture(self):
		try:
			return next(self.atual)
		except StopIteration, e:
			self.atual = cycle(self.default.listaImagem)
			self.priority = 10
		return next(self.atual)

class MovimentEvent(Event):
	def __init__(self,sprite,speed=[1,0]):
		self.sprite = sprite
		assert isinstance(speed, (list,int))
		self.speed = speed
	def action(self):
		self.sprite.position[0]+=self.speed[0]
		self.sprite.position[1]+=self.speed[1]



class State(Event):
	"""docstring for State"""
	def __init__(self,sprite,listaImagem,priority=10):
		assert isinstance(sprite, Sprite)
		self.sprite = sprite
		self.listaImagem = listaImagem
		self.iter = iter(self.listaImagem)
		self.priority = priority
	def action(self):
		if (not self.sprite.atual == self.iter) and self.priority < self.sprite.priority:
			self.sprite.atual = iter(self.listaImagem)
			self.iter = self.sprite.atual
			self.sprite.priority = self.priority
		if self.priority == self.sprite.priority and (not self.sprite.atual == self.iter):
			self.sprite.atual = cycle(self.sprite.default.listaImagem)
			self.sprite.priority = 10

if __name__ == '__main__':	
	trigger1 = EventTrigger()
	trigger2 = EventTrigger()
	hero = Sprite(trigger1,["atual1","atual2","atual3","atual4"])
	hero.events.append(State(trigger2,hero,["walk1","walk2","walk3","walk4"]))
