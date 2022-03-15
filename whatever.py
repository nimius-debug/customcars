from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
ground=Entity(shape="plane",texture="white_cube",scale=40,x=0,y=0,Collider="box")
player=FirstPersonController(x=0,y=30,collider='box',model='cube')
app.run()
