from Event import *
from itertools import cycle

class Sprite(object):
	def __init__(self,listaImagem,position=[255,255]):
		self.default = IdleState(self, listaImagem)
		self.atual = cycle(self.default.listaImagem)
		self.atualState=self.default
		self.position = position
	def getTexture(self):
		try:
			return next(self.atual)
		except StopIteration, e:
			self.setIdle()
		return next(self.atual)
	def setIdle(self):
		self.atual = cycle(self.default.listaImagem)
		self.atualState = self.default

class MovimentEvent(Event):
	def __init__(self,sprite,speed=[1,0]):
		self.sprite = sprite
		assert isinstance(speed, (list,int))
		self.speed = speed
	def action(self):
		if not isinstance(self.sprite.atualState,ActionState):
			self.sprite.position[0]+=self.speed[0]
			self.sprite.position[1]+=self.speed[1]

class State(Event):
	"""docstring for State"""
	def __init__(self,sprite,listaImagem,priority=[]):
		assert isinstance(sprite, Sprite)
		self.sprite = sprite
		self.listaImagem = listaImagem
		self.iter = iter(self.listaImagem)
		self.priority = priority
	def action(self):
		if not isinstance(self,self.sprite.atualState.__class__) and not isinstance(self.sprite.atualState,tuple(self.priority)):
			self.sprite.atual = iter(self.listaImagem)
			self.iter = self.sprite.atual
			self.sprite.atualState = self
		if not isinstance(self.sprite.atualState,tuple(self.priority)) and self.sprite.atualState != self:
			self.sprite.setIdle()

class MovimentState(State):pass
class ActionState(State):pass
class IdleState(State):pass

if __name__ == '__main__':	
	trigger1 = EventTrigger()
	trigger2 = EventTrigger()
	hero = Sprite(trigger1,["atual1","atual2","atual3","atual4"])
	hero.events.append(State(trigger2,hero,["walk1","walk2","walk3","walk4"]))
