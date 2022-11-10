import pygame, sys, time, random

pygame.init()

play_surface = pygame.display.set_mode((500, 500))


fps = pygame.time.Clock()





def main():

    snakehead = [100, 50]
    snakebody = [[100,50],[90,50],[80,50]]
    cambio = "RIGHT"
    run = True
  

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    cambio = "RIGHT"
                if event.key == pygame.K_LEFT:
                    cambio = "LEFT"
                if event.key == pygame.K_UP:
                    cambio = "UP"
                if event.key == pygame.K_DOWN:
                    cambio = "DOWN"
        if cambio == "RIGHT":
            snakehead[0] += 10
        if cambio == "LEFT":
            snakehead[0] -= 10
        if cambio == "UP":
            snakehead[1] -= 10
        if cambio == "DOWN":
            snakehead[1] += 10

        snakebody.insert(0, list(snakehead))

       

        play_surface.fill((0,0,0))

        for pos in snakebody:
            pygame.draw.rect(play_surface,(250,0,0), pygame.Rect(pos[0], pos[1], 10, 10))
        
       



        pygame.display.flip()
        fps.tick(10)
main()

pygame.quit()