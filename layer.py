import cocos
from cocos.actions import *
import random
import threading

import sprites

class BG(cocos.layer.ColorLayer):
	"""docstring for BG"""
	def __init__(self):
		super(BG, self).__init__(255,255,255,255)

class SpritesLayer01(cocos.layer.Layer):
	"""docstring for SpritesLayer"""
	is_event_handler = True

	def __init__(self):
		super(SpritesLayer01, self).__init__()

		self.horizontalV = 0
		self.verticalV = 0
	def addSprites(self,spriteImgPath,size,Xpos,Ypos):
		self.spriteToAdd = None
		self.spriteToAdd = sprites.Panda().getSprite(spriteImgPath)
		self.spriteToAdd.scale = size
		self.spriteToAdd.position = Xpos,Ypos
		self.add(self.spriteToAdd,z = 1)
		
		return self
	def on_key_press(self,key,modifiers):
		if key == 65361:#left
			self.horizontalV -= 10
		elif key == 65363:#right
			self.horizontalV += 10
		elif key == 65362:#up
			self.verticalV += 10
		elif key == 65364:#down
			self.verticalV -= 10
		self.spriteToAdd.do(Repeat(MoveBy((self.horizontalV,self.verticalV),0.05)))
	def on_key_release(self,key,modifiers):
		if key == 65361:
			self.horizontalV += 10
		elif key == 65363:
			self.horizontalV -= 10
		elif key == 65362:
			self.verticalV -= 10
		elif key == 65364:
			self.verticalV += 10
		self.spriteToAdd.do(Repeat(MoveBy((self.horizontalV,self.verticalV),0.05)))

class SpritesLayer02(cocos.layer.Layer):
	"""docstring for SpritesLayer"""
	is_event_handler = True

	def __init__(self):
		super(SpritesLayer02, self).__init__()

		self.horizontalV = 0
		self.verticalV = 0
	def addSprites(self,spriteImgPath,size,Xpos,Ypos):
		self.spriteToAdd = None
		self.spriteToAdd = sprites.Panda().getSprite(spriteImgPath)
		self.spriteToAdd.scale = size
		self.spriteToAdd.position = Xpos,Ypos
		self.add(self.spriteToAdd,z = 1)
		
		return self
	def on_key_press(self,key,modifiers):
		if key == 97:#left
			self.horizontalV -= 10
		elif key == 100:#right
			self.horizontalV += 10
		elif key == 119:#up
			self.verticalV += 10
		elif key == 115:#down
			self.verticalV -= 10
		self.spriteToAdd.do(Repeat(MoveBy((self.horizontalV,self.verticalV),0.05)))
	def on_key_release(self,key,modifiers):
		if key == 97:
			self.horizontalV += 10
		elif key == 100:
			self.horizontalV -= 10
		elif key == 119:
			self.verticalV -= 10
		elif key == 115:
			self.verticalV += 10
		self.spriteToAdd.do(Repeat(MoveBy((self.horizontalV,self.verticalV),0.05)))


	
