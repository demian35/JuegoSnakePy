import pygame, sys, time, random #Bibliotecas a usar en este programa

#inicializamos pygame
pygame.init()

#variables globales
interfaz_vista = pygame.display.set_mode((500, 500)) ##vista del juego


fps = pygame.time.Clock() #fps del juego

##funcion para genere comida en algun punto del mapa
def comida():
    punto_rdm=random.randint(0,49)*10#punto aleatorio generado en el plano
    punto_food=[punto_rdm,punto_rdm] ##a la comida le pasamos el punto aleatorio generado previamente tanto en su cord x y su cord y
    return punto_food


def main():

    snakehead = [100, 50] #pixel que pintara la cabeza de la serpiente
    snakebody = [[100,50],[90,50],[80,50]] #arreglo de pixels que formaran la serpiente
    cambio = "RIGHT"
    run = True
  

    while run: #mientras run sea true

        for event in pygame.event.get(): #for para controlar los eventos que ocurran durante el juego
            if event.type == pygame.QUIT: #cuando se presione la X de salir hacemos run False y se acaba la ejecucion
                run = False
            if event.type == pygame.KEYDOWN: #controlador de teclas 
                if event.key == pygame.K_RIGHT or event.key==pygame.K_d: #tecla d o flecha derecha movemos derecha
                    cambio = "RIGHT"
                if event.key == pygame.K_LEFT or event.key==pygame.K_a:  #tecla a o flecha izq movemos izq
                    cambio = "LEFT"
                if event.key == pygame.K_UP or event.key==pygame.K_w: #tecla w o flecha up movemos up
                    cambio = "UP"
                if event.key == pygame.K_DOWN or event.key==pygame.K_s: #tecla s o flecha abajo movemos abajo
                    cambio = "DOWN"
        #efectuamos los movientos en el plano pintando 10 pixeles en el con cada tecla         
        if cambio == "RIGHT":
            snakehead[0] += 10
        if cambio == "LEFT":
            snakehead[0] -= 10
        if cambio == "UP":
            snakehead[1] -= 10
        if cambio == "DOWN":
            snakehead[1] += 10

        #insertamos a la serpiente
        snakebody.insert(0, list(snakehead))
        snakebody.pop()#funcion pop nos permite eliminar los pixeles previamente pintados al moverse

       
        #pintamos el fondo de la vista de acuerdo al RGB
        interfaz_vista.fill((66,70,50))

        for pos in snakebody:
            #Pintamos a la serpiente con un color RGB
            pygame.draw.rect(interfaz_vista,(250,0,0), pygame.Rect(pos[0], pos[1], 10, 10)) #plasmamos en el plano el rectangulo que funjira como serpiente
        
       


        ##Mostramos la vista
        pygame.display.flip()
        fps.tick(10)
main()

#permite llevar a cabo el cierre de la aplicacion
pygame.quit()