from ursina import *
from ursina.shaders import lit_with_shadows_shader
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

Entity(model='plane', texture='white_cube', shader=lit_with_shadows_shader, scale=50, collider='box')

# Simple cube to see red light effect
Entity(model='cube', texture='white_cube', shader=lit_with_shadows_shader,
       position=(0,1,0), scale=2)

print(f"Fog density: {scene.fog_density}, Fog color: {scene.fog_color}")




player = FirstPersonController()
player.gravity = 0.5
player.camera_pivot.y = 2

# Light setup
dlight = DirectionalLight()
dlight.look_at(Vec3(1, -1, -1))
dlight.color = color.rgba(80, 0, 0, 255)
dlight.parent = scene

alight = AmbientLight()
alight.color = color.rgba(10, 10, 10, 255)
alight.parent = scene

# Fog
def set_fog():
    scene.fog_density = 0.03
    scene.fog_color = color.rgba(20, 0, 0, 255)
    print(f"Fog density: {scene.fog_density}, Fog color: {scene.fog_color}")

invoke(set_fog, delay=0.1)

app.run()
