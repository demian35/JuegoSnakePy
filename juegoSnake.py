import pygame , sys,time,random #bibliotecas necesarias para el desarrollo

#inicializamos pygame
pygame.init()


#interfaz proporcionada por la biblioteca pygame le pasamos las medidas del alto y ancho
interfaz_game=pygame.display.set_mode((600,600))

#fps del juego
fps=pygame.time.Clock()

def main():
    headSnake=[100,50] #cabeza de la serpiente que ocupara un pixel o cuadrito [x,y]
    snakeBody=[[100,50],[90,50],[80,50]] #arrreglo de pixeles que formara la serpiente

    run=True

    while run: ##mientras se este ejecutando run
        for event in pygame.event.get(): ##for para controlar los eventos que ocurran durante la ejecucion
            if event.type== pygame.QUIT: ##si el usuario se sale run cambia a falso y la ejecucio termina
                run=False

        interfaz_game.fill((75,83,32)) #pintamos la interfaz asignandole un color en la escala rgb

        #llamadas para abrir la interfaz
        pygame.display.flip()
        fps.tick(10)
   #llamada a pygame para que se cierre el juego en caso de que el usuario salga
main()

pygame.quit() ##efectua el cierre del programa cuando se pica el icono X
