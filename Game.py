import modules
import classes
import time

# Criando uma Tela
screen1 = classes.Screen("screen1", 140, 10, " ")

# Criando Sprites
ground = classes.Sprite("ground", 140, 1, (1, 1), "_")
player = classes.Sprite("player", 3, 2, (2, 2), "$")

# Desenhando sprite
player_corpo = {1:{1:"%", 2:"%", 3:">"},
                2:{1:"!", 2:"!", 3:" "}}

# Mudando o corpo de player para array
player.change_array(player_corpo)

# Criando inimigos
enemy1 = classes.Sprite("enemy1", 1, 2, (138, 2), "#")
enemy2 = classes.Sprite("enemy2", 2, 1, (120, 5), "=")
enemy3 = classes.Sprite("enemy3", 1, 2, (138, 2), "#")
enemy4 = classes.Sprite("enemy4", 1, 2, (138, 2), "#")
enemy5 = classes.Sprite("enemy5", 1, 2, (138, 2), "#")
enemy6 = classes.Sprite("enemy6", 1, 2, (138, 2), "#")

# Adicionando Sprites na tela
screen1.add_sprite(ground) 
screen1.add_sprite(player)
score = 0
timer = 0.03

while modules.running:
    
    # Esperar resposta
    time.sleep(timer)
    
    # Limpar display
    modules.run(screen1, player)
    modules.clear()
    score += 1
    
    screen1.display()
    print("score:", score)
    print("dic_sprites:", screen1.dic_sprites)
    print("Pressione 'q' para sair")
    

modules.clear()
gameover = classes.Sprite("gameover", 1, 1, (60, 6), "  G A M E  O V E R  ")
score_obj = classes.Sprite("score", 1, 1, (60, 5), f"  S C O R E: {score}  ")
screen1.add_sprite(score_obj)
screen1.add_sprite(gameover)
screen1.display()