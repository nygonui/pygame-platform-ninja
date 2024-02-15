import sys

import pygame 

from scripts.entities import PhysicsEntity
from scripts.utils import load_image, load_images
from scripts.tilemap import Tilemap
from scripts.clouds import Clouds

class Game:
    def __init__(self):
        pygame.init()
        
        pygame.display.set_caption('ninja game')
        self.screen = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface((320, 240))

        self.clock = pygame.time.Clock()

        self.movement = [False, False]
        
        self.assets = {
            'decor': load_images('tiles/decor'),
            'grass': load_images('tiles/grass'),
            'large_decor': load_images('tiles/large_decor'),
            'stone': load_images('tiles/stone'),
            'player': load_image('entities/player.png'),
            'background': load_image('background.png'),
            'clouds': load_images('clouds')
        }
        
        self.clouds = Clouds(self.assets['clouds'], count=16)
        
        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))
        
        self.tilemap = Tilemap(self, tile_size=16)
        
        self.scroll = [0, 0]
        

    def run(self):
        while True:
            self.display.blit(self.assets['background'], (0, 0))
            # essa linha serve meio que para limpar a tela, pois até então a imagem da nuvem que estamos 
            # colocando na tela, está sendo desenhada em cada lugar ao decorrer do seu movemento em cada frame
            
            
            self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 30
            self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1]) / 30
            # se passacemos o self.scroll direto o jogador ficaria no canto esquerdo superior da tela 
            # o que tentamos fazer aqui é encontrar o meio de tela e ver quanto que falta da posição atual da câmera
            # e a divisão por 30 é para que quando a câmera vá rápido quando o player estiver longe do centro
            # e diminui gradativamente quando o player estiver ficando centralizado
            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))
            # isso é para passarmos um valor inteiro como posição da câmera, pois a posição do player é um float
            # quando passamos a posição da câmera como um float também há um bug de pixel quando o player está para 
            # ser centralizado
            
            self.clouds.update()
            self.clouds.render(self.display, offset=render_scroll)
            
            self.tilemap.render(self.display, offset=render_scroll) 
            
            self.player.update(self.tilemap ,(self.movement[1] - self.movement[0], 0))
            self.player.render(self.display, offset=render_scroll)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.movement[1] = True
                    if event.key == pygame.K_UP:
                        self.player.velocity[1] = -3    
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.movement[1] = False                     
                
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)

Game().run()
