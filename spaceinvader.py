import pgzrun,random,pyautogui

print(pyautogui.size())
WIDTH,HEIGHT=pyautogui.size()

player=Actor('rocket (player)')
player.pos=WIDTH/2,HEIGHT-200
enemies=[]
bullets=[]
def draw():
    screen.blit('bg.jpg',(0,0))
    player.draw()
    for i in enemies:
        i.draw()
    for i in bullets:
        i.draw()

def update():
    if keyboard.left and player.x >50:
        player.x-=10

    if keyboard.right and player.x < WIDTH-50:                                                                                                                  
        player.x+=10
    for i in enemies:
        i.y += 10
        if i.y > HEIGHT:
            enemies.remove(i)
    for i in bullets:
        i.y-=10
        if i.y < 0:
            bullets.remove(i)

def create_enemies():
    enemy=Actor('player.png')
    enemy.pos=random.randint(50,WIDTH-50),-50
    enemies.append(enemy)


def on_key_down(key):
    if key == keys.SPACE and len(bullets) < 6:
        bullet=Actor("playerbullet.png")
        bullet.pos = player.x,player.y-100
        bullets.append(bullet)
    



clock.schedule_interval(create_enemies,1)
pgzrun.go()