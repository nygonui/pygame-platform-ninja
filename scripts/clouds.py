import random

class Cloud:
    def __init__(self, pos, img, speed, deth):
        self.pos = list(pos)
        self.img = img
        self.speed = speed
        self.deth = deth
    
    def update(self):
        self.pos[0] += self.speed
        
    def render(self, surf, offset=(0, 0)):
        render_pos = (self.pos[0] - offset[0] * self.deth, self.pos[1] - offset[1] * self.deth)
        # estamos multiplicando o offset pelo deth para dar um efeito, deth seria a profundidade
        # então as nuvens em diferentes profundidades vão se mover diferente 
        surf.blit(self.img, (render_pos[0] % (surf.get_width() + self.img.get_width()) - self.img.get_width(), render_pos[1] % (surf.get_height() + self.img.get_height()) - self.img.get_height()))
        # lembrando que temos um número limitado de nuvens, fazemos com que após que elas atravessem por completo o eixo 
        # x ou y elas voltem para o início, se elas estão indo da esquerda para direita, quando elas passarem por completo
        # no canto direito da tela, elas vão surgir no canto esquerdo da tela
        # se não fizecemos as operações matemáticas para passar a posição das nuves elas desapareriam e apareceriam assim
        # que encostassem na borda da tela
        # ** EXPLICAR AS OPERAÇÕES MATEMÁTICAS QUE ACONTECEM NESSE BLIT **
        
class Clouds:
    def __init__(self, cloud_images, count=16):
        self.clouds = []
        
        for i in range(count):
            pos = (random.random() * 99999, random.random() * 99999)
            img = random.choice(cloud_images)
            speed = random.random() * 0.05 + 0.05
            deth = random.random() * 0.6 + 0.2
            self.clouds.append(Cloud(pos, img, speed, deth))
        
        self.clouds.sort(key=lambda x: x.deth)
        # ordenando a lista de nuvens usando a profundidade delas como parâmetro para ordenação
        # fazendo nos ajuda a definir quem será renderizado primeiro
    
    def update(self):
        for cloud in self.clouds:
            cloud.update()
        
    def render(self, surf, offset=(0, 0)):
        for cloud in self.clouds:
            cloud.render(surf, offset=offset)    
    
        