import pygame
import random
import shelve

import button

pygame.init()


#set up the display window size

WIDTH, HEIGHT = 600, 600

WIN = pygame.display.set_mode((WIDTH,HEIGHT))

#Window Name

pygame.display.set_caption("Going Dark")

#Colours

Background_CLR = (255,255,255) #WHite

WHITE = (255,255,255)
BLACK = (0,0,0)

#Fonts

font = pygame.font.Font('MPLUSRounded1c-Regular.ttf',25)

#game states

main_menu = True

play_game = False

end_game = False

#Images

play_img = pygame.image.load('Assets\Play_Button.png')
play_img = pygame.transform.scale(play_img, (150,150))

exit_img = pygame.image.load('Assets\Exit_Button.png')
exit_img = pygame.transform.scale(exit_img, (150,150))

Golden_Key = pygame.image.load('Assets\Golden Key.png')
Golden_Key = pygame.transform.scale(Golden_Key, (30,30))

Background_image = pygame.image.load('Assets\Background_Image.png')

#Sounds

key_clicked = pygame.mixer.Sound('Assets\correct_ding.mp3')

#Buttons

play_button = button.Button(228,100, play_img)
exit_button = button.Button(230,180, exit_img)

#key_button = button.Button(50,50, Golden_Key)


#Game FPS
FPS = 60

#Score
score = 0

#Countdown Timer

time_limit = 10

count_down = time_limit

last_count = pygame.time.get_ticks()

#Changes the key location when the key is pressed.
def change_location():

    global key_button

    x_pos = (random.randrange(30,501))
    y_pos = (random.randrange(30,501))

    key_button = button.Button(x_pos, y_pos, Golden_Key)

change_location()

#Displays the players current score.
def current_score(score):
    score_text = font.render(f'Score: {score}', True, WHITE)
    WIN.blit(score_text,(0,0))


def draw_menu():
    global run, main_menu,play_game, count_down, score

    play_game = False
    main_menu = True
    
    WIN.set_clip(None) #Resets the clipping area so the screen doesn't remain black
    WIN.fill(Background_CLR)

    #opens the file containing the highest score and reads it.
    d = shelve.open('highscore.txt')
    high_score = d['highscore']
    d.close()

    if count_down == 0:
        end_text = font.render('You ran out of time!', True, BLACK)
        WIN.blit(end_text,(190,10))


    if play_button.draw(WIN):
        score = 0
        play_game = True
        count_down = time_limit


    if exit_button.draw(WIN):
        run = False


    high_scoretxt = font.render(f'Highest Score: {high_score}', True, BLACK)
    WIN.blit(high_scoretxt,(200,300))

    
    desc_text = font.render('Find the key to gain points!', True, BLACK)
    WIN.blit(desc_text,(150,500))


    pygame.display.update()



def draw_game():

    global score, count_down, main_menu, last_count, play_game

    main_menu = False


    radius = 50
    surf = pygame.Surface((radius * 2, radius *2))
    surf.fill(0)
    surf.set_colorkey((255,255,255))
    pygame.draw.circle(surf, (255,255,255),(radius,radius), radius)

    clip_center = pygame.mouse.get_pos()


    WIN.fill(BLACK)
    
    clip_rect = pygame.Rect(clip_center[0] - radius, clip_center[1] - radius, radius *  2, radius * 2) #The area of the screen to be clipped.
    WIN.set_clip(clip_rect) # if set_clip isn't "reset or set to none" the screen will remain black after returning to main menu.
    WIN.blit(Background_image, (0, 0))
    WIN.blit(surf, clip_rect)


    if key_button.draw(WIN):
        score += 1
        key_clicked.play()
        change_location()

    if count_down > 0:
        count_text = font.render(f'{count_down}', True, WHITE)
        WIN.blit(count_text, (290,0))
        count_timer = pygame.time.get_ticks()
        if count_timer - last_count > 1000:
            count_down -= 1
            last_count = count_timer
    elif count_down == 0:
        #saves the score into the file if it is higher.
        d = shelve.open('highscore.txt')
        high_score = d['highscore']
        if score > high_score:
            d['highscore'] = score
            d.close()
        
        #returns the player to the main menu.
        main_menu = True



    current_score(score)

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


