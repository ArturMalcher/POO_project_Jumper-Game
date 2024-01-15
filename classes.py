from typing import Tuple, Dict

# TUDO QUE APARECE NA TELA
class Screen:
    
    # Construtor
    def __init__(self, name: str, width: int, height: int, background: str):
        self.name = name
        self.width = width
        self.height = height
        self.background = background
        self.dic_sprites: Dict[int, Sprite] = {}
        array: Dict[int, Dict[int, str]] = {}

        # Array de dicionário com numeração e caracteres
        for y in range(1, self.height+1):
            array[y] = {}
            for x in range(1, self.width+1):
                array[y][x] = self.background

        # Array de lista default 
        array_default = []
        for y in array.keys():
            array_default.append([array[y][x] for x in array[y].keys()])

        self.array = array
        self.array_default = array_default

    def change_array(self, array):

        array_default = []
        for y in array.keys():
            array_default.append([array[y][x] for x in array[y].keys()])

        self.array = array
        self.array_default = array_default
        
    # Mostrar o objeto com base na matriz criada
    def display(self):
        array = list(map(list, self.array_default))
        
        # Desenhando os sprites adicionados ao display
        for sprite_id in self.dic_sprites:
            sprite = Sprite.dict_id[sprite_id]
            sprite_w = sprite.width
            sprite_h = sprite.height
            x = sprite.position[0]
            y = self.height - sprite.position[1]
            #print(f'{sprite.name}: x:{x}, y:{y}, w:{sprite_w}, h:{sprite_h}')            

            # desenhando coluna por coluna, de linha em linha
            for char_y, sprite_y in enumerate(range(y, y + sprite_h)):
                for char_x, sprite_x in enumerate(range(x, x + sprite_w)):
                    #print(f"{sprite.name}: {char_x}, {char_y}")
                    array[sprite_y][sprite_x -1] = sprite.array[char_y +1][char_x +1]

        # Imprimindo o Array atualizado
        for y in array:
            # Caso não tenha nada dentro de um px, então mostra o Background
            for x in y:
                    print(x, end='')
            print()

         # Imprimindo o Array pelo dicionário
        #for y in array:
            # Caso não tenha nada dentro de um px, então mostra o Background

        #    for x in array[y]:
        #        if array[y][x] == None:
        #            print(bg, end='')
        #         else:
        #            print(array[y][x], end='')
        #    print()

    # Adicionar um sprite ao array do Screen
    def add_sprite(self, sprite):
        self.dic_sprites[sprite.id] = sprite
        sprite.set_screen(self)
        

    def del_sprite(self, id):
        del self.dic_sprites[id]

# Sprite que herda a classe Screen
class Sprite(Screen):
    dict_id: dict = {}

    def __init__(self, name:str, width: int, height: int, position: Tuple[int, int], background: str):
        super().__init__(name, width, height, background)
        self.background = background
        self.position = position

        # Definindo Id do sprite
        id = 1
        for i in Sprite.dict_id:
            id +=1
        self.id = id
        Sprite.dict_id[id] = self
    
    def set_screen(self, screen):
        self.screen = screen
    
    # Método de movimentação de sprite
    def move(self, direction, steps):
        pos = self.position

        if direction == "up":
            if self.position[1] + steps < self.screen.height:
                self.position = (pos[0], pos[1] + steps)
                print(self.height + self.position[1] + steps + 1)
                print(self.screen.height)

        if direction == "down":
            if self.position[1] - steps > 0:
                self.position = (pos[0], pos[1] - steps)
                
        if direction == "left":
            self.position = (pos[0] - steps, pos[1] )
            
        if direction == "right":
            self.position = (pos[0] + steps, pos[1])


# Teste
# Criação de objetos
screen1 = Screen("screen1", 140, 10, ".")
ground = Sprite("ground", 140, 1, (1, 1), "_")
player = Sprite("player", 3, 2, (2, 2), " | ")
enemy1 = Sprite("enemy1", 1, 2, (138, 2), "##")
enemy2 = Sprite("enemy2", 1, 2, (138, 2), "[]")
enemy3 = Sprite("enemy3", 1, 2, (138, 2), "#")
enemy4 = Sprite("enemy4", 1, 2, (138, 2), "#")
enemy5 = Sprite("enemy5", 1, 2, (138, 2), "#")
enemy6 = Sprite("enemy6", 1, 2, (138, 2), "#")

# Adicionando objetos à screen1
screen1.add_sprite(ground) 
screen1.add_sprite(player) 

# Criando um array para corpo
array = {1:{1:"%", 2:"%", 3:">"},
         2:{1:"!", 2:"!", 3:" "}}

# Mudando o corpo de player para array
player.change_array(array)

screen1.display()

