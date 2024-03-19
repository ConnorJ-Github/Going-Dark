import pygame

pygame.init()


#set up the display window size

WIDTH, HEIGHT = 600, 600

WIN = pygame.display.set_mode((WIDTH,HEIGHT))

#Window Name

pygame.display.set_caption("Going Dark")


#Colours

Background_CLR = (255,255,255) #WHite


#Game FPS
FPS = 60


def draw_window():

    WIN.fill(Background_CLR)

    pygame.display.update()





clock = pygame.time.Clock()

run = True
while run:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    draw_window()


    



if __name__ == "__main__":
    main()