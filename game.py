import sys

import pygame 

class Game:
    def __init__(self):
        pygame.init()
        
        pygame.display.set_caption('ninja game')
        self.screen = pygame.display.set_mode((640, 480))

        self.clock = pygame.time.Clock()
        
        self.img = pygame.image.load('data/images/clouds/cloud_1.png')
        self.img.set_colorkey((0, 0, 0)) # transforma a cor(RGB) que passamos em transparente
        
        self.img_pos = [160, 260] # [x, y]
        self.movement = [[False, False],[False, False]] # [x, y]
        

    def run(self):
        while True:
            self.screen.fill((14, 219, 248))
            # essa linha serve meio que para limpar a tela, pois até então a imagem da nuvem que estamos 
            # colocando na tela, está sendo desenhada em cada lugar ao decorrer do seu movemento em cada frame
            
            self.img_pos[1] += (self.movement[1][1] - self.movement[1][0]) * 5
            self.img_pos[0] += (self.movement[0][1] - self.movement[0][0]) * 5
            # a linha anterior vem antes da seguinte pq precisamos alterar a posição antes de desenhar
            # a imagem na tela, também o truque na linha de código anterior é que se o gamer clicar nas 
            # nas duas teclas ao mesmo tempo o resultado da soma sera 0 e a imagem não irá se deslocar
            # ps: python consegue converter implicitamente booleans em integers
            self.screen.blit(self.img, self.img_pos)
            # adiciona a imagem (primeiro argumento) na tela na posição passada no segundo argumento
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.movement[1][0] = True
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.movement[1][1] = True
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.movement[0][0] = True
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.movement[0][1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.movement[1][0] = False
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.movement[1][1] = False
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.movement[0][0] = False
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.movement[0][1] = False                      
                
            pygame.display.update()
            self.clock.tick(60)

Game().run()
