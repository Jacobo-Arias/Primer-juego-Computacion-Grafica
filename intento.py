import pygame
#Dibuja triangulo y lo escala con el teclado
ANCHO=1024
ALTO=900
VERDE=[0,255,0]
AZUL=[0,0,255]
ROJO=[255,0,0]
NEGRO=[0,0,0]
BLANCO=[255,255,255]

class Jugador (pygame.sprite.Sprite):
    def __init__(self,filas,accion = 0):
        pygame.sprite.Sprite.__init__(self)
        self.filas = filas
        self.accion = accion
        self.i = 1
        self.f = self.filas[self.accion]
        self.image = self.f[self.i]
        self.rect = self.image.get_rect()

    def update(self):
        self.f = self.filas[self.accion]
        self.image = self.f[self.i]
        self.i += 1
        if self.i >= len(self.f):
            self.i = 0

class barril(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([40,40])
        self.image.fill(VERDE)
        self.rect=self.image.get_rect()
        self.rect.x=180
        self.rect.y=230


if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO, ALTO])  #Crea la ventana
    fondo=pygame.image.load('ken.png')
    info=fondo.get_rect()
    an_img=info[2]
    al_img=info[3]

    al_corte=al_img/10
    an_corte=an_img/7
    x,y=1,0
    vx,vy = 0,0
    pos_y,pos_x=0,0

    filas = []
    fila=[]

    limites = [4,4,3,5,2,4,5,5,7,1]




    for i in range(4):
        cuadro=fondo.subsurface(i*an_corte,1*al_corte,an_corte,al_corte)
        fila.append(cuadro)
    filas.append(fila)

    fila = []
    for i in range(3):
        cuadro=fondo.subsurface(i*an_corte,2*al_corte,an_corte,al_corte)
        fila.append(cuadro)
    filas.append(fila)

    fila = []
    for i in range(5):
        cuadro=fondo.subsurface(i*an_corte,3*al_corte,an_corte,al_corte)
        fila.append(cuadro)
    filas.append(fila)

    fila = []
    for i in range(5):
        cuadro=fondo.subsurface(i*an_corte,6*al_corte,an_corte,al_corte)
        fila.append(cuadro)
    filas.append(fila)

    fila = []
    for i in range(5):
        cuadro=fondo.subsurface(i*an_corte,7*al_corte,an_corte,al_corte)
        fila.append(cuadro)
    filas.append(fila)

    fila = []
    for i in range(7):
        cuadro=fondo.subsurface(i*an_corte,8*al_corte,an_corte,al_corte)
        fila.append(cuadro)
    filas.append(fila)

    cuadro=fondo.subsurface(0*an_corte,9*al_corte,an_corte,al_corte)
    fila = [cuadro]
    filas.append(fila)

    todos = pygame.sprite.Group()
    jugadores = pygame.sprite.Group()
    jugador = Jugador(filas)
    jugadores.add(jugador)
    todos.add(jugador)

    baril=pygame.sprite.Group()
    Bariil = barril()
    baril.add(Bariil)
    todos.add(Bariil)





    reloj=pygame.time.Clock()
    fin=False
    i=0
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    vx = 1
                if event.key == pygame.K_LEFT:
                    vx = -1
                if event.key == pygame.K_DOWN:
                    vy = 1
                if event.key == pygame.K_UP:
                    vy = -1
                if event.key == pygame.K_a:
                    jugador.accion = 2
                    jugador.i = 0
                if event.key == pygame.K_s:
                    jugador.accion = 0
                    jugador.i = 0
                if event.key == pygame.K_z:
                    jugador.accion = 4
                    jugador.i = 0
                if event.key == pygame.K_x:
                    jugador.accion = 5
                    jugador.i = 0
                if event.key == pygame.K_d:
                    jugador.accion = 7
                    jugador.i = 0
                if event.key == pygame.K_SPACE:
                    jugador.accion = 6
                    jugador.i = 0

            if event.type == pygame.KEYUP:
                vx = 0
                vy = 0
                jugador.accion = 0
                jugador.i = 0

        if jugador.accion==2 :
            ls_col=pygame.sprite.spritecollide(jugador,baril,False)
            for b in ls_col:
                if b.rect.bottom>=(jugador.rect.bottom-25):
                    b.rect.x += 20
        if jugador.accion==7 :
            ls_col=pygame.sprite.spritecollide(jugador,baril,False)
            for b in ls_col:
                if b.rect.bottom>=(jugador.rect.bottom-25):
                    b.rect.x += 20

        pantalla.fill([0,0,0])
        pos_x += vx *15
        pos_y += vy *15
        jugador.rect.x = pos_x
        jugador.rect.y = pos_y
        todos.update()
        todos.draw(pantalla)

        pygame.display.flip()
        reloj.tick(20)
