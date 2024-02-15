import pygame

NEIGHBOR_OFFSETS = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (0, 0), (-1, 1), (0, 1), (1, 1)]
PHYSICS_TILES = {'grass', 'stone'} # *dicinário tem uma busca mais efetiva que listas

class Tilemap:
    def __init__(self, game, tile_size=16):
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}
        self.offgrid_tiles = []

        for i in range(10):
            self.tilemap[str(3 + i) + ';10'] = {'type': 'grass', 'variant': 1, 'pos': (3 + i, 10)}
            # "cria" a definção da posição de uma fileira de terra na vertical, pq o y é fixo em 10
            self.tilemap['10;' + str(5 + i)] = {'type': 'stone', 'variant': 1, 'pos': (10, 5 + i)}
            # "cria" a definção da posição de uma fileira de pedra na horizontal pq o x é fixo em 10
    
    def tiles_around(self, pos):
        tiles = []
        tile_loc = (int(pos[0] // self.tile_size), int(pos[1] // self.tile_size))
        # O que estamos fazendo aqui: transformando uma posição em pixel para uma posição no grid
        # int(x // y) -> pega a parte inteira do divisão
        for offset in NEIGHBOR_OFFSETS:
            check_loc = str(tile_loc[0] + offset[0]) + ';' + str(tile_loc[1] + offset[1])
            if check_loc in self.tilemap:
                tiles.append(self.tilemap[check_loc])
        return tiles 
        # Aqui vamos pegar as posições próximas ao jogador e verificar se existe algum tile perto dele (NEIGHBOR_OFFSETS)
        # serve para isso, coordenada próximas
        # Retornamos todos os tiles próximos a posição do jogador
    
    def physics_rects_around(self, pos):
        rects = []
        for tile in self.tiles_around(pos):
            if tile['type'] in PHYSICS_TILES:
                rects.append(pygame.Rect(tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size, self.tile_size, self.tile_size))
        return rects
        # Criamos e retornamos os retangulos para os tiles que estão próximo ao elemento para que a colisão aconteça
    
    def render(self, surf, offset=(0,0)):
        for tile in self.offgrid_tiles:
            surf.blit(self.game.assets[tile['type']][tile['variant']], (tile['pos'][0] - offset[0], tile['pos'][1] - offset[1]))
        
        for loc in self.tilemap:
            tile = self.tilemap[loc]
            surf.blit(self.game.assets[tile['type']][tile['variant']], (tile['pos'][0] * self.tile_size - offset[0], tile['pos'][1] * self.tile_size - offset[1]))
            # self.game.assets[tile['type']][tile['variant']] -> o asset em questão é uma lista
            # então passamos além do tipo do asset qual asset da lista queremos
            # (tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size) -> precisamos multiplicar a posição
            # pelo tamanho do tile para "caber"
            # lembrando superfice.blit(imagem, posicao) 
        