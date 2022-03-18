from ursina import *
import customcarsmain
import time
i=0
x=29
y=1
health=100
ss=0
bullet = Entity(model='sphere', scale=2, color=color.red,x=10,y=1)
def hitcheck():
    global health,x,y
    if x==30:
      x=0
      y=0
    if y==1:
      x=x+1
    print(str(health)+'-'+str(x))
    if distance(customcarsmain.player, bullet) < bullet.scale_x / 1.5:
         y=1
         
         if x==30:
             health= health -10
        
         #collideSH.animate_scale(0, duration=.1)
        
         if health==0:
            customcarsmain.player.position=(0,10,0)
            health=100
            if x==30:
              x=0
              y=0
            if y==1:
              x=x+1
         #destroy(collideSH, delay=.1)
carspeed=0
car_reverse=0

a=Audio('engine', pitch=1, loop=False, autoplay=False)
class FirstPersonController(Entity):
    def __init__(self, **kwargs):
        self.cursor = Entity(parent=camera.ui)
        super().__init__()
        self.speed = 5
        self.height = 2
        self.camera_pivot = Entity(parent=self, y=self.height)

        camera.parent = self.camera_pivot
        camera.position = (0,0,0)
        camera.rotation = (0,0,0)
        camera.fov = 100
        mouse.locked = True
        self.mouse_sensitivity = Vec2(40, 40)

        self.gravity = 1
        self.grounded = False
        self.jump_height = 2
        self.jump_up_duration = .5
        self.fall_after = .35 # will interrupt jump up
        self.jumping = False
        self.air_time = 0

        for key, value in kwargs.items():
            setattr(self, key ,value)

        # make sure we don't fall through the ground if we start inside it
        if self.gravity:
            ray = raycast(self.world_position+(0,self.height,0), self.down, ignore=(self,))
            if ray.hit:
                self.y = ray.world_point.y


    def update(self):
        hitcheck()
        global carspeed,car_reverse,a,i
        self.rotation_y += (held_keys['d'] - held_keys['a'])

        self.camera_pivot.rotation_x -= mouse.velocity[1] * self.mouse_sensitivity[0]
        self.camera_pivot.rotation_x= clamp(self.camera_pivot.rotation_x, -90, 90)
        
        print('carspeed:'+str(round(carspeed))+' speed:'+str(round(self.speed)))
        if carspeed<20:
            carspeed= carspeed +(0.1*(held_keys['w']-held_keys['s']))
        if held_keys['w'] + held_keys['s']>0:
            # a.volume = round(carspeed)*0.4 
            # a = Audio('engine', pitch=round(carspeed)*0.05, loop=False, autoplay=True)
            i=i
        if held_keys['w']-held_keys['s']==0:
            if carspeed<0:
                carspeed=carspeed+0.05
            else:
                carspeed=carspeed-0.05
        if carspeed<0:
            self.speed=-1*carspeed
            car_reverse=-1

        else:
            self.speed=carspeed
            car_reverse=1
        self.direction = Vec3(
            self.forward * car_reverse).normalized()
        
        if customcarsmain.player.intersects(bullet).hit:
           bullet.color = color.lime
           print('player is inside trigger box')
        else:
           bullet.color = color.gray



        feet_ray = raycast(self.position+Vec3(0,0.5,0), self.direction, ignore=(self,), distance=.5, debug=False)
        head_ray = raycast(self.position+Vec3(0,self.height-.1,0), self.direction, ignore=(self,), distance=.5, debug=False)
        if not feet_ray.hit and not head_ray.hit:
            self.position += self.direction * self.speed * time.dt


        if self.gravity:
            # gravity
            ray = raycast(self.world_position+(0,self.height,0), self.down, ignore=(self,))
            # ray = boxcast(self.world_position+(0,2,0), self.down, ignore=(self,))

            if ray.distance <= self.height+.1:
                if not self.grounded:
                    self.land()
                self.grounded = True
                # make sure it's not a wall and that the point is not too far up
                if ray.world_normal.y > .7 and ray.world_point.y - self.world_y < .5: # walk up slope
                    self.y = ray.world_point[1]
                return
            else:
                self.grounded = False

            # if not on ground and not on way up in jump, fall
            self.y -= min(self.air_time, ray.distance-.05) * time.dt * 100
            self.air_time += time.dt * .25 * self.gravity


    def input(self, key):
        if key == 'space':
            self.jump()


    def jump(self):
        if not self.grounded:
            return

        self.grounded = False
        self.animate_y(self.y+self.jump_height, self.jump_up_duration, resolution=int(1//time.dt), curve=curve.out_expo)
        invoke(self.start_fall, delay=self.fall_after)


    def start_fall(self):
        self.y_animator.pause()
        self.jumping = False

    def land(self):
        # print('land')
        self.air_time = 0
        self.grounded = True


    def on_enable(self):
        mouse.locked = True
        self.cursor.enabled = True


    def on_disable(self):
        mouse.locked = False
        self.cursor.enabled = False









