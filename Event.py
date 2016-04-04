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
	@abstractmethod
	def action(self):
		return NotImplemented

class EventHandler(object):
	def __init__(self):
		self._listeners={}
		self._triggers={}

	def addListener(self,key,listener):
		self._listeners[id(key)]=listener
		self._triggers[id(key)] = {}

	def addEventToListener(self,listenerKey,listenerStatus,event):
		assert isinstance(event, Event)
		triggersListerner = self._triggers[id(listenerKey)]
		if not str(listenerStatus) in triggersListerner:
			triggersListerner[str(listenerStatus)] = EventTrigger()
		triggersListerner[str(listenerStatus)].addEvent(event)
		print self._triggers

	def action(self):
		for listenerKey,listener in self._listeners.items():
			status = listener()
			for state in status:
				if str(state) in self._triggers[listenerKey].keys():
					self._triggers[listenerKey][str(state)].action()


