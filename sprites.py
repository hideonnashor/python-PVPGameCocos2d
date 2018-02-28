import cocos

class Panda(object):
	"""docstring for Panda"""
	def __init__(self):
		super(Panda, self).__init__()
	def getSprite(self,spriteImgPath):
		self.sprite = cocos.sprite.Sprite(spriteImgPath)
		return self.sprite

# class Coin(object):
# 	"""docstring for Coin"""
# 	def __init__(self):
# 		super(Coin, self).__init__()
# 	def getCoin(self):
# 		self.sprite = cocos.sprite.Sprite("img/coin_common.png")
# 		return self.sprite
