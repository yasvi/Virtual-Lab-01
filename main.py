#=====================
# IMPORT STATEMENTS
#=====================
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
import mysql.connector as cc
from mysql.connector import IntegrityError
from random import randint

#==========================================

#   BEFORE RUNNING READ THE README FILE

#==========================================

app = Ursina()

#==============================
# SQL DATABASE CONNECTION
#==============================

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



# PLAYER SETTINGS
player =FirstPersonController()
player.position = (0,-23,21.5)
player.gravity=0.5
player.camera_pivot.y=5

# EditorCamera()

#===================
# CREDENTIAL ROOM
#===================

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
    ,continue_l,msg_l,cancel_s,cancel_l\
    ,bg,text_l,text_s,click,cred_bg

    login_door=Entity(model='assets/rift.glb',
                      scale=4,
                      position=(-16,-24,-12),
                      color=color.rgb(255,0,0),
                      rotation_z=180,
                      collider='box')
    
    signup_door=Entity(model='assets/rift.glb',
                       scale=4,
                       position=(16,-24,-12),
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
    
    # SOUNDS
    click= Audio('assets/click.wav',autoplay=False)
    cred_bg=Audio('assets/abg.mp3',autoplay=False,loop=True)
    cred_bg.volume=5
    cred_bg.play()

    # LOGIN ENTITY
    login_panel=Entity(enabled=False,parent=camera.ui)

    user_l = InputField('Username',y=0,parent=login_panel,
                        color=color.rgba(0.5,0.5,0.5,0.6),z=-1)
    user_l.highlight_color=color.rgba(0.5,0.5,0.5,0.6)

    passwords_l = InputField('Password',y=-0.2,parent=login_panel,password=True,
                             color=color.rgba(0.5,0.5,0.5,0.6),z=-1)
    passwords_l.highlight_color=color.rgba(0.5,0.5,0.5,0.6)
    passwords_l.hide_content=True
   
    msg_l = Text("", parent=login_panel, y=-0.1,x=-0.08, color=color.black)

    continue_l=Button('Continue',parent=login_panel,y=-0.3,x=-0.1,scale=(0.15,0.1),
                      color=color.rgba(0.5,0.5,0.5,0.6))
    continue_l.text_entity.scale=8

    cancel_l=Button('Cancel',parent=login_panel,y=-0.3,x=0.1,scale=0.1,
                    color=color.rgba(0.5,0.5,0.5,0.6))

    text_l=Text('Login',parent=login_panel,y=0.3,x=-0.16,scale=5,color=color.white,z=-1)


    #SIGNUP ENTITY
    signup_panel=Entity(enabled=False,parent=camera.ui) 

    user_s = InputField('Username',y=0,parent=signup_panel,z=-1,
                        color=color.rgba(0.5,0.5,0.5,0.6))
    user_s.highlight_color=color.rgba(0.5,0.5,0.5,0.6)

    passwords_s = InputField('Password',y=-0.2,parent=signup_panel,password=True,z=-1,
                             color=color.rgba(0.5,0.5,0.5,0.6))
    passwords_s.highlight_color=color.rgba(0.5,0.5,0.5,0.6)
    passwords_s.hide_content=True

    msg_s = Text("", parent=signup_panel, y=-0.1,x=-0.08, color=color.black)

    continue_s=Button('Continue',parent=signup_panel,y=-0.3,z=-1,x=-0.1,scale=(0.15,0.1),
                      color=color.rgba(0.5,0.5,0.5,0.6))
    continue_s.text_entity.scale=8

    cancel_s=Button('Cancel',parent=signup_panel,y=-0.3,x=0.1,scale=0.1,z=-1,
                    color=color.rgba(0.5,0.5,0.5,0.6))

    text_s=Text('Sign up',parent=signup_panel,y=0.3,x=-0.2,scale=5,
                color=color.white,z=-1)

    bg= Button(parent=camera.ui,
               color=color.white,
               scale=(2.5,3),
               position=(0,0),
               enabled=False,z=1,
               texture='assets/auth.jpg',
               texture_scale=(1.5,1.5))

    cred_entities.extend([login_door,signup_door,light,signin,login])
    
cred_room()

#=================================
# FUNCTIONS OF BUTTONS AND PANELS
#=================================

def show_sign_panel():
    player.enabled=False
    mouse.locked=False
    signup_panel.enabled=True
    bg.enabled=True

def hide_sign_panel():
    player.enabled=True
    mouse.locked=True
    signup_panel.enabled=False
    bg.enabled=False

def can_l():
    click.play()
    hide_login_panel()

def can_s():
    click.play()
    hide_sign_panel()

def show_login_panel():
    player.enabled=False
    mouse.locked=False
    login_panel.enabled=True
    bg.enabled=True
    
    
def hide_login_panel():
    player.enabled=True
    mouse.locked=True
    login_panel.enabled=False
    bg.enabled=False

def continue_login():
    if user_l.text and passwords_l.text and user_l.text !='Username' and passwords_l.text!='Password':
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
                  click.play()
                  cred_bg.stop()
                  hide_login_panel()
                  player.position=Vec3(0,0,16)
                  voice.play() 
                  siren.play()
        else:
             msg_l.text="login error"
             msg_l.color=color.white                  
            

    else:
        msg_l.text='please enter values for both fields'
  

def continue_sign():
    if user_s.text and passwords_s.text and user_s.text !='Username' and passwords_s.text!='Password':
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
        click.play()
        cred_bg.stop()
        hide_sign_panel()
        voice.play()
        siren.play()
        player.position=Vec3(0,0,16)
    
    else:
        msg_s.text='please enter values for both fields'
        
        
continue_s.on_click=continue_sign
continue_l.on_click=continue_login
cancel_l.on_click=can_l
cancel_s.on_click=can_s
    
#================
# GAME MECHANICS
#================

def update():
    if held_keys['b']:
        Dlight.color=color.rgba(0.5,0,0,80)
       
    if held_keys['escape']:
        application.quit()

    if distance(player.position,signup_door.position)<7 and held_keys['e']:
        click.play()
        show_sign_panel()

    else:
        signin.enabled=False

    if distance(player.position,login_door.position)<7 and held_keys['e']:
        click.play()
        show_login_panel()
        

    else:
        login.enabled=False

    bg.rotation_z += 1 * time.dt 

def power():
    Dlight.color=color.rgba(0.5,0.7,0.5,180)
    pow.color=color.green
    voice.stop()
    siren.stop()
    charge_m.play()
    bg_m()
    
#LIGHTING
Dlight=DirectionalLight()
Dlight.look_at(Vec3(1,-1,-1))
Dlight.color=color.rgba(0.5,0,0,80)
Dlight.parent=scene

Alight=AmbientLight()
Alight.color=color.rgba(10,10,10,255)
Alight.parent=scene

flicker_light = PointLight()
flicker_light.color = color.rgba(255, 50, 0, 200)  
flicker_light.position = Vec3(20, 5, 20)  
flicker_light.parent = scene


#SOUND
voice=Audio('assets/main_v.mp3',autoplay=False,loop=True)
siren=Audio('assets/main_a.mp3',autoplay=False,loop=True)
charge_m=Audio('assets/charge.mp3',autoplay=False)
main_bg=Audio('assets/mbg.mp3',autoplay=False,loop=True)
main_bg.volume=6
voice.volume=8
siren.volume=0.6

def bg_m():
    main_bg.play()
    
#========================
# ENTITIES FOR MAIN ROOM
#========================

#ADD FLOOR
Entity(model='plane',
       scale=50,
       collider='box',
       texture='floor.jpg',
       texture_scale=(10,10),
       color=color.white,
       shader=lit_with_shadows_shader
)


#ADD CEILNG
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

#ADD WALLS
wall5=Entity(model='cube',
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

# ADD POWER
pow_entity=Entity(position=(-24,8,8),
           model='cube',
           scale=1,
           color=color.black)

pow=Button(position=(0,0,1),
           model='cube',
           parent=pow_entity,
           scale=1,
           color=color.red,
           on_click=power)

#ADD TABLES
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

#ADD BUNSEN BUNER
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

#ADD TESTUBE STAND
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
    

# ADD HOLOGRAM
Entity(model= 'assets/hologram.glb',
       position=(0,4,0),
       scale=2.5,
       color=color.rgb(255,255,255),
       collider='sphere',
       shader=lit_with_shadows_shader)


#ADD SHELF
Entity(model='book_shelf.glb',
       scale =0.04,
       position=(-24,0,0),
       collider='box',
       color=color.white,
       shader=lit_with_shadows_shader,
       rotation_y=270)

#ADD FLAME
Entity(model='cube',
       scale=(0.05,0.05),
       collider='box',
       color=color.blue,
       position=(0,5,12),
       rotation_x=90,
       shader=lit_with_shadows_shader)

Entity(model='cube',
       scale=(0.05,0.05),
       collider='box',
       color=color.blue,
       position=(0,5,-12),
       rotation_x=90,
       shader=lit_with_shadows_shader)

Entity(model='cube',
       scale=(0.05,0.05),
       collider='box',
       color=color.blue,
       position=(16,5,12),
       rotation_x=90,
       shader=lit_with_shadows_shader)

Entity(model='cube',
       scale=(0.05,0.05),
       collider='box',
       color=color.blue,
       position=(-16,5,12),
       rotation_x=90,
       shader=lit_with_shadows_shader)

Entity(model='cube',
       scale=(0.05,0.05),
       collider='box',
       color=color.blue,
       position=(16,5,-12),
       rotation_x=90,
       shader=lit_with_shadows_shader)

Entity(model='cube',
       scale=(0.05,0.05),
       collider='box',
       color=color.blue,
       position=(-16,5,-12),
       rotation_x=90,
       shader=lit_with_shadows_shader)

# ADD CHEMICALS
Mg=Entity(model='assets/bottles.glb',
       scale=0.2,
       collider='box',
       color=color.white,
       position=(-23,4.3,2),
       shader=lit_with_shadows_shader)

Na=Entity(model='assets/bottles.glb',
       scale=0.2,
       collider='box',
       color=color.white,
       position=(-23,7,2),
       shader=lit_with_shadows_shader)

Al=Entity(model='assets/bottles.glb',
       scale=0.2,
       collider='box',
       color=color.white,
       position=(-23,5.5,2),
       shader=lit_with_shadows_shader)

Ca=Entity(model='assets/bottles.glb',
       scale=0.2,
       collider='box',
       color=color.white,
       position=(-23,3,2),
       shader=lit_with_shadows_shader)

Entity(model='assets/canister.glb',
       scale=0.006,
       collider='box',
       color=color.white,
       position=(-16,3.8,10),
       shader=lit_with_shadows_shader)

Entity(model='assets/canister.glb',
       scale=0.006,
       collider='box',
       color=color.white,
       position=(16,3.8,10),
       shader=lit_with_shadows_shader)

Entity(model='assets/canister.glb',
       scale=0.006,
       collider='box',
       color=color.white,
       position=(-16,3.8,-15),
       shader=lit_with_shadows_shader)

Entity(model='assets/canister.glb',
       scale=0.006,
       collider='box',
       color=color.white,
       position=(16,3.8,-15),
       shader=lit_with_shadows_shader)

Entity(model='assets/o2.glb',
       scale=1.5,
       collider='box',
       color=color.white,
       position=(16,7,-23.8),
       shader=lit_with_shadows_shader)

Entity(model='assets/o2.glb',
       scale=1.5,
       collider='box',
       color=color.white,
       position=(17,7,-23.8),
       shader=lit_with_shadows_shader)

Entity(model='assets/gas.glb',
       scale=5,
       collider='box',
       color=color.white,
       position=(18,7,-23.8),
       rotation_y=180,
       shader=lit_with_shadows_shader)
app.run()

#=========================================#





























































