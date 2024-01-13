from typing import Tuple, List, Dict

# TUDO QUE APARECE NA TELA
class Screen:
    
    # Construtor
    def __init__(self, width: int, height: int, background: str):
        self.width = width
        self.height = height
        self.background = background
        self.dic_sprites: Dict[int, Sprite] = {}
    
    # Mostrar o objeto com base na matriz criada
        
    def display(self):
        bg = self.background

        # Redesenhando os sprites adicionados ao display
        array = {}

        for y in range(1, self.height+1):
            array[y] = {}
            for x in range(1, self.width+1):
                array[y][x] = self.background

        for sprite_id in self.dic_sprites:
            sprite = Sprite.dict_id[sprite_id]
            width = sprite.width
            height = sprite.height
            x = sprite.position[0]
            y = self.height - sprite.position[1]

            # Refazendo a matriz do objeto com base no sprite adicionado

            for py in range(y, y + height):
                for px in range(x, x + width):
                    array[py][px] = sprite.material
        
        # Imprimindo o Array atualizado
        for y in array:
            # Caso não tenha nada dentro de um px, então mostra o Background
            for x in array[y]:
                if array[y][x] == None:
                    print(bg, end='')
                else:
                    print(array[y][x], end='')
            print()
            

    
    # Adicionar um sprite ao array do Screen
    def add_sprite(self, sprite):
        self.dic_sprites[sprite.id] = sprite

    def del_sprite(self, id):
        del self.dic_sprites[id]

# Sprite que herda a classe Screen
class Sprite(Screen):
    dict_id: dict = {}

    def __init__(self, screen: Screen, width: int, height: int, position: Tuple[int, int], material: str):
        super().__init__(width, height, material)
        self.material = material
        self.screen = screen
        self.body = material
        self.position = position

        # Definindo Id do sprite
        id = 1
        for i in Sprite.dict_id:
            id +=1
        self.id = id
        Sprite.dict_id[id] = self
    
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