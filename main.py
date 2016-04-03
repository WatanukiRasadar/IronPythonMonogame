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

def getKeyboardStatus():
	return Keyboard.GetState().GetPressedKeys()
def getMouseStatus():
	state =  Mouse.GetState()
	return [str((str(state.LeftButton),state.ScrollWheelValue,str(state.RightButton))),]
class App(Game):
    def __init__(self):
        self.graphics = GraphicsDeviceManager(self)
        self.Content.RootDirectory = os.getcwd() + "/Content"
        self.eventHandler = EventHandler()
        self.eventHandler.addListener("keyboard", getKeyboardStatus)
        self.eventHandler.addListener("Mouse", getMouseStatus)
        self.spriteBatch = None
        self.currentStage = Stage(self)
    def LoadContent(self):
    	self.currentStage.Load()
    	self.spriteBatch = SpriteBatch(self.graphics.GraphicsDevice)
    def Update(self,gameTime):
    	self.eventHandler.action()
    def Draw(self, gameTime):
        self.graphics.GraphicsDevice.Clear(Color.Black)
        self.spriteBatch.Begin()
        for texture in self.currentStage.textures:
        	self.spriteBatch.Draw(texture.getTexture(),Vector2(texture.position[0],texture.position[1]),Color.White)
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
		sprite = Sprite(self.LoadHeroState("hero/stop"))
		walking = State(sprite,self.LoadHeroState("hero/walk"),priority=7)
		action = State(sprite,self.LoadHeroState("hero/action"),priority=5)
		self.game.eventHandler.addEventToListener("keyboard","X",action)
		self.game.eventHandler.addEventToListener("Mouse",('Pressed',0,'Released'),action)
		self.game.eventHandler.addEventToListener("keyboard","Right",walking)
		self.game.eventHandler.addEventToListener("keyboard","Left",walking)
		self.game.eventHandler.addEventToListener("keyboard","Right",MovimentEvent(sprite))
		self.game.eventHandler.addEventToListener("keyboard","Left",MovimentEvent(sprite,speed=[-1,0]))
		self.textures.append(sprite)

	def LoadHeroState(self,path):
		listSprites = []
		for img in os.listdir("./Content/"+path):
			listSprites.append(self.game.Content.Load[Texture2D](path + "/" + img.replace(".png","")))
		return listSprites

if __name__ == "__main__":
	
	app = App()
	app.Run()