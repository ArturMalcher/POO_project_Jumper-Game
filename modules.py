import os
import threading
import msvcrt
import classes
import random

timer = 0.02
running = True
frame = 0
jump = False
falling = False
cont = 0


# Limpar display
def clear():
        return os.system("cls" if os.name in ("nt", "dos") else "clear")

# Frame a frame

def controls(sprite):
    global running
    global jump
    # Controles
    resp = msvcrt.getch().decode('utf-8')
    if resp:
        if resp[0] == "a":
            sprite.move('left', 2)
        
        elif resp[0] == "d":
            sprite.move('right', 2)
        
        elif resp[0] == "q":
            running = False
    
        elif resp[0] == "w":
            if jump == False and falling == False:
                jump = True
    
        elif resp[0] == "s":
            sprite.move('down', 1)

# AQUI É ONDE RODA TUDO
def run(screen, sprite, enemy1, enemy2, enemy3):
    global frame
    global running
    global jump
    global falling
    global cont
    
    if sprite.position in [enemy1.position, enemy2.position, enemy3.position]:
        running = False
        
    if enemy1.id in screen.dic_sprites:
        enemy1.move('left', 2)
        if enemy1.position[0] < 1:
            enemy1.position = (138, enemy1.position[1])
            screen.del_sprite(enemy1.id)   
    else:
        if random.randint(1, 100) == 1:
            screen.add_sprite(enemy1)
    
    if enemy2.id in screen.dic_sprites:
        enemy2.move('left', 2)
        if enemy2.position[0] < 2:
            enemy2.position = (138, enemy2.position[1])
            screen.del_sprite(enemy2.id)   
    else:
        if random.randint(1, 100) == 100:
            screen.add_sprite(enemy2)
    
    if enemy3.id in screen.dic_sprites:
        enemy3.move('left', 2)
        if enemy3.position[0] < 2:
            enemy3.position = (138, enemy3.position[1])
            screen.del_sprite(enemy3.id)   
    else:
        if random.randint(1, 100) == 20:
            screen.add_sprite(enemy3)

    # Em caso de estar pulando
    if jump:
        sprite.move('up', 2)
        if sprite.position[1] > 6:
            jump = False
            falling = True
    
    # Caindo
    elif falling:
        sprite.move('down', 2)
        if sprite.position[1] < 3:
            falling = False
    
    controls(sprite)

    

# Esperar resposta
def wait(funct, screen, sprite, enemy1, enemy2, enemy3):
        global thread_ativa
        thread_input = threading.Thread(target=funct, args=(screen, sprite, enemy1, enemy2, enemy3))
        thread_input.start()
        thread_input.join(timeout=timer)

        if not thread_input.is_alive():
            funct(screen, sprite, enemy1, enemy2, enemy3)

