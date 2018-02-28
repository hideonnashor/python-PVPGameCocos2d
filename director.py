import cocos

import layer
import sprites

cocos.director.director.init(resizable = True)

#layer
backgroundLayer = layer.BG()
spritesLayer01 = layer.SpritesLayer01().addSprites("img/panda_sit.png",0.2,310,90)
spritesLayer02 = layer.SpritesLayer02().addSprites("img/coin_common.png",0.2,310,90)
# coninsLayer01 = layer.CoinLayer()
#
mainScene = cocos.scene.Scene(backgroundLayer,spritesLayer01,spritesLayer02)
#
cocos.director.director.run(mainScene)
