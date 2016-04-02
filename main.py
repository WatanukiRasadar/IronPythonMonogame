__watanuki__="Elielton_Kremer"
import clr,sys,os
from State import *
isWindows = sys.platform == 'win32'
if isWindows:
	print 'windows'
else:
	dllpath = "./dll/unix" 
	for dll in os.listdir(dllpath):
		clr.AddReferenceToFileAndPath(dllpath + "/" + dll)
from Microsoft.Xna.Framework import *
from Microsoft.Xna.Framework.Graphics import *
from Microsoft.Xna.Framework.Input import *

class App(Game):
    def __init__(self):
        self.graphics = GraphicsDeviceManager(self)
        self.Content.RootDirectory = os.getcwd() + "/Content"
        self.keyboardListener = KeyBoardListener(Keyboard)
        self.spriteBatch = None
        self.currentStage = Stage(self)
    def LoadContent(self):
    	self.currentStage.Load()
    	self.spriteBatch = SpriteBatch(self.graphics.GraphicsDevice)
    def Update(self,gameTime):
    	self.keyboardListener.action()
    def Draw(self, gameTime):
        self.graphics.GraphicsDevice.Clear(Color.Black)
        self.spriteBatch.Begin()
        for texture in self.currentStage.textures:
        	self.spriteBatch.Draw(texture.getTexture(),Vector2(100,100),Color.White)
        self.spriteBatch.End()
        Game.Draw(self, gameTime)


class Stage(object):
	"""docstring for Stage"""
	def __init__(self,game):
		self.__next__= None
		assert isinstance(game, App)
		self.game = game
		self.textures = []
	def Load(self):
		walkTrigger = EventTrigger()
		actionTrigger = EventTrigger()
		self.game.keyboardListener.addTrigger("Right", walkTrigger)
		self.game.keyboardListener.addTrigger("X", actionTrigger)
		stopedTrigger = EventTrigger()
		sprite = Sprite(stopedTrigger, self.LoadHeroState("hero/stop"))
		sprite.events.append(State(walkTrigger,sprite,self.LoadHeroState("hero/walk")))
		sprite.events.append(State(actionTrigger,sprite,self.LoadHeroState("hero/action")))
		self.textures.append(sprite)

	def LoadHeroState(self,path):
		listSprites = []
		for img in os.listdir("./Content/"+path):
			listSprites.append(self.game.Content.Load[Texture2D](path + "/" + img.replace(".png","")))
		return listSprites



class KeyBoardListener(object):
	def __init__(self,keyboard,keysTriggers={}):
		self.keyboard=keyboard
		self.keysTriggers = keysTriggers
	def addTrigger(self,key,trigger):
		if not self.keysTriggers.has_key(key):
			self.keysTriggers[key] = []
		self.keysTriggers[key].append(trigger)
	def action(self):
		presseds = self.keyboard.GetState().GetPressedKeys()
		for key in presseds:
			if self.keysTriggers.has_key(str(key)):
				for trigger in self.keysTriggers[str(key)]:
					trigger.action()

if __name__ == "__main__":
	app = App()
	app.Run()