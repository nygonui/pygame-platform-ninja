import pygame

class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.velocity = [0, 0]
        self.collisions = {'up': False, 'down': False, 'left': False, 'right': False}
        
    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        # para haver colisão precisamos do pygame.Rect, 
        # que gera um retangulo na posição do elemento e do tamanho do elemento
    
    def update(self, tilemap, movement=(0, 0)):
        self.collisions = {'up': False, 'down': False, 'left': False, 'right': False}

        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])
        
        self.pos[0] += frame_movement[0]
        entity_rect = self.rect() # Criando o retângulo da nossa entidade
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[0] > 0:
                    entity_rect.right = rect.left
                    self.collisions['right'] = True
                if frame_movement[0] < 0:
                    entity_rect.left = rect.right
                    self.collisions['left'] = True
                self.pos[0] = entity_rect.x
        # Passamos a posição da entidade para pegar todos os tiles que estão próximos a entidade
        # Ela retorna o retângulo deles
        # E o que fazemos nos IFs é parar o movimento da entidade igualando a posição do tile e da entidade
        # Então se andarmos para direita (movimento positivo) a posição direita da entidade será 
        # igual a posição esquerda do tile, ou seja irá colidir ... mesma coisa para os outros lados
        # No final atualizamos a posição real da entidade para a posição do retângulo que a "cobre"
        
        self.pos[1] += frame_movement[1]
        entity_rect = self.rect() # Criando o retângulo da nossa entidade
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[1] > 0:
                    entity_rect.bottom = rect.top
                    self.collisions['down'] = True
                if frame_movement[1] < 0:
                    entity_rect.top = rect.bottom
                    self.collisions['top'] = True
                self.pos[1] = entity_rect.y
        
        self.velocity[1] = min(5, self.velocity[1] + 0.1)
        # a função min faz com que seja atribuído o menor valor entre os parametros à variável self.velocity
        # e como por enquanto estamos falando da aceleração da gravidade vamos mexer no eixo y 
        if self.collisions['up'] or self.collisions['down']:
            self.velocity[1] = 0
        
        
    def render(self, surf):
        surf.blit(self.game.assets['player'], self.pos)
        