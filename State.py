from Event import *
from itertools import cycle

class Sprite(object):
	def __init__(self,trigger,listaImagem):
		self.events = []
		self.default = State(trigger,self, listaImagem)
		self.atual = cycle(self.default.listaImagem)
	def getTexture(self):
		try:
			return next(self.atual)
		except StopIteration, e:
			self.atual = cycle(self.default.listaImagem)
		return next(self.atual)

		

class State(Event):
	"""docstring for State"""
	def __init__(self,trigger,sprite,listaImagem):
		super(State, self).__init__(trigger)
		assert isinstance(sprite, Sprite)
		self.sprite = sprite
		self.listaImagem = listaImagem
		self.iter = iter(self.listaImagem)
	def action(self):
		if not self.sprite.atual == self.iter:
			self.sprite.atual = iter(self.listaImagem)
			self.iter = self.sprite.atual

if __name__ == '__main__':	
	trigger1 = EventTrigger()
	trigger2 = EventTrigger()
	hero = Sprite(trigger1,["atual1","atual2","atual3","atual4"])
	hero.events.append(State(trigger2,hero,["walk1","walk2","walk3","walk4"]))
