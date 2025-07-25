from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
from random import randint

app = Ursina()

#lighting
Dlight=DirectionalLight()
Dlight.look_at(Vec3(1,-1,-1))
Dlight.color=color.rgba(0.3,0,0,80)
Dlight.parent=scene

Alight=AmbientLight()
Alight.color=color.rgba(10,10,10,255)
Alight.parent=scene

flicker_light = PointLight()
flicker_light.color = color.rgba(255, 50, 0, 200)  
flicker_light.position = Vec3(20, 5, 20)  
flicker_light.parent = scene

def flicker_task():
    flicker_intensity = randint(50, 200)
    flicker_light.color = color.rgba(255, 50, 0, flicker_intensity)
    flicker_cube.color = color.rgba(255, 255, 0, flicker_intensity)
    invoke(flicker_task, delay=0.1 + randint(0, 100)/1000)

flicker_cube=Entity(model='cube', color=color.yellow, scale=(0.2,0.2,0.2), position=flicker_light.position)
flicker_task()

#game mechanics
def update():
    if held_keys['b']:
        Dlight.color=color.rgba(0.9,0,0,80)
       
    if held_keys['escape']:
        application.quit()

#add floor
Entity(model='plane',
       scale=50,
       collider='box',
       texture='floor.jpg',
       texture_scale=(10,10),
       color=color.white,
       shader=lit_with_shadows_shader
)


#add ceiling
Entity(model='cube',
       color=color.white,
       scale=(1,50,50),
       collider='box',
       position=(0,12,0),
       texture='assets/wall.jpeg' ,
       rotation_z=90,
       texture_scale=(1,1),
       shader=lit_with_shadows_shader
)

#add walls
Entity(model='cube',
       scale=(1,20,50),
       position=(-25,2.5,0),
       texture='assets/wall.jpeg',
       texture_scale=(1,1),
       collider='box',
       color=color.white,
       shader=lit_with_shadows_shader)

Entity(model='cube',
       scale=(1,20,50),
       position=(25,2.5,0),
       texture='assets/wall.jpeg',
       rotation_y=180,
       texture_scale=(1,1),
       collider='box',
       color=color.white,
       shader=lit_with_shadows_shader)

Entity(model='cube',
       scale=(50,20,1),
       position=(0,2.5,-25),
       texture='assets/wall.jpeg',
       texture_scale=(1,1),
       collider='box',
       color=color.white,
       shader=lit_with_shadows_shader)

Entity(model='cube',
       scale=(50,20,1),
       position=(0,2.5,25),
       texture='assets/wall.jpeg',
       texture_scale=(1,1),
       collider='box',
       color=color.white,
       shader=lit_with_shadows_shader)

#add tables
Entity(model='assets/table.glb',
       scale=5,
       position=(-16,1.8,-12),
       collider='box',
       color=color.white,
       shader=lit_with_shadows_shader)

Entity(model='assets/table.glb',
       scale=5,position=(0,1.8,-12),
       collider='box',
       color=color.white,
       shader=lit_with_shadows_shader)

Entity(model='assets/table.glb',
       scale=5,
       position=(16,1.8,-12),
       collider='box',
       color=color.white,
       shader=lit_with_shadows_shader)

Entity(model='assets/table.glb',
       scale=5,
       position=(16,1.8,12),
       collider='box',
       color=color.white,
       shader=lit_with_shadows_shader)

Entity(model='assets/table.glb',
       scale=5,
       position=(0,1.8,12),
       collider='box',
       color=color.white,
       shader=lit_with_shadows_shader)

Entity(model='assets/table.glb',
       scale=5,
       position=(-16,1.8,12),
       collider='box',
       color=color.white,
       shader=lit_with_shadows_shader)

#add Bunsen burner
Entity(model='assets/bunsen_burner.glb',
       scale=7.5,
       position=(16,3.8,12),
       collider='mesh',
       color=color.white,
       shader=lit_with_shadows_shader)

Entity(model='assets/bunsen_burner.glb',
       scale=7.5,
       position=(-16,3.8,-12),
       collider='mesh',
       color=color.white,
       shader=lit_with_shadows_shader)

Entity(model='assets/bunsen_burner.glb',
       scale=7.5,
       position=(-16,3.8,12),
       collider='mesh',
       color=color.white,
       shader=lit_with_shadows_shader)

Entity(model='assets/bunsen_burner.glb',
       scale=7.5,
       position=(16,3.8,-12),
       collider='mesh',
       color=color.white,
       shader=lit_with_shadows_shader)

Entity(model='assets/bunsen_burner.glb',
       scale=7.5,
       position=(0,3.8,12),
       collider='mesh',
       color=color.white,
       shader=lit_with_shadows_shader)

Entity(model='assets/bunsen_burner.glb',
       scale=7.5,
       position=(0,3.8,-12),
       collider='mesh',
       color=color.white,
       shader=lit_with_shadows_shader)

#Add testube stand
Entity(model='assets/testubes.glb',
       scale=1.3,
       position=(16,3.8,15),
       collider='mesh',
       color=color.white,
       shader=lit_with_shadows_shader,
       rotation_y=270)

Entity(model='assets/testubes.glb',
       scale=1.3,
       position=(-16,3.8,-9),
       collider='mesh',
       color=color.white,
       shader=lit_with_shadows_shader,
       rotation_y=270)

Entity(model='assets/testubes.glb',
       scale=1.3,
       position=(-16,3.8,15),
       collider='mesh',
       color=color.white,
       shader=lit_with_shadows_shader,
       rotation_y=270)

Entity(model='assets/testubes.glb',
       scale=1.3,
       position=(16,3.8,-9),
       collider='mesh',
       color=color.white,
       shader=lit_with_shadows_shader,
       rotation_y=270)

Entity(model='assets/testubes.glb',
       scale=1.3,
       position=(0,3.8,15),
       collider='mesh',
       color=color.white,
       shader=lit_with_shadows_shader,
       rotation_y=270)

Entity(model='assets/testubes.glb',
       scale=1.3,
       position=(0,3.8,-9),
       collider='mesh',
       color=color.white,
       shader=lit_with_shadows_shader,
       rotation_y=270)
    
#EditorCamera()

# Add hologram
Entity(model= 'assets/hologram.glb',
       position=(0,4,0),
       scale=2.5,
       color=color.rgb(255,255,255),
       collider='sphere',
       shader=lit_with_shadows_shader)


#Add shelf
Entity(model='book_shelf.glb',
       scale =0.04,
       position=(-24,0,0),
       collider='box',
       color=color.white,
       shader=lit_with_shadows_shader,
       rotation_y=270)

#add flame
Entity(model='cube',
       scale=(0.05,0.05),
       collider='box',
       color=color.blue,
       position=(0,5,12),
       rotation_x=90)

Entity(model='cube',
       scale=(0.05,0.05),
       collider='box',
       color=color.blue,
       position=(0,5,-12),
       rotation_x=90)

Entity(model='cube',
       scale=(0.05,0.05),
       collider='box',
       color=color.blue,
       position=(16,5,12),
       rotation_x=90)

Entity(model='cube',
       scale=(0.05,0.05),
       collider='box',
       color=color.blue,
       position=(-16,5,12),
       rotation_x=90)

Entity(model='cube',
       scale=(0.05,0.05),
       collider='box',
       color=color.blue,
       position=(16,5,-12),
       rotation_x=90)

Entity(model='cube',
       scale=(0.05,0.05),
       collider='box',
       color=color.blue,
       position=(-16,5,-12),
       rotation_x=90)

# Add chemicals
Mg=Entity(model='cube',
       scale=0.5,
       collider='box',
       color=color.white,
       position=(-23,4.3,0)
       )


#player settings
player =FirstPersonController()
player.position = (0,6,0)

player.gravity=0.5
player.camera_pivot.y=5


update()


app.run()






























































