from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
import mysql.connector as cc
from mysql.connector import IntegrityError
from random import randint

app = Ursina()

db={
    'host':'localhost',
    'user':'root',
    'password':'sql'
}

conn= cc.connect(**db)
cursor=conn.cursor()

cursor.execute('create database if not exists ursina')
cursor.execute('use ursina'
               )
cursor.execute('''create table if not exists auth(
               username varchar(60) primary key,
               password varchar(50))''')
conn.commit()



# player settings
player =FirstPersonController()
player.position = (0,-26,-10)

player.gravity=0.5
player.camera_pivot.y=5

# EditorCamera()

def cred_room():
    
    global cred_entities
    cred_entities=[]

    floor=Entity(model='plane',
                 color=color.black  ,
                 scale=50,
                 collider='box',
                 y=-30)

    ceiling=Entity(model='cube',
       color=color.black,
       scale=(1,50,50),
       collider='box',
       position=(0,-18,0),
       rotation_z=90,)
                     
    
    wall1= Entity(model='cube',
       scale=(1,20,50),
       position=(-25,-27.5,0),
       collider='box',
       color=color.black,
       shader=lit_with_shadows_shader)

    wall2=Entity(model='cube',
       scale=(1,20,50),
       position=(25,-27.5,0),
       rotation_y=180,
       collider='box',
       color=color.black,
       shader=lit_with_shadows_shader)

    wall3=Entity(model='cube',
       scale=(50,20,1),
       position=(0,-27.5,-25),
       collider='box',
       color=color.black,
       shader=lit_with_shadows_shader)

    wall4=Entity(model='cube',
       scale=(50,20,1),
       position=(0,-27.5,25),
       collider='box',
       color=color.black,
       shader=lit_with_shadows_shader)
        

    cred_entities.extend([floor,ceiling,wall1,wall2,wall3,wall4])

    global login_door, signup_door,\
    signin ,login ,signup_panel,\
    login_panel,user_s,passwords_s,\
    msg_s,user_l,passwords_l,continue_s\
    ,continue_l,msg_l

    login_door=Entity(model='cube',
                      scale=7,
                      position=(-16,-26,-12),
                      color=color.red,
                      collider='box')
    
    signup_door=Entity(model='cube',
                       scale=7,
                       position=(16,-26,-12),
                       collider='box',
                       color=color.blue)

    light=PointLight(position=Vec3(20,-25,20),
                     color=color.white)

    signin=Text('Sign in',
                scale=10,
                origin=(0,0),
                enabled =False,
                color=color.white,
                parent=signup_door,
                billboard=True,
                z=-0.1,
                )
    
    login=Text('Login',
                scale=10,
                origin=(0,0),
                enabled =False,
                color=color.white,
                parent=login_door,
                billboard=True,
                z=-0.1,
                )
    

    signup_panel=Entity(enabled=False,parent=camera.ui)
    login_panel=Entity(enabled=False,parent=camera.ui)
    user_l = InputField(y=0,parent=login_panel)
    passwords_l = InputField(y=-0.2,parent=login_panel,password=True)
    
    user_s = InputField(y=0,parent=signup_panel)
    passwords_s = InputField(y=-0.2,parent=signup_panel,password=True)
    msg_s = Text("", parent=signup_panel, y=0.3, color=color.black)
    msg_l = Text("", parent=login_panel, y=0.3, color=color.black)
    continue_s=Button('continue',parent=signup_panel,y=-0.3)
    continue_l=Button('continue',parent=login_panel,y=-0.3)

    cred_entities.extend([login_door,signup_door,light,signin,login])
    
    

cred_room()

def show_sign_panel():
    player.enabled=False
    mouse.locked=False
    signup_panel.enabled=True

def hide_sign_panel():
    player.enabled=True
    mouse.locked=True
    signup_panel.enabled=False

def show_login_panel():
    player.enabled=False
    mouse.locked=False
    login_panel.enabled=True

def hide_login_panel():
    player.enabled=True
    mouse.locked=True
    login_panel.enabled=False

def continue_login():
    if user_l.text and passwords_l.text:
        username = user_l.text.strip()
        password = passwords_l.text.strip()
        cursor=conn.cursor()
        cursor.execute('use ursina')
        try:
              cursor.execute('select * from auth where username=%s and password=%s',(username,password))
              result=cursor.fetchone()
              cursor.close()



        except cc.Error as err:
            return
        
        if result:
                  hide_login_panel()
                  player.position=Vec3(0,0,16) 
        else:
             msg_l.text="login error"
             msg_l.color=color.white                  
            

    else:
        msg_l.text='please enter values for both fields'
  

def continue_sign():
    if user_s.text and passwords_s.text:
        username = user_s.text.strip()
        password = passwords_s.text.strip()
        cursor=conn.cursor()
        cursor.execute('use ursina')
        try:
              cursor.execute('insert into auth values(%s,%s) ',(username,password))

        except IntegrityError:
            msg_s.text=" Username already exists! Please choose another."
            msg_s.color=color.white
            return
            
        conn.commit()
        hide_sign_panel()
        player.position=Vec3(0,0,16)
    
    else:
        msg_s.text='please enter values for both fields'
        
        
continue_s.on_click=continue_sign
continue_l.on_click=continue_login 



#game mechanics
def update():
    if held_keys['b']:
        Dlight.color=color.rgba(0.9,0,0,80)
       
    if held_keys['escape']:
        application.quit()

    if distance(player.position,signup_door.position)<15 and held_keys['e']:
        show_sign_panel()

    else:
        signin.enabled=False

    if distance(player.position,login_door.position)<15 and held_keys['e']:
        show_login_panel()

    else:
        login.enabled=False


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

app.run()





























































