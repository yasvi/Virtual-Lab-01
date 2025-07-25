from ursina import *
app=Ursina()
Entity(model='assets/bunsen_burner.glb',scale=6,position=(0,0,0))
EditorCamera()
app.run()
# #add countertops
# Entity(model='cube',scale=(7,0.25,11),position=(-16,1.6,12),
#        color=color.white,texture_scale=(10,10),collider='box')

# Entity(model='cube',scale=(7,0.25,11),position=(16,1.6,-12),
#        color=color.white,texture_scale=(10,10),collider='box')

# Entity(model='cube',scale=(7,0.25,11),position=(0,1.6,12),
#        color=color.white,texture_scale=(10,10),collider='box')

# Entity(model='cube',scale=(7,0.25,11),position=(-16,1.6,-12),
#        color=color.white,texture_scale=(10,10),collider='box')

# Entity(model='cube',scale=(7,0.25,11),position=(0,1.6,-12),
#        color=color.white,texture_scale=(10,10),collider='box')

# Entity(model='cube',scale=(7,0.25,11),position=(16,1.6,12),
#        color=color.white,texture_scale=(10,10),collider='box')

# flame_light = PointLight(parent=scene, position=(16, 5, 12), color=color.orange,shadow=True)
# flame_light.shadow_strength = 0.3