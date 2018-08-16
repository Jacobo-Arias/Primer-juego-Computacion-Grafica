import pygame
import random
#Dibuja triangulo y lo escala con el teclado
ANCHO=800
ALTO=600
VERDE=[0,255,0]
AZUL=[0,0,255]
ROJO=[255,0,0]
NEGRO=[0,0,0]
BLANCO=[255,255,255]
GRIS=[155,155,155]

class Jugador (pygame.sprite.Sprite):
    def __init__(self,filas,sonido,accion = 0,):
        pygame.sprite.Sprite.__init__(self)
        self.filas = filas
        self.accion = accion
        self.i = 0
        self.f = self.filas[self.accion]
        self.image = self.f[self.i]
        self.rect = self.image.get_rect()
        self.salud=150
        self.eliminacion=0
        self.eliminacion2 = 0
        self.damage = 10
        self.resistence = 1
        self.dire = 0
        self.punch = sonido
        self.auch = pygame.mixer.Sound('auch.ogg')
        self.vampirismp = 0
    def update(self):
        self.f = self.filas[self.accion+self.dire]
        self.image = self.f[self.i]
        self.i += 1
        if self.i >= len(self.f):
            self.i = 0
        #if self.eliminacion2 >= 6: self.salud += 10

class EnemigoStatico(pygame.sprite.Sprite):
    def __init__(self,filas):
        pygame.sprite.Sprite.__init__(self)
        self.filas = filas
        self.accion = 0
        self.i = 0
        self.image = self.filas[self.accion][self.i]
        self.salud = 50
        self.rect = self.image.get_rect()
        self.wait = 20
        self.vulnerable = True
        self.disparo = 30
        self.sonido = pygame.mixer.Sound("laser.ogg")

    def update(self):
        self.image = self.filas[self.i][self.accion]

class BalaEnemigaH(pygame.sprite.Sprite):
    def __init__(self,bala,dire = 1):
        pygame.sprite.Sprite.__init__(self)
        self.image=bala
        self.rect=self.image.get_rect()
        self.var_x=14*dire
        self.damage = 5
    def update(self):
        self.rect.x += self.var_x

class BalaEnemigaV(pygame.sprite.Sprite):
    def __init__(self,bala,dire = 1):
        pygame.sprite.Sprite.__init__(self)
        self.image=bala
        self.rect=self.image.get_rect()
        self.var_y=14*dire
        self.damage = 5
    def update(self):
        self.rect.y += self.var_y

class Enemigo(pygame.sprite.Sprite):
    def __init__(self,ninja,dire = 1):
        pygame.sprite.Sprite.__init__(self)
        self.dire = dire
        self.ninja = ninja
        self.image = self.ninja[self.dire]
        self.rect = self.image.get_rect()
        self.wait = 5
        self.damage = 20
        self.generation = [ALTO+10,-50,-50,ANCHO+50]
        self.destroy = [-10,ALTO+10,ANCHO+10,-10]
        self.sonido = pygame.mixer.Sound("Explosion01.ogg")

    def update(self):
        if self.dire == 0:
            self.rect.y -= 30
        elif self.dire == 1:
            self.rect.y +=30
        elif self.dire == 2:
            self.rect.x += 30
        elif self.dire == 3:
            self.rect.x -= 30
        elif self.dire >= 4:
            if self.wait == 0:
                self.wait = 5
                self.dire += 1
            else:
                self.wait -= 1
        if self.dire<=6:
            self.image = self.ninja[self.dire]
        else:
            self.dire=6

class MaCursor(pygame.sprite.Sprite):
    def __init__(self,pont):
        pygame.sprite.Sprite.__init__(self)
        self.image=pont
        self.rect=self.image.get_rect()
        self.rect.x=226
        self.rect.y=220
        self.opu=False
        self.opa=False

    def update(self):
        if self.opu:
             if self.rect.y==220:
                 self.rect.y=300
                 self.opu=False
             else:
                 self.rect.y-=40
                 self.opu=False
        elif self.opa:
            if self.rect.y==300:
                self.rect.y=220
                self.opa=False
            else:
                self.rect.y+=40
                self.opa=False

class Comida(pygame.sprite.Sprite):
    def __init__(self,spr,tipo):
        pygame.sprite.Sprite.__init__(self)
        self.tipo=tipo
        self.image=spr
        self.bon=2
        self.rect=self.image.get_rect()
        self.pepsi = pygame.mixer.Sound('pepsiman.ogg')
        self.metal = pygame.mixer.Sound("metal.ogg")

    def update(self):
        if self.tipo==2:
            self.bon=2
        elif self.tipo==1:
            self.bon=0.2

def recorteninja():
    ninja = []
    corte = pygame.image.load('ninup.png')
    ninja.append(corte)
    corte = pygame.image.load('nindown.png')
    ninja.append(corte)
    corte = pygame.image.load('ninrig.png')
    ninja.append(corte)
    corte = pygame.image.load('ninleft.png')
    ninja.append(corte)
    corte = pygame.image.load('boomboom.png')
    for i in range (3):
        corte2 = corte.subsurface(i*48,0,48,48)
        ninja.append(corte2)
    return ninja


if __name__ == '__main__':
    pygame.init()
    regeneration = 75
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    ventana=pygame.display.set_mode([ANCHO,ALTO])
    fondo=pygame.image.load("mapa.png")
    player=pygame.image.load('ryu.png')
    player2=pygame.image.load('robotmen.png')
    robot = pygame.image.load("robot.png")
    animales=pygame.image.load("animals.png")
    cursor=pygame.image.load('cursor.png')
    pizza = pygame.image.load("pizza.png")
    pepsi = pygame.image.load("pepsi.png")
    puno=pygame.mixer.Sound("punch.ogg")

    spritebalaH = pygame.image.load('balaH.png')
    spritebalaV = pygame.image.load('balaV.png')

    fuente= pygame.font.Font(None, 30)
    info=player.get_rect()
    info2=player2.get_rect()
    infon=fondo.get_rect()
    infoene=animales.get_rect()
    inforobot=robot.get_rect()
    an_img=info[2]
    al_img=info[3]
    an_img2=info2[2]
    al_img2=info2[3]
    an_imgene=infoene[2]
    al_imgene=infoene[3]
    an_imrobot = inforobot[2]
    al_imrobot = inforobot[3]

    al_corte=al_img/6
    an_corte=an_img/5
    al_corte2=al_img2/6
    an_corte2=an_img2/5
    al_corteene=al_imgene/8
    an_corteene=an_imgene/12
    al_robot = al_imrobot/2
    an_robot = an_imrobot/2
    x,y=1,0
    vx,vy = 0,0
    vx2,vy2 = 0,0
    pos_y,pos_x=0,0
    pos2_y,pos2_x=0,0
    filas = []
    fila=[]

    ninja = recorteninja()

    '''recorte de los usuarios'''
    limites = [5,5,4,5,5,4]
    k=0
    for j in limites:
        fila = []
        for i in range(j):
            cuadro=player.subsurface(i*an_corte,k*al_corte,an_corte,al_corte)
            fila.append(cuadro)
        k+=1
        filas.append(fila)
    filas2 = []
    k=0
    limites = [4,5,4,4,5,4]
    for j in limites:
        fila = []
        for i in range(j):
            cuadro=player2.subsurface(i*an_corte2,k*al_corte2,an_corte2,al_corte2)
            fila.append(cuadro)
        k+=1
        filas2.append(fila)
    '''Recorte de los enemigos moviles'''
    mene=[]
    i=0
    j=0
    for j in range(3):
        filaene=[]
        for i in range (4):
            cuadroene=animales.subsurface(j*an_corteene,i*al_corteene,an_corteene,al_corteene)
            filaene.append(cuadroene)
        mene.append(filaene)

    '''Recorte Enemigos Estaticos'''
    rob=[]
    i=0
    j=0
    for j in range(2):
        filarob=[]
        for i in range (2):
            dron=robot.subsurface(j*an_robot,i*al_robot,an_robot,al_robot)
            filarob.append(dron)
        rob.append(filarob)

    todos = pygame.sprite.Group()
    balas = pygame.sprite.Group()
    jugadores = pygame.sprite.Group()
    bonus = pygame.sprite.Group()
    jugador = Jugador(filas,puno)
    jugador2 = Jugador(filas2,puno)
    jugadores.add(jugador)
    jugadores.add(jugador2)
    todos.add(jugador)
    todos.add(jugador2)
    point = MaCursor(cursor)
    menu = pygame.sprite.Group()
    menu.add(point)
    enemigos=pygame.sprite.Group()
    enemigosestaticos = pygame.sprite.Group()
    bonpizza=Comida(pizza,1)
    bonpizza.rect.x=2000/2
    bonpizza.rect.y=1200/2
    bonus.add(bonpizza)
    todos.add(bonpizza)


    e1=Enemigo(ninja,0)
    e1.rect.x=random.randrange(50,ANCHO-50)
    e1.rect.y=ALTO+50
    e1.generation=random.randrange(0,100)
    enemigos.add(e1)
    todos.add(e1)
    e2=Enemigo(ninja,1)
    e2.rect.x=random.randrange(50,ANCHO-50)
    e2.rect.y=-50
    e2.generation=random.randrange(0,100)
    enemigos.add(e2)
    todos.add(e2)
    e3=Enemigo(ninja,2)
    e3.rect.x=-50
    e3.rect.y=random.randrange(50,ALTO-150)
    e3.generation=random.randrange(0,100)
    enemigos.add(e3)
    todos.add(e3)
    e4=Enemigo(ninja,3)
    e4.rect.x=ANCHO+50
    e4.rect.y=random.randrange(50,ALTO-150)
    e4.generation=random.randrange(0,100)
    enemigos.add(e4)
    todos.add(e4)
    cant_enemigos=20
    for i in range(20):
        robot=EnemigoStatico(rob)
        robot.rect.x = random.randrange(0,2000)
        robot.rect.y = random.randrange(0,1200)
        enemigosestaticos.add(robot)
        todos.add(robot)

    fonx=0
    fony=0
    pantalla.blit(fondo,[fonx,fony])
    pygame.display.flip()
    reloj=pygame.time.Clock()
    fin=False
    pause=True #Pausa
    opc=False
    findgv=False
    findgd=False
    finsc=False
    puntv=20
    pista = pygame.mixer.Sound("sax.wav")
    pista.play()

    i=0
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    vx = 1
                    jugador.dire=0
                    jugador.accion = 1
                if event.key == pygame.K_a:
                    vx = -1
                    jugador.dire = 3
                    jugador.accion = 1
                if event.key == pygame.K_s:
                    vy = 1
                    point.opa=True
                    jugador.accion = 1
                if event.key == pygame.K_w:
                    vy = -1
                    point.opu=True
                    jugador.accion = 1
                if event.key == pygame.K_RIGHT:
                    vx2 = 1
                    jugador2.dire=0
                    jugador2.accion = 1
                if event.key == pygame.K_LEFT:
                    vx2 = -1
                    jugador2.dire=3
                    jugador2.accion = 1
                if event.key == pygame.K_DOWN:
                    vy2 = 1
                    point.opa=True
                    jugador2.accion = 1
                if event.key == pygame.K_UP:
                    vy2 = -1
                    point.opu=True
                    jugador2.accion = 1
                if event.key == pygame.K_t:
                    jugador.accion = 2
                    jugador.i = 0
                if event.key == pygame.K_l:
                    jugador2.accion = 2
                    jugador2.i = 0
                if event.key == pygame.K_b:
                    jugador2.vampirismp = 2
                if event.key == pygame.K_v:
                    jugador.vampirismp = 2
                if event.key == pygame.K_SPACE:
                    if findgd or findgv:
                        finsc=True
                if event.key==pygame.K_p:
                    if point.rect.y==220:
                        pause=not pause
                    if point.rect.y==300:
                        fin=True
                    if point.rect.y==260:
                        opc=not opc

            if event.type == pygame.KEYUP: #stop acciones
                if event.key == pygame.K_d:
                    vx = 0
                if event.key == pygame.K_a:
                    vx = 0
                if event.key == pygame.K_s:
                    vy = 0
                if event.key == pygame.K_w:
                    vy = 0
                if event.key == pygame.K_RIGHT:
                    vx2 = 0
                if event.key == pygame.K_LEFT:
                    vx2 = 0
                if event.key == pygame.K_DOWN:
                    vy2 = 0
                if event.key == pygame.K_UP:
                    vy2 = 0
                jugador2.accion=0
                jugador2.i=0
                jugador.accion =0
                jugador.i = 0



        ###########Limitadores de pantalla#############
        ###########Limitadores de pantalla en X ############
        if(pos_x+an_corte>=ANCHO):
            if(fonx-15>=ANCHO-infon[2]):
                jugador.rect.x=jugador.rect.x
                ls_col=enemigos
                ls_col2=enemigosestaticos
                ls_col3=balas
                ls_col4=bonus
                pos_x-=15
                pos2_x-=15
                fonx-=15
                for e in ls_col:
                    e.rect.x-=15
                for e in ls_col2:
                    e.rect.x-=15
                for e in ls_col3:
                    e.rect.x-=15
                for e in ls_col4:
                    e.rect.x-=15
            else:
                jugador.rect.x=jugador.rect.x
                pos_x-=15

        else:
            jugador.rect.x = pos_x

        if(pos_x<=5):
            if(fonx+15<=0):
                ls_col=enemigos
                ls_col2=enemigosestaticos
                ls_col3=balas
                ls_col4=bonus
                jugador.rect.x=jugador.rect.x
                pos_x+=15
                pos2_x+=15
                fonx+=15
                for e in ls_col:
                    e.rect.x+=15
                for e in ls_col2:
                    e.rect.x+=15
                for e in ls_col3:
                    e.rect.x+=15
                for e in ls_col4:
                    e.rect.x+=15
            else:
                jugador.rect.x=jugador.rect.x
                pos_x+=15
        else:
            jugador.rect.x = pos_x

        if(pos2_x+an_corte>=ANCHO):
            if(fonx-15>=ANCHO-infon[2]):
                jugador2.rect.x=jugador2.rect.x
                ls_col=enemigos
                ls_col2=enemigosestaticos
                ls_col3=balas
                ls_col4=bonus
                pos2_x-=15
                pos_x-=15
                fonx-=15
                for e in ls_col:
                    e.rect.x-=15
                for e in ls_col2:
                    e.rect.x-=15
                for e in ls_col3:
                    e.rect.x-=15
                for e in ls_col4:
                    e.rect.x-=15
            else:
                jugador2.rect.x=jugador2.rect.x
                pos2_x-=15
        else:
            jugador2.rect.x = pos2_x

        if(pos2_x<=5):
            if(fonx+15<=0):
                ls_col=enemigos
                ls_col2=enemigosestaticos
                ls_col3=balas
                ls_col4=bonus
                jugador2.rect.x=jugador2.rect.x
                pos2_x+=15
                pos_x+=15
                fonx+=15
                for e in ls_col:
                    e.rect.x+=15
                for e in ls_col2:
                    e.rect.x+=15
                for e in ls_col3:
                    e.rect.x+=15
                for e in ls_col4:
                    e.rect.x+=15
            else:
                jugador2.rect.x=jugador2.rect.x
                pos2_x+=15
        else:
            jugador2.rect.x = pos2_x

        ###########Limitadores de pantalla en Y ############
        if(pos_y>=ALTO-100-al_corte):
            if(fony-15>=ALTO-100-infon[3]):
                ls_col=enemigos
                ls_col2=enemigosestaticos
                ls_col3=balas
                ls_col4=bonus
                jugador.rect.y=jugador.rect.y
                pos_y-=15
                pos2_y-=15
                fony-=15
                for e in ls_col:
                    e.rect.y-=15
                for e in ls_col2:
                    e.rect.y-=15
                for e in ls_col3:
                    e.rect.y-=15
                for e in ls_col4:
                    e.rect.y-=15
            else:
                jugador.rect.y=jugador.rect.y
                pos_y-=15
        else:
            jugador.rect.y = pos_y

        if(pos_y<=10):
            if(fony+15<=0):
                ls_col=enemigos
                ls_col2=enemigosestaticos
                ls_col3=balas
                ls_col4=bonus
                jugador.rect.y=jugador.rect.y
                pos_y+=15
                pos2_y+=15
                fony+=15
                for e in ls_col:
                    e.rect.y+=15
                for e in ls_col2:
                    e.rect.y+=15
                for e in ls_col3:
                    e.rect.y+=15
                for e in ls_col4:
                    e.rect.y+=15
            else:
                jugador.rect.y=jugador.rect.y
                pos_y+=15
        else:
            jugador.rect.y = pos_y

        if(pos2_y>=ALTO-100-al_corte):
            if(fony-15>=ALTO-100-infon[3]):
                ls_col=enemigos
                ls_col2=enemigosestaticos
                ls_col3=balas
                ls_col4=bonus
                jugador2.rect.y=jugador2.rect.y
                pos2_y-=15
                pos_y-=15
                fony-=15
                for e in ls_col:
                    e.rect.y-=15
                for e in ls_col2:
                    e.rect.y-=15
                for e in ls_col3:
                    e.rect.y-=15
                for e in ls_col4:
                    e.rect.y-=15
            else:
                jugador2.rect.y=jugador2.rect.y
                pos2_y-=15
        else:
            jugador2.rect.y = pos2_y

        if(pos2_y<=10):
            if(fony+15<=0):
                ls_col=enemigos
                ls_col2=enemigosestaticos
                ls_col3=balas
                ls_col4=bonus
                jugador2.rect.y=jugador2.rect.y
                pos2_y+=15
                pos_y+=15
                fony+=15
                for e in ls_col:
                    e.rect.y+=15
                for e in ls_col2:
                    e.rect.y+=15
                for e in ls_col3:
                    e.rect.y+=15
                for e in ls_col4:
                    e.rect.y+=15
            else:
                jugador2.rect.y=jugador2.rect.y
                pos2_y+=15
        else:
            jugador2.rect.y = pos2_y

        for e in balas:
            if e.rect.bottom<=0 or e.rect.top>=ALTO:
                e.remove(balas)
                e.remove(todos)
            if e.rect.right<=0 or e.rect.left>ANCHO:
                e.remove(balas)
                e.remove(todos)

        for e in enemigos:
            if e.dire == 0:
                if e.destroy[e.dire] >= e.rect.y:
                    e.remove(todos)
                    e.remove(enemigos)
            elif e.dire == 1:
                if e.destroy[e.dire] <= e.rect.y:
                    e.remove(todos)
                    e.remove(enemigos)
            elif e.dire == 2:
                if e.destroy[e.dire] <= e.rect.x:
                    e.remove(todos)
                    e.remove(enemigos)
            elif e.dire == 3:
                if e.destroy[e.dire] >= e.rect.x:
                    e.remove(todos)
                    e.remove(enemigos)
            if e.dire==6 and e.wait==0:
                    e.remove(todos)
                    e.remove(enemigos)

        ##################################################
        ############    Pausa  ############
        if jugador.salud<=0 or jugador2.salud<=0:
            findgd=True
            pause=True
        if jugador.eliminacion2+jugador2.eliminacion2>=cant_enemigos:
            findgv=True
            pause=True

        if findgv and pause:
            pantalla.fill([0,0,0])
            txt_creditos=fuente.render("Victoria de:", False, BLANCO)
            pantalla.blit(txt_creditos,[330, 310])
            if jugador.eliminacion>jugador2.eliminacion:
                txt_creditos=fuente.render("Jugador 1", False, BLANCO)
                pantalla.blit(txt_creditos,[330, 370])
            else:
                txt_creditos=fuente.render("Jugador 2", False, BLANCO)
                pantalla.blit(txt_creditos,[330, 370])
            txt_creditos=fuente.render("Presione espacio para salir ", False, BLANCO)
            pantalla.blit(txt_creditos,[270, 450])
            menu.draw(pantalla)
            pygame.display.flip()
            if finsc:
                fin=True

        elif findgd and pause:
            pantalla.fill([0,0,0])
            txt_creditos=fuente.render("Derrota ", False, BLANCO)
            pantalla.blit(txt_creditos,[300, 310])
            txt_creditos=fuente.render("Presione espacio para salir ", False, BLANCO)
            pantalla.blit(txt_creditos,[270, 450])
            menu.draw(pantalla)
            pygame.display.flip()
            if finsc:
                fin=True

        elif pause==False:
            pantalla.fill([0,0,0])
            pantalla.blit(fondo,[fonx,fony])
            if jugador.eliminacion+jugador.eliminacion2 >= 6:
                pos_x += (vx*1.2) *15
                pos_y += (vy*1.2) *15
            else:
                pos_x += vx *15
                pos_y += vy *15
            if jugador2.eliminacion+jugador2.eliminacion2>=6:
                pos2_x += (vx2*1.2) *15
                pos2_y += (vy2*1.2) *15
            else:
                pos2_x += vx2 *15
                pos2_y += vy2 *15
            if regeneration == 0:
                regeneration = 75
                e1=Enemigo(ninja,0)
                e1.rect.x=random.randrange(50,ANCHO-50)
                e1.rect.y=ALTO+50
                e1.generation=random.randrange(0,100)
                enemigos.add(e1)
                todos.add(e1)
                e2=Enemigo(ninja,1)
                e2.rect.x=random.randrange(50,ANCHO-50)
                e2.rect.y=-50
                e2.generation=random.randrange(0,100)
                enemigos.add(e2)
                todos.add(e2)
                e3=Enemigo(ninja,2)
                e3.rect.x=-50
                e3.rect.y=random.randrange(50,ALTO-150)
                e3.generation=random.randrange(0,100)
                enemigos.add(e3)
                todos.add(e3)
                e4=Enemigo(ninja,3)
                e4.rect.x=ANCHO+50
                e4.rect.y=random.randrange(50,ALTO-150)
                e4.generation=random.randrange(0,100)
                enemigos.add(e4)
                todos.add(e4)
            else:
                regeneration -= 1
            todos.update()
            todos.draw(pantalla)
            enemigos.draw(pantalla)
            pygame.draw.polygon(pantalla, NEGRO, [(0,ALTO-100),(0,ALTO),(ANCHO,ALTO),(ANCHO,ALTO-100)])
            #DATA jugador 1
            txt_ply1=fuente.render("Jugador 1", False, BLANCO)
            txt_salud=fuente.render("Salud:", False, BLANCO)
            txt_vsalud= fuente.render(str(jugador.salud), False, BLANCO)
            txt_eliminacion=fuente.render("Eliminaciones: ", False, BLANCO)
            txt_veliminacion= fuente.render(str(jugador.eliminacion + jugador.eliminacion2), False, BLANCO)
            pantalla.blit(txt_ply1,[50, ALTO-80])
            pantalla.blit(txt_salud,[50, ALTO-50])
            pantalla.blit(txt_vsalud, [120, ALTO-50])
            pantalla.blit(txt_eliminacion, [50, ALTO-30])
            pantalla.blit(txt_veliminacion, [200, ALTO-30])
            #DATA jugador 2
            txt_ply2=fuente.render("Jugador 2", False, BLANCO)
            txt_salud2=fuente.render("Salud:", False, BLANCO)
            txt_vsalud2= fuente.render(str(jugador2.salud), False, BLANCO)
            txt_eliminacion2=fuente.render("Eliminaciones: ", False, BLANCO)
            txt_veliminacion2= fuente.render(str(jugador2.eliminacion + jugador2.eliminacion2), False, BLANCO)
            pantalla.blit(txt_ply2,[340, ALTO-80])
            pantalla.blit(txt_salud2,[340, ALTO-50])
            pantalla.blit(txt_vsalud2, [410, ALTO-50])
            pantalla.blit(txt_eliminacion2, [340, ALTO-30])
            pantalla.blit(txt_veliminacion2, [490, ALTO-30])
            pygame.display.flip()
            for men in jugadores:
                ls_col2=pygame.sprite.spritecollide(men,enemigosestaticos, False) #enemigos estaticos
                for e in ls_col2:
                    if men.accion==2 and men.dire==0 and e.rect.center[0]>=men.rect.center[0]:
                        if e.vulnerable:
                            e.salud-=men.damage
                            men.salud += men.vampirismp
                            if men.salud >= 200:
                                men.salud = 200
                            men.punch.play()
                        e.wait = 20

                    if men.accion==2 and men.dire==3 and e.rect.center[0]<=men.rect.center[0]:
                        if e.vulnerable:
                            e.salud-=men.damage
                        e.wait = 20

                    if e.salud <= 0:
                        e.i = 1
                        if e.vulnerable:
                            men.eliminacion2 += 1
                        e.vulnerable = False

                ls_col2=pygame.sprite.spritecollide(men,balas, True) #balas
                for e in ls_col2:
                    if men.salud > 0:
                        men.auch.play()
                        men.salud -= e.damage * men.resistence
                    else:
                        men.remove(todos)
                        men.remove(jugadores)

                ls_col2=pygame.sprite.spritecollide(men,enemigos, False) #kamikaze
                for e in ls_col2:
                    if e.dire <=3:
                        e.sonido.play()
                        men.auch.play()
                        e.rect.center = men.rect.center
                        men.salud-=e.damage*men.resistence
                        e.dire=4


                ls_col2=pygame.sprite.spritecollide(men,bonus, True) #comida
                for e in ls_col2:
                    if e.tipo == 1:
                        e.metal.play()
                        men.resistence-=e.bon
                    elif e.tipo == 2:
                        e.pepsi.play()
                        men.damage += e.bon

            #for b in balas:
                #if
            for static in enemigosestaticos:
                static.disparo -= 1
                if static.vulnerable:
                    if static.disparo == 0:
                        static.sonido.play()
                        static.disparo = 30
                        bala = BalaEnemigaH(spritebalaH,1)
                        bala.rect.center = static.rect.center
                        balas.add(bala)
                        todos.add(bala)
                        bala = BalaEnemigaH(spritebalaH,-1)
                        bala.rect.center = static.rect.center
                        balas.add(bala)
                        todos.add(bala)
                        bala = BalaEnemigaV(spritebalaV,1)
                        bala.rect.center = static.rect.center
                        balas.add(bala)
                        todos.add(bala)
                        bala = BalaEnemigaV(spritebalaV,-1)
                        bala.rect.center = static.rect.center
                        balas.add(bala)
                        todos.add(bala)

                static.wait -=1
                if static.wait == 0:
                    static.wait = 20
                    if static.accion == 0:
                        static.accion = 1
                    else:
                        static.accion = 0
                    if static.salud <= 0:
                        e = Comida(pepsi,2)
                        e.rect.x=static.rect.x
                        e.rect.y=static.rect.y
                        bonus.add(e)
                        todos.add(e)
                        static.remove(enemigosestaticos)
                        static.remove(todos)

        elif pause==True and opc==False:
            menu.update()
            pantalla.fill(NEGRO)
            txt_creditos=fuente.render("Jugar ", False, BLANCO)
            pantalla.blit(txt_creditos,[300, 230])
            txt_creditos=fuente.render("Creditos ", False, BLANCO)
            pantalla.blit(txt_creditos,[300, 270])
            txt_creditos=fuente.render("Salir ", False, BLANCO)
            pantalla.blit(txt_creditos,[300, 310])
            menu.draw(pantalla)
            pygame.display.flip()

        elif pause==True and opc==True:
            pantalla.fill(NEGRO)
            txt_creditos=fuente.render("Creditos ", False, GRIS)
            pantalla.blit(txt_creditos,[350, 300])
            txt_n1=fuente.render("Juan Jacobo Arias ", True, GRIS)
            pantalla.blit(txt_n1,[310, 340])
            txt_n2=fuente.render("Lizardo Perdomo Carmona ", False, GRIS)
            pantalla.blit(txt_n2,[290, 380])
            txt_n3=fuente.render("Volver ", False, BLANCO)
            pantalla.blit(txt_n3,[370, 260])
            pygame.display.flip()
        ##################################################
        reloj.tick(15)
