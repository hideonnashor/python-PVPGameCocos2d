import cocos
from cocos.actions import *
import pyglet
#label/sprite->layer->scene->director
#layer class includes a label
class HelloWorld(cocos.layer.ColorLayer):
	def __init__(self):
		super(HelloWorld,self).__init__(64,164,224,100)

		#label
		self.label = cocos.text.Label(
			'アメリカ人',
			font_name = 'Microsoft YaHei',
			font_size = 32,
			anchor_x = 'center',anchor_y = 'center'
			)
		self.label.position = 320,240
		#sprite
		sprite = cocos.sprite.Sprite('img.png')
		sprite.scale = 1
		sprite.position = 320,240
		#action
		action_scale = ScaleBy(2,duration = 2)

		# set the label in the center of the screen
		self.add(self.label)
		# set the sprite
		self.add(sprite,z=-1)

		#set the action of the sprite
		sprite.do(Repeat(Reverse(action_scale)+action_scale))
class KeyDisplay(cocos.layer.Layer):
 	# If you want that your layer receives director.window events
    # you must set this variable to 'True'
	is_event_handler = True

	def __init__(self):
		super(KeyDisplay, self).__init__()
		self.text = cocos.text.Label("",x = 100,y = 280)

		#To keep track of which keys are pressed
		self.keys_pressed = set()
		self.key_names = []
		self.update_text()

		self.add(self.text)

	def update_text(self):
		for k in self.keys_pressed:
			self.key_names = [pyglet.window.key.symbol_string(k) ]
		text = 'Keys:'+','.join(self.key_names)
			#update self.text
		self.text.element.text = text

	def on_key_press (self, key, modifiers):
		self.keys_pressed.add(key)
		self.update_text()

	def on_key_release (self, key, modifiers):
		self.keys_pressed.remove(key)
		self.update_text()
		

# director
cocos.director.director.init(resizable = True)
# scene includes the layer
hello_layer = HelloWorld()
key_display = KeyDisplay()#create layers instance
main_scene = cocos.scene.Scene(hello_layer,key_display)#add the layer to the scene
# run the scene included in the director
cocos.director.director.run(main_scene)