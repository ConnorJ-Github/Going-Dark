import pygame
import button

pygame.init()


#set up the display window size

WIDTH, HEIGHT = 600, 600

WIN = pygame.display.set_mode((WIDTH,HEIGHT))

#Window Name

pygame.display.set_caption("Going Dark")

#game states

main_menu = True

play_game = False

#Colours

Background_CLR = (255,255,255) #WHite


#Buttons

play_img = pygame.image.load('Assets\Play_Button.png')
play_img = pygame.transform.scale(play_img, (150,150))

exit_img = pygame.image.load('Assets\Exit_Button.png')
exit_img = pygame.transform.scale(exit_img, (150,150))

play_button = button.Button(228,100, play_img)
exit_button = button.Button(230,180, exit_img)

#Images

Golden_Key = pygame.image.load('Assets\Golden Key.png')
Golden_Key = pygame.transform.scale(Golden_Key, (75,75))

Background_image = pygame.image.load('Assets\Background_Image.png')



#Game FPS
FPS = 60


def draw_menu():

    global run, main_menu,play_game
    
    WIN.fill(Background_CLR)

    if play_button.draw(WIN):
        play_game = True


    if exit_button.draw(WIN):
        run = False

    pygame.display.update()

def draw_game():

    global main_menu
    main_menu = False

    WIN.blit(Background_image, (0, 0))
    WIN.blit(Golden_Key, (0,0))

    pygame.display.update()



clock = pygame.time.Clock()

run = True
while run:

    clock.tick(FPS)


    #if main_menu is true, draws the main menu
    if main_menu:
        draw_menu()

    #if play_game is true, draws the game scene
    if play_game:
        draw_game()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False





pygame.quit()


