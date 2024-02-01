import os
import msvcrt
import classes
import random
import threading

running = True
jump = False
falling = False
cont = 0
frame = 0

# Limpar display
def clear():
    return os.system("cls" if os.name in ("nt", "dos") else "clear")

# Função auxiliar para lidar com input em uma thread separada
def _controls(sprite):
    global running
    global jump

    while True:
        resp = msvcrt.getch().decode('utf-8')
        if resp:
            if resp[0] == "a":
                sprite.move('left', 2)
            elif resp[0] == "d":
                sprite.move('right', 2)
            elif resp[0] == "w":
                if jump == False and falling == False:
                    jump = True
            elif resp[0] == "q":
                running = False

# Função de controle principal
def controls(sprite):
    global running
    global jump

    # Cria uma thread para lidar com input
    thread = threading.Thread(target=_controls, args=(sprite,))
    thread.daemon = True 
    thread.start()

# Função principal do jogo
def run(screen, sprite):
    global frame
    global running
    global jump
    global falling
    global cont

    # Chama a função de controle para lidar com input
    controls(sprite)

    for sprite_obj in classes.Sprite.dict_id.values():
        
        if "enemy" in sprite_obj.name:
            if sprite_obj in screen.dic_sprites.copy().values():
                sprite_obj.move('left', 2)
                if sprite_obj.position[0] < 1:
                    sprite_obj.position = (138, sprite_obj.position[1])
                    screen.del_sprite(sprite_obj.id)  
                
                if sprite.position == sprite_obj.position:
                    running = False
            else:
                if random.randint(1, 100) == 1:
                    screen.add_sprite(sprite_obj)
    
    # Em caso de estar pulando
    if jump:
        sprite.move('up', 1)
        if sprite.position[1] > 6:
            jump = False
            falling = True
    
    # Em caso de estar caindo
    elif falling:   
        sprite.move('down', 1)
        if sprite.position[1] < 3:
            falling = False

            

