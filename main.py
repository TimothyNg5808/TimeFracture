from gamelib import *
from music import *

game=Game(1480,820,"Time Fracture")

#Graphics
titlescreen=Image("titlescreen.jpg",game)
title=Image("title.png",game)
companyname=Image("companyname.png",game)
blackbackground=Image("blackbackground.jpg",game)
citybackground=Image("citybackground.png",game)
labbackground=Image("game8_screen.png",game)
story1=Image("story1.png",game)
start=Image("start.png",game)
play=Image("play.png",game)
story=Image("story.png",game)
howtoplay=Image("howtoplay.png",game)
wjwalk=Animation("wjwalk.png",10,game,507/10,74,4,use_alpha=False)
wjjump=Image("williamjacksonjump2.png",game,use_alpha=False)
begin=Image("begin.png",game)
loading=Image("loading.png",game)
loadingsymbol=Animation("loadingsymbol.png",17,game,1700/17,100,4,use_alpha=False)
pause=Image("pause.png",game)
unpause=Image("unpause.png",game)
mute=Image("mute.png",game)
unmute=Image("unmute.png",game)
level1=Image("level1.png",game)
level2=Image("Level-2.png",game)
level3=Image("Level-3.png",game)
level4=Image("Level-4.png",game)
font=Font(green,15,green,"Lucida Console")
font1=Font(red,15,red,"Lucida Console")
tip1=Image("tip1.png",game)
tip2=Image("tip2.png",game)
tip3=Image("Tip-You-Have-Powers.png",game)
tip4=Image("But-Use-Them-When-Necessary.png",game)
tip5=Image("tip5.png",game)
tip6=Image("tip6.png",game)
tip7=Image("tip7.png",game)
tip8=Image("tip8.png",game)
floorspikes=Image("floorspikes.png",game,use_alpha=False)
floorspikes1=Image("floorspikes.png",game,use_alpha=False)
floorspikes2=Image("floorspikes.png",game,use_alpha=False)
gameover=Image("gameover.jpg",game)
end=Image("end.png",game)
moveon=Image("Continue-To-Next-Level.png",game)
enemy=Animation("enemywalk.png",2,game,159/2,79,36,use_alpha=False)
enemy1=Animation("enemywalk.png",2,game,159/2,79,36,use_alpha=False)
enemy2=Animation("enemywalk.png",2,game,159/2,79,36,use_alpha=False)
bullet=Image("bullet2.png",game)
bullet1=Image("bullet.png",game)
bullet2=Image("bullet.png",game)
bullet3=Image("bullet.png",game)
controls=Image("controls.png",game)
controls1=Image("controls1.png",game)
controls2=Image("controls2.png",game)
page1=Image("1.png",game)
page2=Image("2.png",game)
page3=Image("3.png",game)
returnmenu=Image("Return-To-Menu.png",game)
aim=Image("aim2.png",game)
forcefield=Animation("forcefield.png",20,game,960/5,768/4,8)
timeblast=Animation("timeblast.png",10,game,640/10,64)
appear=Animation("magic_002.png",15,game,960/5,576/3,4,use_alpha=False)
boss=Image("boss.png",game)
bossweapon2=Animation("timeblast.png",10,game,640/10,64)
bossweapon1=Animation("timeblast.png",10,game,640/10,64)
bossweapon=Animation("timeblast.png",10,game,640/10,64)
victoryscreen=Image("victoryscreen.png",game)
victoryscreen1=Image("victoryscreen1.png",game)
victoryquit=Image("quit.png",game)

game.setBackground(citybackground)
citybackground.resizeTo(1480,820)
blackbackground.resizeTo(1480,820)
titlescreen.resizeTo(1480,820)
controls.resizeTo(1480,820)
controls1.resizeTo(1480,820)
controls2.resizeTo(1480,820)
story1.resizeTo(1480,820)
gameover.resizeBy(-25)

controls.visible=False
controls1.visible=False
controls2.visible=False
story1.visible=False
blackbackground.visible=False
forcefield.visible=False
title.y-=250
companyname.resizeBy(-50)
companyname.y+=380
start.y+=220
start.resizeBy(-50)
play.resizeBy(-25)
play.y-=50
story.resizeBy(-25)
story.y+=50
howtoplay.resizeBy(-20)
howtoplay.y+=150
returnmenu.resizeBy(-45)
returnmenu.moveTo(215,25)
returnmenu.visible=False
page1.resizeBy(-45)
page1.moveTo(25,600)
page1.visible=False
page2.resizeBy(-45)
page2.moveTo(25,680)
page2.visible=False
page3.resizeBy(-45)
page3.moveTo(25,765)
page3.visible=False
wjwalk.resizeBy(40)
wjjump.resizeBy(40)
wjjump.visible=False
begin.resizeBy(-25)
begin.y+=340
begin.visible=False
loading.resizeBy(-25)
loading.y+=340
loadingsymbol.resizeBy(-35)
loadingsymbol.y+=370
loadingsymbol.x+=710
pause.resizeBy(-65)
pause.y-=380
pause.x-=550
mute.resizeBy(-65)
mute.y-=380
mute.x+=500
unmute.resizeBy(-65)
unmute.y-=340
unmute.x+=500
level1.resizeBy(-15)
level1.y-=370
level2.resizeBy(-15)
level2.y-=370
level3.resizeBy(-15)
level3.y-=370
level4.resizeBy(-15)
level4.y-=370
tip1.resizeBy(-25)
tip2.resizeBy(-25)
tip2.y+=60
tip3.resizeBy(-25)
tip4.resizeBy(-25)
tip4.y+=60
tip5.resizeBy(-25)
tip6.resizeBy(-25)
tip6.y+=60
tip7.resizeBy(-25)
tip7.y+=120
tip8.resizeBy(-25)
floorspikes.resizeBy(-70)
floorspikes.moveTo(game.width,675)
floorspikes.setSpeed(4.8,90)
floorspikes1.resizeBy(-70)
floorspikes1.moveTo(game.width+150,675)
floorspikes1.setSpeed(4.8,90)
floorspikes2.resizeBy(-70)
floorspikes2.moveTo(game.width+300,675)
floorspikes2.setSpeed(4.8,90)
end.y+=100
end.resizeBy(-45)
moveon.resizeBy(-25)
enemy.moveTo(1690,660)
enemy1.moveTo(1750,660)
enemy2.moveTo(1880,660)
bullet.resizeBy(-85)
bullet.visible=False
bullet1.resizeBy(-85)
bullet1.moveTo(enemy.x,enemy.y)
bullet1.visible=False
bullet2.resizeBy(-85)
bullet2.moveTo(enemy1.x,enemy1.y)
bullet2.visible=False
bullet3.resizeBy(-85)
bullet3.moveTo(enemy2.x,enemy2.y)
bullet3.visible=False
aim.resizeBy(-79)
timeblast.visible=False
timeblast.resizeBy(-35)
bossweapon.visible=False
bossweapon.resizeBy(-35)
bossweapon1.visible=False
bossweapon1.resizeBy(-35)
bossweapon2.visible=False
bossweapon2.resizeBy(-35)
appear.resizeBy(-30)
boss.resizeBy(-30)
boss.x+=300
boss.y+=230
victoryscreen.resizeBy(-50)
victoryscreen1.resizeBy(-50)
victoryscreen1.y+=45
victoryquit.resizeBy(-45)
victoryquit.y+=150

#Health Packs
healthpacks=[]
for index in range(10):
    healthpacks.append(Image("healthpack.png",game,use_alpha = False))

for index in range(10):
    x=randint(100,1300)
    z=randint(1,3)
    healthpacks[index].moveTo(x,-950)
    healthpacks[index].setSpeed(z,180)
    healthpacks[index].resizeBy(-80)

healthpacks1=[]
for index in range(10):
    healthpacks1.append(Image("healthpack.png",game,use_alpha = False))

for index in range(10):
    x=randint(100,1300)
    z=randint(1,3)
    healthpacks1[index].moveTo(x,-1450)
    healthpacks1[index].setSpeed(z,180)
    healthpacks1[index].resizeBy(-80)

healthpacks2=[]
for index in range(10):
    healthpacks2.append(Image("healthpack.png",game,use_alpha = False))

for index in range(10):
    x=randint(100,1300)
    z=randint(1,3)
    healthpacks2[index].moveTo(x,-1680)
    healthpacks2[index].setSpeed(z,180)
    healthpacks2[index].resizeBy(-80)

healthpacks3=[]
for index in range(10):
    healthpacks3.append(Image("healthpack.png",game,use_alpha = False))

for index in range(10):
    x=randint(100,1300)
    z=randint(1,3)
    healthpacks3[index].moveTo(x,-950)
    healthpacks3[index].setSpeed(z,180)
    healthpacks3[index].resizeBy(-80)

healthpacks4=[]
for index in range(10):
    healthpacks4.append(Image("healthpack.png",game,use_alpha = False))

for index in range(10):
    x=randint(100,1300)
    z=randint(1,3)
    healthpacks4[index].moveTo(x,-1450)
    healthpacks4[index].setSpeed(z,180)
    healthpacks4[index].resizeBy(-80)

healthpacks5=[]
for index in range(10):
    healthpacks5.append(Image("healthpack.png",game,use_alpha = False))

for index in range(10):
    x=randint(100,1300)
    z=randint(1,3)
    healthpacks5[index].moveTo(x,-1680)
    healthpacks5[index].setSpeed(z,180)
    healthpacks5[index].resizeBy(-80)

#Power Packs
powerpacks=[]
for index in range(10):
    powerpacks.append(Animation("magic_001.png",30,game,960/5,1152/6,4,use_alpha=False))

for index in range(10):
    x=randint(250,1300)
    z=randint(1,3)
    powerpacks[index].moveTo(x,-950)
    powerpacks[index].setSpeed(z,180)
    powerpacks[index].resizeBy(-80)

powerpacks1=[]
for index in range(10):
    powerpacks1.append(Animation("magic_001.png",30,game,960/5,1152/6,4,use_alpha=False))

for index in range(10):
    x=randint(250,1300)
    z=randint(1,3)
    powerpacks1[index].moveTo(x,-1450)
    powerpacks1[index].setSpeed(z,180)
    powerpacks1[index].resizeBy(-80)

powerpacks2=[]
for index in range(10):
    powerpacks2.append(Animation("magic_001.png",30,game,960/5,1152/6,4,use_alpha=False))

for index in range(10):
    x=randint(250,1300)
    z=randint(1,3)
    powerpacks2[index].moveTo(x,-1680)
    powerpacks2[index].setSpeed(z,180)
    powerpacks2[index].resizeBy(-80)
    
powerpacks3=[]
for index in range(10):
    powerpacks3.append(Animation("magic_001.png",30,game,960/5,1152/6,4,use_alpha=False))

for index in range(10):
    x=randint(250,1300)
    z=randint(1,3)
    powerpacks3[index].moveTo(x,-950)
    powerpacks3[index].setSpeed(z,180)
    powerpacks3[index].resizeBy(-80)

powerpacks4=[]
for index in range(10):
    powerpacks4.append(Animation("magic_001.png",30,game,960/5,1152/6,4,use_alpha=False))

for index in range(10):
    x=randint(250,1300)
    z=randint(1,3)
    powerpacks4[index].moveTo(x,-1450)
    powerpacks4[index].setSpeed(z,180)
    powerpacks4[index].resizeBy(-80)

powerpacks5=[]
for index in range(10):
    powerpacks5.append(Animation("magic_001.png",30,game,960/5,1152/6,4,use_alpha=False))

for index in range(10):
    x=randint(250,1300)
    z=randint(1,3)
    powerpacks5[index].moveTo(x,-1680)
    powerpacks5[index].setSpeed(z,180)
    powerpacks5[index].resizeBy(-80)

#Sounds
gun=Sound("Gun.wav",1)
death=Sound("death.wav",2)
pickup=Sound("pickup.wav",3)
damage=Sound("damage.wav",4)
selection=Sound("selection.wav",5)
timeblastsound=Sound("timeblast.wav",6)

#Startup Screen
meunMusic()
playmeunMusic()

while not game.over:
    game.processInput()
    
    titlescreen.draw()
    title.draw()
    companyname.draw()
    start.draw()
    
    if start.collidedWith(mouse) and mouse.LeftClick:
        selection.play()
        game.over=True
            
    game.update(151)
game.over=False

#Main Meun
while not game.over:
    game.processInput()

    titlescreen.draw()
    play.draw()
    story.draw()
    howtoplay.draw()
    blackbackground.draw()
    controls.draw()
    controls1.draw()
    controls2.draw()
    story1.draw()
    returnmenu.draw()
    page1.draw()
    page2.draw()
    page3.draw()
    
    if play.collidedWith(mouse) and mouse.LeftClick:
        stopmeunMusic()
        selection.play()
        game.over=True

    if returnmenu.collidedWith(mouse) and mouse.LeftClick:
        selection.play()
        play.visible=True
        story.visible=True
        howtoplay.visible=True
        blackbackground.visible=False
        returnmenu.visible=False
        controls2.visible=False
        controls1.visible=False
        controls.visible=False
        story1.visible=False
        page1.visible=False
        page2.visible=False
        page3.visible=False

    if story.collidedWith(mouse) and mouse.LeftClick:
        selection.play()
        story1.visible=True
        blackbackground.visible=True
        returnmenu.visible=True
        play.visible=False
        story.visible=False
        howtoplay.visible=False

    if howtoplay.collidedWith(mouse) and mouse.LeftClick:
        selection.play()
        controls.visible=True
        returnmenu.visible=True
        page1.visible=True
        page2.visible=True
        page3.visible=True
        play.visible=False
        story.visible=False
        howtoplay.visible=False

    if page1.collidedWith(mouse) and mouse.LeftClick:
        selection.play()
        controls1.visible=False
        controls2.visible=False
        controls.visible=True

    if page2.collidedWith(mouse) and mouse.LeftClick:
        selection.play()
        controls1.visible=True
        controls2.visible=False
        controls.visible=False

    if page3.collidedWith(mouse) and mouse.LeftClick:
        selection.play()
        controls1.visible=False
        controls2.visible=True
        controls.visible=False

    game.update(151)
    
game.over=False

#Loading Screen
loadingMusic()
playloadingMusic()

time=651

game.viewMouse(True)

while not game.over:
    game.processInput()

    blackbackground.draw()
    blackbackground.visible=True
    begin.draw()
    loading.draw()
    loadingsymbol.draw()
    level1.draw()
    tip1.draw()
    tip2.draw()

    if time>0:
        game.update(101)
        time-=1
        continue

    if time<2:
        begin.visible=True
        loading.visible=False
        loadingsymbol.visible=False
    
    if begin.collidedWith(mouse) and mouse.LeftClick:
        stoploadingMusic()
        selection.play()
        game.over=True

    game.update(151)
game.over=False

#Level 1
gameMusic()
playgameMusic()

time=3250
powerlevel=0
jumpboost=100

game.viewMouse(False)

while not game.over:
    game.processInput()

    citybackground.move()
    game.scrollBackground("left",3.5)
    pause.draw()
    wjwalk.move()
    wjjump.move()
    wjjump.moveTo(wjwalk.x,wjwalk.y)
    mute.draw()
    unmute.draw()
    level1.draw()
    floorspikes.move()
    floorspikes1.move()
    floorspikes2.move()

    for index in range(10):
        healthpacks[index].move()

        if healthpacks[index].collidedWith(wjwalk,"rectangle"):
            wjwalk.health+=20
            pickup.play()
            healthpacks[index].visible=False

        if healthpacks[index].collidedWith(wjjump,"rectangle"):
            wjwalk.health+=20
            pickup.play()
            healthpacks[index].visible=False

        if healthpacks[index].y>700:
            healthpacks[index].visible=False

    for index in range(10):
        healthpacks1[index].move()

        if healthpacks1[index].collidedWith(wjwalk,"rectangle"):
            wjwalk.health+=20
            pickup.play()
            healthpacks1[index].visible=False

        if healthpacks1[index].collidedWith(wjjump,"rectangle"):
            wjwalk.health+=20
            pickup.play()
            healthpacks1[index].visible=False

        if healthpacks1[index].y>700:
            healthpacks1[index].visible=False

    for index in range(10):
        healthpacks2[index].move()

        if healthpacks2[index].collidedWith(wjwalk,"rectangle"):
            wjwalk.health+=20
            pickup.play()
            healthpacks2[index].visible=False

        if healthpacks2[index].collidedWith(wjjump,"rectangle"):
            wjwalk.health+=20
            pickup.play()
            healthpacks2[index].visible=False

        if healthpacks2[index].y>700:
            healthpacks2[index].visible=False
            
    for index in range(10):
        powerpacks[index].move()

        if powerpacks[index].collidedWith(wjwalk,"rectangle"):
            powerlevel+=30
            pickup.play()
            powerpacks[index].visible=False

        if powerpacks[index].collidedWith(wjjump,"rectangle"):
            powerlevel+=30
            pickup.play()
            powerpacks[index].visible=False

        if powerpacks[index].y>700:
            powerpacks[index].visible=False

    for index in range(10):
        powerpacks1[index].move()

        if powerpacks1[index].collidedWith(wjwalk,"rectangle"):
            powerlevel+=30
            pickup.play()
            powerpacks1[index].visible=False

        if powerpacks1[index].collidedWith(wjjump,"rectangle"):
            powerlevel+=30
            pickup.play()
            powerpacks1[index].visible=False

        if powerpacks1[index].y>700:
            powerpacks1[index].visible=False

    for index in range(10):
        powerpacks2[index].move()

        if powerpacks2[index].collidedWith(wjwalk,"rectangle"):
            powerlevel+=30
            pickup.play()
            powerpacks2[index].visible=False

        if powerpacks2[index].collidedWith(wjjump,"rectangle"):
            powerlevel+=30
            pickup.play()
            powerpacks2[index].visible=False

        if powerpacks2[index].y>700:
            powerpacks2[index].visible=False

    if floorspikes.isOffScreen("left"):
        x=randint(1495,1595)
        floorspikes.moveTo(x,675)

    if floorspikes.collidedWith(wjwalk):
        wjwalk.health-=2
        damage.play()

    if floorspikes.collidedWith(wjjump):
        wjwalk.health-=2
        damage.play()

    if floorspikes1.isOffScreen("left"):
        x=randint(1620,1700)
        floorspikes1.moveTo(x,675)

    if floorspikes1.collidedWith(wjwalk):
        wjwalk.health-=2
        damage.play()

    if floorspikes1.collidedWith(wjjump):
        wjwalk.health-=2
        damage.play()

    if floorspikes2.isOffScreen("left"):
        x=randint(1750,1830)
        floorspikes2.moveTo(x,675)

    if floorspikes2.collidedWith(wjwalk):
        wjwalk.health-=2
        damage.play()

    if floorspikes2.collidedWith(wjjump):
        wjwalk.health-=2
        damage.play()
        
    #Game Controls
    if wjwalk.y<665 or wjjump.y<665:
        wjwalk.y+=4
        wjjump.y+=4
    
    if keys.Pressed[K_d]:
        wjwalk.x+=3.77
    elif keys.Pressed[K_d]:
        wjwalk.x-=3.77

    if not keys.Pressed[K_d]:
        wjwalk.x-=1

    if keys.Pressed[K_a]:
        wjwalk.x-=3.77
        
    if keys.Pressed[K_w]:
        wjwalk.visible=False
        wjjump.visible=True
        wjwalk.y-=7.2
        wjjump.y-=7.2
        jumpboost-=1
        
    if jumpboost<0:
        wjwalk.y+=4
        wjjump.y+=4
        jumpboost+=1

    if jumpboost<100 and not keys.Pressed[K_w]:
        jumpboost+=1
        
    if jumpboost>100:
        jumpboost-=1
        jumpboost+=1
        
    if not keys.Pressed[K_w]:
        wjwalk.visible=True
        wjjump.visible=False

    if keys.Pressed[K_s]:
        wjwalk.y+=7.2
        wjjump.y+=7.2

    if wjwalk.y>675 or wjwalk.y>675:
        wjwalk.y-=7.2

    if keys.Pressed[K_ESCAPE]:
        unpause.draw()
        game.update(101)
        game.wait(K_TAB)

    if keys.Pressed[K_n]:
        stopgameMusic()

    if keys.Pressed[K_m]:
        playgameMusic()

    game.drawText("Your Health:"+str(wjwalk.health),5,65,font)
    game.drawText("Your Power Level:"+str(powerlevel),5,85,font)
    game.drawText("Your Jump Boost Fuel:"+str(jumpboost),5,105,font)
    
    #Game Over
    if wjwalk.health<1:
        stopgameMusic()
        death.play()
        game.clearBackground()
        gameover.draw()
        end.draw()
        game.update(151)
        game.wait(K_RETURN)
        game.quit()

    if time>0:
        game.update(101)
        time-=1
        continue

    if time<1:
        game.viewMouse(True)
        moveon.draw()
        floorspikes.visible=False
        floorspikes1.visible=False
        floorspikes2.visible=False

    if moveon.collidedWith(mouse) and mouse.LeftClick:
        game.over=True
    
    game.update(151)
game.over=False

#Loading Screen 2
loadingMusic()
playloadingMusic()

time=651

game.viewMouse(True)

while not game.over:
    game.processInput()

    blackbackground.draw()
    blackbackground.visible=True
    begin.draw()
    loading.draw()
    loadingsymbol.draw()
    level2.draw()
    tip3.draw()
    tip4.draw()
    begin.visible=False
    loading.visible=True
    loadingsymbol.visible=True

    if time>-1:
        game.update(101)
        time-=1
        continue

    if time<2:
        begin.visible=True
        loading.visible=False
        loadingsymbol.visible=False
    
    if begin.collidedWith(mouse) and mouse.LeftClick:
        stoploadingMusic()
        selection.play()
        game.over=True

    game.update(151)
game.over=False

#Level 2
gameMusic()
playgameMusic()

time=4000

jumpboost=100
enemyfire=0
enemyfire1=0
enemyfire2=0
forcefieldtime=1500

game.viewMouse(False)

while not game.over:
    game.processInput()

    citybackground.move()
    game.scrollBackground("left",3.5)
    pause.draw()
    aim.draw()
    aim.moveTo(mouse.x-53,mouse.y)
    wjwalk.move()
    wjjump.move()
    wjjump.moveTo(wjwalk.x,wjwalk.y)
    mute.draw()
    unmute.draw()
    level2.draw()
    bullet.move()
    timeblast.move()
    
    if forcefield.visible:
        forcefield.move()
        forcefield.moveTo(wjwalk.x,wjwalk.y)
        forcefieldtime-=1
        
    enemy.move()
    x=randint(1,3)
    enemy.setSpeed(x,90)

    enemy1.move()
    y=randint(2,4)
    enemy1.setSpeed(y,90)

    enemy2.move()
    enemy2.setSpeed(2,90)

    if enemy.isOffScreen("left"):
        x=randint(1500,1600)
        enemy.moveTo(x,660)

    if enemy1.isOffScreen("left"):
        x=randint(1550,1650)
        enemy1.moveTo(x,660)

    if enemy2.isOffScreen("left"):
        x=randint(1620,1700)
        enemy2.moveTo(x,660)

    bullet1.move()
    bullet2.move()
    bullet3.move()

    if enemyfire<271:
        enemyfire+=1

    if enemyfire>270:
        enemyfire-=271
        gun.play()
        bullet1.setSpeed(5.3,90)
        bullet1.visible=True

    if bullet1.collidedWith(wjwalk) or bullet1.collidedWith(wjjump):
        wjwalk.health-=5
        damage.play()
        bullet1.moveTo(enemy.x,enemy.y)
        bullet1.visible=False

    if bullet1.isOffScreen("left"):
        bullet1.moveTo(enemy.x,enemy.y)
        bullet1.visible=False
        
    if enemyfire1<251:
        enemyfire1+=1

    if enemyfire1>250:
        enemyfire1-=251
        gun.play()
        bullet2.setSpeed(5.3,90)
        bullet2.visible=True

    if bullet2.collidedWith(wjwalk) or bullet2.collidedWith(wjjump):
        wjwalk.health-=5
        damage.play()
        bullet2.moveTo(enemy1.x,enemy1.y)
        bullet2.visible=False

    if bullet2.isOffScreen("left"):
        bullet2.moveTo(enemy1.x,enemy1.y)
        bullet2.visible=False

    if enemyfire2<251:
        enemyfire2+=1

    if enemyfire2>250:
        enemyfire2-=251
        gun.play()
        bullet3.setSpeed(5.3,90)
        bullet3.visible=True

    if bullet3.collidedWith(wjwalk) or bullet3.collidedWith(wjjump):
        wjwalk.health-=5
        damage.play()
        bullet3.moveTo(enemy2.x,enemy2.y)
        bullet3.visible=False

    if bullet3.isOffScreen("left"):
        bullet3.moveTo(enemy2.x,enemy2.y)
        bullet3.visible=False

    #Game Controls
    if wjwalk.y<665 or wjjump.y<665:
        wjwalk.y+=4
        wjjump.y+=4
    
    if keys.Pressed[K_d]:
        wjwalk.x+=3.77
    elif keys.Pressed[K_d]:
        wjwalk.x-=3.77

    if not keys.Pressed[K_d]:
        wjwalk.x-=1

    if keys.Pressed[K_a]:
        wjwalk.x-=3.77
    
    if keys.Pressed[K_w]:
        wjwalk.visible=False
        wjjump.visible=True
        wjwalk.y-=5.7
        wjjump.y-=5.7
        jumpboost-=1
        
    if jumpboost<0:
        wjwalk.y+=4
        wjjump.y+=4
        jumpboost+=1

    if jumpboost<100 and not keys.Pressed[K_w]:
        jumpboost+=1
        
    if jumpboost>100:
        jumpboost-=1
        jumpboost+=1
        
    if not keys.Pressed[K_w]:
        wjwalk.visible=True
        wjjump.visible=False

    if keys.Pressed[K_s]:
        wjwalk.y+=5.7
        wjjump.y+=5.7

    if wjwalk.y>675:
        wjwalk.y-=5.7

    if keys.Pressed[K_SPACE]:
        bullet.moveTo(wjwalk.x+15,wjwalk.y-30)
        angleToCrosshair=bullet.angleTo(aim)
        bullet.setSpeed(8.4,angleToCrosshair)
        bullet.visible=True
        gun.play()

    if bullet.collidedWith(enemy,"rectangle"):
        bullet.visible=False
        bullet1.moveTo(enemy.x,enemy.y)
        x=randint(1500,1600)
        enemy.moveTo(x,660)

    if bullet.collidedWith(enemy1,"rectangle"):
        bullet.visible=False
        bullet2.moveTo(enemy1.x,enemy1.y)
        x=randint(1550,1650)
        enemy1.moveTo(x,660)
        
    if bullet.collidedWith(enemy2,"rectangle"):
        bullet.visible=False
        bullet3.moveTo(enemy2.x,enemy2.y)
        x=randint(1620,1700)
        enemy2.moveTo(x,660)

    if bullet.x>1450:
        bullet.visible=False
        bullet.moveTo(wjwalk.x+15,wjwalk.y-30)

    if keys.Pressed[K_LCTRL]:
        forcefield.visible=not forcefield.visible
        powerlevel-=20

    if forcefieldtime<0:
        forcefield.visible=False

    if bullet1.collidedWith(forcefield,"circle") or bullet2.collidedWith(forcefield,"circle") or bullet3.collidedWith(forcefield,"circle"):
        bullet1.visible=False
        bullet2.visible=False
        bullet3.visible=False

    if keys.Pressed[K_LALT]:
        timeblast.moveTo(wjwalk.x+15,wjwalk.y-30)
        angleToCrosshair=timeblast.angleTo(aim)
        timeblast.setSpeed(7.5,angleToCrosshair)
        timeblast.visible=True
        timeblastsound.play()
        powerlevel-=10

    if timeblast.collidedWith(enemy):
        bullet1.moveTo(enemy.x,enemy.y)
        x=randint(1500,1600)
        enemy.moveTo(x,660)

    if timeblast.collidedWith(enemy1):
        bullet2.moveTo(enemy1.x,enemy1.y)
        x=randint(1550,1650)
        enemy1.moveTo(x,660)
        
    if timeblast.collidedWith(enemy2):
        bullet3.moveTo(enemy2.x,enemy2.y)
        x=randint(1620,1700)
        enemy2.moveTo(x,660)

    if timeblast.x>1500:
        timeblast.visible=False
        timeblast.moveTo(wjwalk.x+15,wjwalk.y-30)

    if keys.Pressed[K_LSHIFT]:
        bullet1.setSpeed(1.8,90)
        bullet2.setSpeed(1.8,90)
        bullet3.setSpeed(1.8,90)
        enemy.setSpeed(1,90)
        enemy1.setSpeed(1,90)
        enemy2.setSpeed(1,90)
        powerlevel-=1

    if not keys.Pressed[K_LSHIFT] or powerlevel<1:
        bullet1.setSpeed(5.3,90)
        bullet2.setSpeed(5.3,90)
        bullet3.setSpeed(5.3,90)
        x=randint(1,3)
        enemy.setSpeed(x,90)
        y=randint(2,4)
        enemy1.setSpeed(y,90)
        enemy2.setSpeed(2,90)

    if powerlevel<1:
        if keys.Pressed[K_LALT]:
            timeblast.visible=False

        if keys.Pressed[K_LCTRL]:
            forcefield.visible=False

    if powerlevel<-1:
        powerlevel+=1

    if powerlevel<1:
        powerlevel+=1
             
    if keys.Pressed[K_ESCAPE]:
        unpause.draw()
        game.update(101)
        game.wait(K_TAB)

    if keys.Pressed[K_n]:
        stopgameMusic()

    if keys.Pressed[K_m]:
        playgameMusic()

    game.drawText("Your Health:"+str(wjwalk.health),5,65,font)
    game.drawText("Your Power Level:"+str(powerlevel),5,85,font)
    game.drawText("Your Jump Boost Fuel:"+str(jumpboost),5,105,font)

    #Game Over
    if wjwalk.health<1:
        stopgameMusic()
        death.play()
        game.clearBackground()
        gameover.draw()
        end.draw()
        game.update(151)
        game.wait(K_RETURN)
        game.quit()

    if time>0:
        game.update(101)
        time-=1
        continue

    if time<1:
        game.viewMouse(True)
        moveon.draw()
        enemy.visible=False
        enemy1.visible=False
        enemy2.visible=False

    if moveon.collidedWith(mouse) and mouse.LeftClick:
        game.over=True

    game.update(151)
game.over=False

#Loading Screen 3
loadingMusic()
playloadingMusic()

time=651

game.viewMouse(True)

while not game.over:
    game.processInput()

    blackbackground.draw()
    blackbackground.visible=True
    begin.draw()
    loading.draw()
    loadingsymbol.draw()
    level3.draw()
    tip5.draw()
    tip6.draw()
    tip7.draw()
    begin.visible=False
    loading.visible=True
    loadingsymbol.visible=True

    if time>-1:
        game.update(101)
        time-=1
        continue

    if time<2:
        begin.visible=True
        loading.visible=False
        loadingsymbol.visible=False
    
    if begin.collidedWith(mouse) and mouse.LeftClick:
        stoploadingMusic()
        selection.play()
        game.over=True

    game.update(151)
game.over=False

#Level 3
bossMusic()
playbossMusic()

game.setBackground(labbackground)
labbackground.resizeTo(1480,820)

time=3850

jumpboost=100
enemyfire=0
enemyfire1=0
enemyfire2=0
forcefieldtime=1500

enemy.moveTo(1690,715)
enemy1.moveTo(1750,715)
enemy2.moveTo(1880,715)

game.viewMouse(False)

while not game.over:
    game.processInput()

    labbackground.move()
    game.scrollBackground("left",3.5)
    pause.draw()
    wjwalk.move()
    wjjump.move()
    wjjump.moveTo(wjwalk.x,wjwalk.y)
    mute.draw()
    unmute.draw()
    level3.draw()
    bullet.move()
    aim.draw()
    aim.moveTo(mouse.x-53,mouse.y)
    timeblast.move()
    enemy.visible=True
    enemy1.visible=True
    enemy2.visible=True
    enemyangleTo=bullet1.angleTo(wjwalk)
    enemy1angleTo=bullet2.angleTo(wjwalk)
    enemy2angleTo=bullet3.angleTo(wjwalk)

    if forcefield.visible:
        forcefield.move()
        forcefield.moveTo(wjwalk.x,wjwalk.y)
        forcefieldtime-=1

    for index in range(10):
        healthpacks3[index].move()

        if healthpacks3[index].collidedWith(wjwalk,"rectangle"):
            wjwalk.health+=20
            pickup.play()
            healthpacks3[index].visible=False

        if healthpacks3[index].collidedWith(wjjump,"rectangle"):
            wjwalk.health+=20
            pickup.play()
            healthpacks3[index].visible=False

        if healthpacks3[index].y>730:
            healthpacks3[index].visible=False

    for index in range(10):
        healthpacks4[index].move()

        if healthpacks4[index].collidedWith(wjwalk,"rectangle"):
            wjwalk.health+=20
            pickup.play()
            healthpacks4[index].visible=False

        if healthpacks4[index].collidedWith(wjjump,"rectangle"):
            wjwalk.health+=20
            pickup.play()
            healthpacks4[index].visible=False

        if healthpacks4[index].y>730:
            healthpacks4[index].visible=False

    for index in range(10):
        healthpacks5[index].move()

        if healthpacks5[index].collidedWith(wjwalk,"rectangle"):
            wjwalk.health+=20
            pickup.play()
            healthpacks5[index].visible=False

        if healthpacks5[index].collidedWith(wjjump,"rectangle"):
            wjwalk.health+=20
            pickup.play()
            healthpacks5[index].visible=False

        if healthpacks5[index].y>730:
            healthpacks5[index].visible=False
            
    for index in range(10):
        powerpacks3[index].move()

        if powerpacks3[index].collidedWith(wjwalk,"rectangle"):
            powerlevel+=30
            pickup.play()
            powerpacks3[index].visible=False

        if powerpacks3[index].collidedWith(wjjump,"rectangle"):
            powerlevel+=30
            pickup.play()
            powerpacks3[index].visible=False

        if powerpacks3[index].y>730:
            powerpacks3[index].visible=False

    for index in range(10):
        powerpacks4[index].move()

        if powerpacks4[index].collidedWith(wjwalk,"rectangle"):
            powerlevel+=30
            pickup.play()
            powerpacks4[index].visible=False

        if powerpacks4[index].collidedWith(wjjump,"rectangle"):
            powerlevel+=30
            pickup.play()
            powerpacks4[index].visible=False

        if powerpacks4[index].y>730:
            powerpacks4[index].visible=False

    for index in range(10):
        powerpacks5[index].move()

        if powerpacks5[index].collidedWith(wjwalk,"rectangle"):
            powerlevel+=30
            pickup.play()
            powerpacks5[index].visible=False

        if powerpacks5[index].collidedWith(wjjump,"rectangle"):
            powerlevel+=30
            pickup.play()
            powerpacks5[index].visible=False

        if powerpacks5[index].y>730:
            powerpacks5[index].visible=False
    
    enemy.move()
    x=randint(1,3)
    enemy.setSpeed(x,90)

    enemy1.move()
    y=randint(2,4)
    enemy1.setSpeed(y,90)

    enemy2.move()
    enemy2.setSpeed(2,90)

    if enemy.isOffScreen("left"):
        x=randint(1500,1600)
        enemy.moveTo(x,715)

    if enemy1.isOffScreen("left"):
        x=randint(1550,1650)
        enemy1.moveTo(x,715)

    if enemy2.isOffScreen("left"):
        x=randint(1620,1700)
        enemy2.moveTo(x,715)

    bullet1.move()
    bullet2.move()
    bullet3.move()

    if enemyfire<271:
        enemyfire+=1

    if enemyfire>270:
        enemyfire-=271
        gun.play()
        bullet1.setSpeed(5.3,enemyangleTo)
        bullet1.visible=True

    if bullet1.collidedWith(wjwalk) or bullet1.collidedWith(wjjump):
        wjwalk.health-=5
        damage.play()
        bullet1.moveTo(enemy.x,enemy.y)
        bullet1.visible=False

    if bullet1.isOffScreen("left"):
        bullet1.moveTo(enemy.x,enemy.y)
        bullet1.visible=False
        
    if enemyfire1<251:
        enemyfire1+=1

    if enemyfire1>250:
        enemyfire1-=251
        gun.play()
        bullet2.setSpeed(5.3,enemy1angleTo)
        bullet2.visible=True

    if bullet2.collidedWith(wjwalk) or bullet2.collidedWith(wjjump):
        wjwalk.health-=5
        damage.play()
        bullet2.moveTo(enemy1.x,enemy1.y)
        bullet2.visible=False

    if bullet2.isOffScreen("left"):
        bullet2.moveTo(enemy1.x,enemy1.y)
        bullet2.visible=False

    if enemyfire2<251:
        enemyfire2+=1

    if enemyfire2>250:
        enemyfire2-=251
        gun.play()
        bullet3.setSpeed(5.3,enemy2angleTo)
        bullet3.visible=True

    if bullet3.collidedWith(wjwalk) or bullet3.collidedWith(wjjump):
        wjwalk.health-=5
        damage.play()
        bullet3.moveTo(enemy2.x,enemy2.y)
        bullet3.visible=False

    if bullet3.isOffScreen("left"):
        bullet3.moveTo(enemy2.x,enemy2.y)
        bullet3.visible=False

    #Game Controls
    if wjwalk.y<700 or wjjump.y<700:
        wjwalk.y+=4
        wjjump.y+=4
    
    if keys.Pressed[K_d]:
        wjwalk.x+=3.77
    elif keys.Pressed[K_d]:
        wjwalk.x-=3.77

    if not keys.Pressed[K_d]:
        wjwalk.x-=1

    if keys.Pressed[K_a]:
        wjwalk.x-=3.77
    
    if keys.Pressed[K_w]:
        wjwalk.visible=False
        wjjump.visible=True
        wjwalk.y-=5.7
        wjjump.y-=5.7
        jumpboost-=1
        
    if jumpboost<0:
        wjwalk.y+=4
        wjjump.y+=4
        jumpboost+=1

    if jumpboost<100 and not keys.Pressed[K_w]:
        jumpboost+=1
        
    if jumpboost>100:
        jumpboost-=1
        jumpboost+=1
        
    if not keys.Pressed[K_w]:
        wjwalk.visible=True
        wjjump.visible=False

    if keys.Pressed[K_s]:
        wjwalk.y+=5.7
        wjjump.y+=5.7

    if wjwalk.y>725:
        wjwalk.y-=5.7

    if keys.Pressed[K_SPACE]:
        bullet.moveTo(wjwalk.x+15,wjwalk.y-30)
        angleToCrosshair = bullet.angleTo(aim)
        bullet.setSpeed(8.4,angleToCrosshair)
        bullet.visible=True
        gun.play()

    if bullet.collidedWith(enemy,"rectangle"):
        bullet.visible=False
        bullet1.moveTo(enemy.x,enemy.y)
        x=randint(1500,1600)
        enemy.moveTo(x,715)

    if bullet.collidedWith(enemy1,"rectangle"):
        bullet.visible=False
        bullet2.moveTo(enemy1.x,enemy1.y)
        x=randint(1550,1650)
        enemy1.moveTo(x,715)
        
    if bullet.collidedWith(enemy2,"rectangle"):
        bullet.visible=False
        bullet3.moveTo(enemy2.x,enemy2.y)
        x=randint(1620,1700)
        enemy2.moveTo(x,715)

    if bullet.x>1450:
        bullet.visible=False
        bullet.moveTo(wjwalk.x+15,wjwalk.y-30)

    if keys.Pressed[K_LCTRL]:
        forcefield.visible=not forcefield.visible

    if forcefieldtime<0:
        forcefield.visible=False

    if bullet1.collidedWith(forcefield,"circle") or bullet2.collidedWith(forcefield,"circle") or bullet3.collidedWith(forcefield,"circle"):
        bullet1.visible=False
        bullet2.visible=False
        bullet3.visible=False

    if keys.Pressed[K_LALT]:
        timeblast.moveTo(wjwalk.x+15,wjwalk.y-30)
        angleToCrosshair=timeblast.angleTo(aim)
        timeblast.setSpeed(7.5,angleToCrosshair)
        timeblast.visible=True
        timeblastsound.play()
        powerlevel-=10

    if timeblast.collidedWith(enemy):
        bullet1.moveTo(enemy.x,enemy.y)
        x=randint(1500,1600)
        enemy.moveTo(x,715)

    if timeblast.collidedWith(enemy1):
        bullet2.moveTo(enemy1.x,enemy1.y)
        x=randint(1550,1650)
        enemy1.moveTo(x,715)
        
    if timeblast.collidedWith(enemy2):
        bullet3.moveTo(enemy2.x,enemy2.y)
        x=randint(1620,1700)
        enemy2.moveTo(x,715)

    if timeblast.x>1500:
        timeblast.visible=False
        timeblast.moveTo(wjwalk.x+15,wjwalk.y-30)

    if keys.Pressed[K_LSHIFT]:
        bullet1.setSpeed(1.8,90)
        bullet2.setSpeed(1.8,90)
        bullet3.setSpeed(1.8,90)
        enemy.setSpeed(1,90)
        enemy1.setSpeed(1,90)
        enemy2.setSpeed(1,90)
        powerlevel-=1

    if not keys.Pressed[K_LSHIFT] or powerlevel<0:
        bullet1.setSpeed(5.3,90)
        bullet2.setSpeed(5.3,90)
        bullet3.setSpeed(5.3,90)
        x=randint(1,3)
        enemy.setSpeed(x,90)
        y=randint(2,4)
        enemy1.setSpeed(y,90)
        enemy2.setSpeed(2,90)

    if powerlevel<0:
        if keys.Pressed[K_LALT]:
            timeblast.visible=False

        if keys.Pressed[K_LCTRL]:
            forcefield.visible=False

    if powerlevel<-1:
        powerlevel+=1

    if powerlevel<1:
        powerlevel-=1
    
    if keys.Pressed[K_ESCAPE]:
        unpause.draw()
        game.update(101)
        game.wait(K_TAB)

    if keys.Pressed[K_n]:
        stopgameMusic()

    if keys.Pressed[K_m]:
        playgameMusic()

    game.drawText("Your Health:"+str(wjwalk.health),5,65,font)
    game.drawText("Your Power Level:"+str(powerlevel),5,85,font)
    game.drawText("Your Jump Boost Fuel:"+str(jumpboost),5,105,font)

    #Game Over
    if wjwalk.health<1:
        stopbossMusic()
        death.play()
        game.clearBackground()
        gameover.draw()
        end.draw()
        game.update(151)
        game.wait(K_RETURN)
        game.quit()

    if time>0:
        game.update(101)
        time-=1
        continue

    if time<1:
        game.viewMouse(True)
        moveon.draw()
        enemy.visible=False
        enemy1.visible=False
        enemy2.visible=False

    if moveon.collidedWith(mouse) and mouse.LeftClick:
        game.over=True

    game.update(151)
game.over=False

#Loading Screen 4
loadingMusic()
playloadingMusic()

time=651

game.viewMouse(True)

while not game.over:
    game.processInput()

    blackbackground.draw()
    blackbackground.visible=True
    begin.draw()
    loading.draw()
    loadingsymbol.draw()
    level4.draw()
    tip8.draw()
    begin.visible=False
    loading.visible=True
    loadingsymbol.visible=True

    if time>-1:
        game.update(101)
        time-=1
        continue

    if time<2:
        begin.visible=True
        loading.visible=False
        loadingsymbol.visible=False
    
    if begin.collidedWith(mouse) and mouse.LeftClick:
        stoploadingMusic()
        selection.play()
        game.over=True

    game.update(151)
game.over=False

#Level 4
bossMusic()
playbossMusic()

game.setBackground(labbackground)
labbackground.resizeTo(1480,820)

jumpboost=100
enemyfire=0
enemyfire1=0
enemyfire2=0
forcefieldtime=1500
bosshealth=1000
bosshide=1000
bosshide1=1000
bosshide2=1000
bossfire=250
bossfire1=280
bossfire2=300

enemy.moveTo(1690,715)
enemy1.moveTo(1750,715)
enemy2.moveTo(1880,715)

game.viewMouse(False)

while not game.over:
    game.processInput()

    labbackground.move()
    game.scrollBackground("left",3.5)
    pause.draw()
    wjwalk.move()
    wjjump.move()
    wjjump.moveTo(wjwalk.x,wjwalk.y)
    mute.draw()
    unmute.draw()
    level4.draw()
    bullet.move()
    aim.draw()
    aim.moveTo(mouse.x-53,mouse.y)
    timeblast.move()
    boss.move()
    appear.move()
    bossweapon.move()
    bossweapon1.move()
    bossweapon2.move()
    enemy.visible=False
    enemy1.visible=False
    enemy2.visible=False
    appear.visible=False

    if forcefield.visible:
        forcefield.move()
        forcefield.moveTo(wjwalk.x,wjwalk.y)
        forcefieldtime-=1

    if wjwalk.collidedWith(boss,"rectangle"):
        wjwalk.health-=1000

    if bossfire>249 and not bossfire<1:
         bossweapon.moveTo(boss.x,boss.y)
    
    if bossfire<251:
        bossfire-=1

    if bossfire<1:
        bossfire+=250
        bossweapon.visible=True
        bossangleTo=boss.angleTo(wjwalk)
        bossweapon.setSpeed(7.3,bossangleTo)

    if wjwalk.collidedWith(bossweapon,"circle"):
        wjwalk.health-=20
        bossweapon.visible=False

    if bosshealth<750:
        appear.visible=True
        boss.visible=False
        bossweapon.visible=False
        bosshide-=1

    if bosshide<1:
        appear.visible=False
        boss.visible=True
        bossweapon.visible=True

    if bosshealth<750 and bosshide>1:
        enemy.visible=True
        enemy1.visible=True
        enemy2.visible=True
        
        enemy.move()
        x=randint(1,3)
        enemy.setSpeed(x,90)

        enemy1.move()
        y=randint(2,4)
        enemy1.setSpeed(y,90)

        enemy2.move()
        enemy2.setSpeed(2,90)

        if enemy.isOffScreen("left"):
            x=randint(1500,1600)
            enemy.moveTo(x,715)

        if enemy1.isOffScreen("left"):
            x=randint(1550,1650)
            enemy1.moveTo(x,715)

        if enemy2.isOffScreen("left"):
            x=randint(1620,1700)
            enemy2.moveTo(x,715)

        bullet1.move()
        bullet2.move()
        bullet3.move()

        if enemyfire<271:
            enemyfire+=1

        if enemyfire>270:
            enemyfire-=271
            gun.play()
            bullet1.setSpeed(5.3,90)
            bullet1.visible=True

        if bullet1.collidedWith(wjwalk) or bullet1.collidedWith(wjjump):
            wjwalk.health-=5
            damage.play()
            bullet1.moveTo(enemy.x,enemy.y)
            bullet1.visible=False

        if bullet1.isOffScreen("left"):
            bullet1.moveTo(enemy.x,enemy.y)
            bullet1.visible=False
        
        if enemyfire1<251:
            enemyfire1+=1

        if enemyfire1>250:
            enemyfire1-=251
            gun.play()
            bullet2.setSpeed(5.3,90)
            bullet2.visible=True

        if bullet2.collidedWith(wjwalk) or bullet2.collidedWith(wjjump):
            wjwalk.health-=5
            damage.play()
            bullet2.moveTo(enemy1.x,enemy1.y)
            bullet2.visible=False

        if bullet2.isOffScreen("left"):
            bullet2.moveTo(enemy1.x,enemy1.y)
            bullet2.visible=False

        if enemyfire2<251:
            enemyfire2+=1

        if enemyfire2>250:
            enemyfire2-=251
            gun.play()
            bullet3.setSpeed(5.3,90)
            bullet3.visible=True

        if bullet3.collidedWith(wjwalk) or bullet3.collidedWith(wjjump):
            wjwalk.health-=5
            damage.play()
            bullet3.moveTo(enemy2.x,enemy2.y)
            bullet3.visible=False

        if bullet3.isOffScreen("left"):
            bullet3.moveTo(enemy2.x,enemy2.y)
            bullet3.visible=False

    if bosshealth<500:
        appear.visible=True
        boss.visible=False
        bosshide1-=1

        if bossfire1>279 and not bossfire1<1:
            bossweapon1.moveTo(boss.x,boss.y)
    
        if bossfire1<281:
            bossfire1-=1

        if bossfire1<1:
            bossfire1+=280
            bossweapon1.visible=True
            bossangleTo=boss.angleTo(wjwalk)
            bossweapon1.setSpeed(7.3,bossangleTo)

        if wjwalk.collidedWith(bossweapon1,"circle"):
            wjwalk.health-=20
            bossweapon1.visible=False

        if bossfire2>299 and not bossfire2<1:
            bossweapon2.moveTo(boss.x,boss.y)
    
        if bossfire2<301:
            bossfire2-=1
    
        if bossfire2<1:
            bossfire2+=300
            bossweapon2.visible=True
            bossangleTo=boss.angleTo(wjwalk)
            bossweapon2.setSpeed(7.3,bossangleTo)

        if wjwalk.collidedWith(bossweapon2,"circle"):
            wjwalk.health-=20
            bossweapon2.visible=False

    if bosshide1<1:
        appear.visible=False
        boss.visible=True
        bossweapon.visible=True
        bossweapon1.visible=True
        bossweapon2.visible=True

    if bosshealth<500 and bosshide1>1:
        enemy.visible=True
        enemy1.visible=True
        enemy2.visible=True
        bossweapon.visible=False
        bossweapon1.visible=False
        bossweapon2.visible=False
        
        enemy.move()
        x=randint(1,3)
        enemy.setSpeed(x,90)

        enemy1.move()
        y=randint(2,4)
        enemy1.setSpeed(y,90)

        enemy2.move()
        enemy2.setSpeed(2,90)

        if enemy.isOffScreen("left"):
            x=randint(1500,1600)
            enemy.moveTo(x,715)

        if enemy1.isOffScreen("left"):
            x=randint(1550,1650)
            enemy1.moveTo(x,715)

        if enemy2.isOffScreen("left"):
            x=randint(1620,1700)
            enemy2.moveTo(x,715)

        bullet1.move()
        bullet2.move()
        bullet3.move()

        if enemyfire<271:
            enemyfire+=1

        if enemyfire>270:
            enemyfire-=271
            gun.play()
            bullet1.setSpeed(5.3,90)
            bullet1.visible=True

        if bullet1.collidedWith(wjwalk) or bullet1.collidedWith(wjjump):
            wjwalk.health-=5
            damage.play()
            bullet1.moveTo(enemy.x,enemy.y)
            bullet1.visible=False

        if bullet1.isOffScreen("left"):
            bullet1.moveTo(enemy.x,enemy.y)
            bullet1.visible=False
        
        if enemyfire1<251:
            enemyfire1+=1

        if enemyfire1>250:
            enemyfire1-=251
            gun.play()
            bullet2.setSpeed(5.3,90)
            bullet2.visible=True

        if bullet2.collidedWith(wjwalk) or bullet2.collidedWith(wjjump):
            wjwalk.health-=5
            damage.play()
            bullet2.moveTo(enemy1.x,enemy1.y)
            bullet2.visible=False

        if bullet2.isOffScreen("left"):
            bullet2.moveTo(enemy1.x,enemy1.y)
            bullet2.visible=False

        if enemyfire2<251:
            enemyfire2+=1

        if enemyfire2>250:
            enemyfire2-=251
            gun.play()
            bullet3.setSpeed(5.3,90)
            bullet3.visible=True

        if bullet3.collidedWith(wjwalk) or bullet3.collidedWith(wjjump):
            wjwalk.health-=5
            damage.play()
            bullet3.moveTo(enemy2.x,enemy2.y)
            bullet3.visible=False

        if bullet3.isOffScreen("left"):
            bullet3.moveTo(enemy2.x,enemy2.y)
            bullet3.visible=False

    if bosshealth<250:
        enemy.visible=True
        enemy1.visible=True
        enemy2.visible=True
        
        enemy.move()
        x=randint(1,3)
        enemy.setSpeed(x,90)

        enemy1.move()
        y=randint(2,4)
        enemy1.setSpeed(y,90)

        enemy2.move()
        enemy2.setSpeed(2,90)

        if enemy.isOffScreen("left"):
            x=randint(1500,1600)
            enemy.moveTo(x,715)

        if enemy1.isOffScreen("left"):
            x=randint(1550,1650)
            enemy1.moveTo(x,715)

        if enemy2.isOffScreen("left"):
            x=randint(1620,1700)
            enemy2.moveTo(x,715)

        bullet1.move()
        bullet2.move()
        bullet3.move()

        if enemyfire<271:
            enemyfire+=1

        if enemyfire>270:
            enemyfire-=271
            gun.play()
            bullet1.setSpeed(5.3,90)
            bullet1.visible=True

        if bullet1.collidedWith(wjwalk) or bullet1.collidedWith(wjjump):
            wjwalk.health-=5
            damage.play()
            bullet1.moveTo(enemy.x,enemy.y)
            bullet1.visible=False

        if bullet1.isOffScreen("left"):
            bullet1.moveTo(enemy.x,enemy.y)
            bullet1.visible=False
        
        if enemyfire1<251:
            enemyfire1+=1

        if enemyfire1>250:
            enemyfire1-=251
            gun.play()
            bullet2.setSpeed(5.3,90)
            bullet2.visible=True

        if bullet2.collidedWith(wjwalk) or bullet2.collidedWith(wjjump):
            wjwalk.health-=5
            damage.play()
            bullet2.moveTo(enemy1.x,enemy1.y)
            bullet2.visible=False

        if bullet2.isOffScreen("left"):
            bullet2.moveTo(enemy1.x,enemy1.y)
            bullet2.visible=False

        if enemyfire2<251:
            enemyfire2+=1

        if enemyfire2>250:
            enemyfire2-=251
            gun.play()
            bullet3.setSpeed(5.3,90)
            bullet3.visible=True

        if bullet3.collidedWith(wjwalk) or bullet3.collidedWith(wjjump):
            wjwalk.health-=5
            damage.play()
            bullet3.moveTo(enemy2.x,enemy2.y)
            bullet3.visible=False

        if bullet3.isOffScreen("left"):
            bullet3.moveTo(enemy2.x,enemy2.y)
            bullet3.visible=False
    
    if bosshealth<250:
        appear.visible=True
        boss.visible=False
        bossweapon.visible=False
        bossweapon1.visible=False
        bossweapon2.visible=False
        bosshide2-=1

    if bosshide2<1:
        appear.visible=False
        boss.visible=True
        bossweapon.visible=True
        bossweapon1.visible=True
        bossweapon2.visible=True

    #Game Controls
    if wjwalk.y<700 or wjjump.y<700:
        wjwalk.y+=4
        wjjump.y+=4
    
    if keys.Pressed[K_d]:
        wjwalk.x+=3.77
    elif keys.Pressed[K_d]:
        wjwalk.x-=3.77

    if not keys.Pressed[K_d]:
        wjwalk.x-=1

    if keys.Pressed[K_a]:
        wjwalk.x-=3.77
    
    if keys.Pressed[K_w]:
        wjwalk.visible=False
        wjjump.visible=True
        wjwalk.y-=5.7
        wjjump.y-=5.7
        jumpboost-=1
        
    if jumpboost<0:
        wjwalk.y+=4
        wjjump.y+=4
        jumpboost+=1

    if jumpboost<100 and not keys.Pressed[K_w]:
        jumpboost+=1
        
    if jumpboost>100:
        jumpboost-=1
        jumpboost+=1
        
    if not keys.Pressed[K_w]:
        wjwalk.visible=True
        wjjump.visible=False

    if keys.Pressed[K_s]:
        wjwalk.y+=5.7
        wjjump.y+=5.7

    if wjwalk.y>725:
        wjwalk.y-=5.7

    if keys.Pressed[K_SPACE]:
        bullet.moveTo(wjwalk.x+15,wjwalk.y-30)
        angleToCrosshair = bullet.angleTo(aim)
        bullet.setSpeed(8.4,angleToCrosshair)
        bullet.visible=True
        gun.play()

    if bullet.collidedWith(boss,"rectangle"):
        bullet.visible=False
        bosshealth-=20

    if bullet.collidedWith(enemy,"rectangle"):
        bullet.visible=False
        bullet1.moveTo(enemy.x,enemy.y)
        x=randint(1500,1600)
        enemy.moveTo(x,715)

    if bullet.collidedWith(enemy1,"rectangle"):
        bullet.visible=False
        bullet2.moveTo(enemy1.x,enemy1.y)
        x=randint(1550,1650)
        enemy1.moveTo(x,715)
        
    if bullet.collidedWith(enemy2,"rectangle"):
        bullet.visible=False
        bullet3.moveTo(enemy2.x,enemy2.y)
        x=randint(1620,1700)
        enemy2.moveTo(x,715)

    if bullet.x>1450:
        bullet.visible=False
        bullet.moveTo(wjwalk.x+15,wjwalk.y-30)

    if keys.Pressed[K_LCTRL]:
        forcefield.visible=not forcefield.visible
        powerlevel-=30

    if forcefieldtime<0:
        forcefield.visible=False

    if bullet1.collidedWith(forcefield,"circle") or bullet2.collidedWith(forcefield,"circle") or bullet3.collidedWith(forcefield,"circle") or bossweapon.collidedWith(forcefield,"circle") or bossweapon1.collidedWith(forcefield,"circle") or bossweapon2.collidedWith(forcefield,"circle"):
        bullet1.visible=False
        bullet2.visible=False
        bullet3.visible=False
        bossweapon.visible=False
        bossweapon1.visible=False
        bossweapon2.visible=False

    if keys.Pressed[K_LALT]:
        timeblast.moveTo(wjwalk.x+15,wjwalk.y-30)
        angleToCrosshair=timeblast.angleTo(aim)
        timeblast.setSpeed(7.5,angleToCrosshair)
        timeblast.visible=True
        timeblastsound.play()
        powerlevel-=10

    if timeblast.collidedWith(boss):
        bosshealth-=50
        timeblast.visible=False

    if timeblast.collidedWith(enemy):
        bullet1.moveTo(enemy.x,enemy.y)
        x=randint(1500,1600)
        enemy.moveTo(x,715)

    if timeblast.collidedWith(enemy1):
        bullet2.moveTo(enemy1.x,enemy1.y)
        x=randint(1550,1650)
        enemy1.moveTo(x,715)
        
    if timeblast.collidedWith(enemy2):
        bullet3.moveTo(enemy2.x,enemy2.y)
        x=randint(1620,1700)
        enemy2.moveTo(x,715)

    if timeblast.x>1500:
        timeblast.visible=False
        timeblast.moveTo(wjwalk.x+15,wjwalk.y-30)

    if keys.Pressed[K_LSHIFT]:
        bullet1.setSpeed(1.8,90)
        bullet2.setSpeed(1.8,90)
        bullet3.setSpeed(1.8,90)
        enemy.setSpeed(1,90)
        enemy1.setSpeed(1,90)
        enemy2.setSpeed(1,90)
        powerlevel-=1

    if not keys.Pressed[K_LSHIFT] or powerlevel<0:
        bullet1.setSpeed(5.3,90)
        bullet2.setSpeed(5.3,90)
        bullet3.setSpeed(5.3,90)
        x=randint(1,3)
        enemy.setSpeed(x,90)
        y=randint(2,4)
        enemy1.setSpeed(y,90)
        enemy2.setSpeed(2,90)

    if powerlevel<0:
        if keys.Pressed[K_LALT]:
            timeblast.visible=False

        if keys.Pressed[K_LCTRL]:
            forcefield.visible=False

    if powerlevel<-1:
        powerlevel+=1

    if powerlevel<1:
        powerlevel-=1
    
    if keys.Pressed[K_ESCAPE]:
        unpause.draw()
        game.update(101)
        game.wait(K_TAB)

    if keys.Pressed[K_n]:
        stopgameMusic()

    if keys.Pressed[K_m]:
        playgameMusic()

    game.drawText("Your Health:"+str(wjwalk.health),5,65,font)
    game.drawText("Your Power Level:"+str(powerlevel),5,85,font)
    game.drawText("Your Jump Boost Fuel:"+str(jumpboost),5,105,font)
    game.drawText("Boss Health:"+str(bosshealth),1325,95,font1)

    #Game Over
    if wjwalk.health<1:
        stopbossMusic()
        death.play()
        game.clearBackground()
        gameover.draw()
        end.draw()
        game.update(151)
        game.wait(K_RETURN)
        game.quit()

    if bosshealth<1:
        game.over=True
        
    game.update(151)
game.over=False

#Game Win
while not game.over:
    stopbossMusic()
    blackbackground.draw()
    victoryscreen.draw()
    victoryscreen1.draw()
    victoryquit.draw()
    game.update(151)
    game.wait(K_RETURN)
    game.quit()
    
    game.update(151)
game.over=False

game.quit()
