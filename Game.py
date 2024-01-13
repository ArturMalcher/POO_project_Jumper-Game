import modules
import classes

# Criando uma Tela
screen1 = classes.Screen(140, 15, " ")


# Criando Sprites
ground = classes.Sprite(screen1, 140, 1, (1, 1), "_")
player = classes.Sprite(screen1, 2, 2, (2, 2), " | ")
enemy1 = classes.Sprite(screen1, 1, 2, (138, 2), "##")
enemy2 = classes.Sprite(screen1, 1, 2, (100, 2), " ! ")
enemy3 = classes.Sprite(screen1, 1, 2, (54, 2), "#")

# Adicionando Sprites na tela
screen1.add_sprite(ground) 
screen1.add_sprite(player)
screen1.add_sprite(enemy1)
screen1.add_sprite(enemy2)
screen1.add_sprite(enemy3)

score = 0
frame = 0
while modules.running:
    
    modules.wait(modules.run, screen1, player, enemy1, enemy2, enemy3)
    # Esperar resposta

    # Limpar display
    modules.clear()
    score += 1
    
    screen1.display()
    print("score:", score)
    print("dic_sprites:", screen1.dic_sprites)
    print("Pressione 'q' para sair")
    

modules.clear()
screen1 = classes.Screen(140, 15, "/")
gameover = classes.Sprite(screen1, 1, 1, (60, 6), "  G A M E  O V E R  ")
score_obj = classes.Sprite(screen1, 1, 1, (60, 5), f"  S C O R E: {score}  ")
screen1.add_sprite(score_obj)
screen1.add_sprite(gameover)
screen1.display()

