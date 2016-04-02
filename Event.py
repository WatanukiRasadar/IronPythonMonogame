from abc import abstractmethod,ABCMeta

class EventTrigger(object):
	def __init__(self):
		self.events = []
	def addEvent(self,event):
		assert isinstance(event, Event)
		self.events.append(event)
	def action(self):
		for event in self.events:
			event.action()

class Event(object):
	__metaclass__=ABCMeta
	def __init__(self,trigger):
		assert isinstance(trigger, EventTrigger)
		self.trigger = trigger
		self.trigger.addEvent(self)
	@abstractmethod
	def action(self):
		return NotImplemented