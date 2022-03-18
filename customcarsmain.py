from random import gammavariate
from ursina import *
from customcarsthirdpersoncontroller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
    
app = Ursina()
window.title="game"
window.borderless=False
Entity.default_shader = lit_with_shadows_shader
ground = Entity(model='plane', collider='box', scale=200, color=color.green)
player = FirstPersonController(model="tinker", color=color.orange, origin_y=-0.5,scale=0.01)

# the default camera_pivot is (0,2,0)
player.camera_pivot.z = -7.5  # move the camera behind the player model
player.camera_pivot.y = 20.5  # move the camera a little higher

# setting collider and making it visible for debugging
player.collider = BoxCollider(player, Vec3(0,1,0), Vec3(1,2,1))
player.collider.visible=True

# adding some objects to collide with
for i in range(16):
    a=Entity(model='cube', origin_y=-.5, scale=2, texture='building', texture_scale=(1,2),
        x=random.uniform(-10,10),
        z=random.uniform(-10,10) + 10,
        collider='box',
        scale_y = random.uniform(2,3),
        color=color.hsv(0, 0, random.uniform(.9, 1))
    )

sun = DirectionalLight()
sun.look_at(Vec3(1,-1,-1))
Sky()
def input(key):
    if key == 'q':
        exit()
app.run()
if ss==2:
    app2 = Ursina()
    window.title="player2"
    window.borderless=False
    player2= FirstPersonController(model="spacething/tinker", color=color.orange, origin_y=-0.5,scale=0.01)

    # the default camera_pivot is (0,2,0)
    player2.camera_pivot.z = -7.5  # move the camera behind the player model
    player2.camera_pivot.y = 20.5  # move the camera a little higher

    # setting collider and making it visible for debugging
    player2.collider = BoxCollider(player, Vec3(0,1,0), Vec3(1,2,1))
    player2.collider.visible=True
    def input(key):
        if key == 'q':
            exit()
    app2.run()
