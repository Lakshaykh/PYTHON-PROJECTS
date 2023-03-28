import pygame
import random
import os
pygame.mixer.init()

x=pygame.init()


screen_widht = 900
screen_height = 600
gamewindow=pygame.display.set_mode((screen_widht,screen_height))


bgimg=pygame.image.load("snakeimage.jpg")
bgimg=pygame.transform.scale(bgimg, (screen_widht,screen_height)).convert_alpha()
pygame.display.set_caption("SNAKE GAME")
pygame.display.update()

clock=pygame.time.Clock()
font=pygame.font.SysFont(None, 55)



def text_screen(text,color,x,y):
    screen_text=font.render(text, True, color)
    gamewindow.blit(screen_text, [x,y])
def plot_snake(gamewindow,color,snk_list,snake_size):
    for x,y in snk_list:

        pygame.draw.rect(gamewindow,color, [x,y, snake_size, snake_size])
def welcome():
    exit_game=False
    while not exit_game:
        gamewindow.fill("#00a8f3")
        
        text_screen("Welcome to my saap vala game", "#000000", 200, 250)
        text_screen("Press Enter to play", "#000000", 250, 320)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game =True
            
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    pygame.mixer.music.load("back.mp3")
                    pygame.mixer.music.play()
                    gameloop()

        pygame.display.update()
        clock.tick(60)


def gameloop():
    exit_game=False
    game_over=False
    snake_x = 45
    snake_y = 55
    velocity_x=0
    velocity_y=0
    food_x= random.randint(20, screen_widht)
    food_y= random.randint(20, screen_height)
    snake_size = 20
    score= 0
    init_velocity=5
    fps=60
    if (not os.path.exists("highscore.txt")):
        with open("highscore.txt","w") as f:
            f.write("0")
    with open("highscore.txt","r") as f:
        hiscore=f.read()
    snk_list=[]
    snk_lenght=1
    while not exit_game:
        if game_over:
            with open("highscore.txt","w") as f:
                f.write(str(hiscore))
            gamewindow.fill('#00a8f3')
            text_screen("GAME OVER PRESS ENTER O CONTINUE", '#ff0000', 100, 250)
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        welcome()
        
        
        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocity_x=init_velocity
                        velocity_y=0

                    if event.key==pygame.K_LEFT:
                        velocity_x=-init_velocity
                        velocity_y=0
                    
                    if event.key==pygame.K_UP:
                        velocity_y=-init_velocity
                        velocity_x=0
                    
                    if event.key==pygame.K_DOWN:
                        velocity_y=init_velocity
                        velocity_x=0
                    if event.key == pygame.K_q:
                        score +=10


            snake_x = snake_x +velocity_x
            snake_y= snake_y +velocity_y


            if abs(snake_x - food_x)<12 and abs(snake_y -food_y)<12:
                score +=10

                food_x= random.randint(20, screen_widht/1.5)
                food_y= random.randint(20, screen_height/1.5)
                snk_lenght+=5
                if score>int(hiscore):
                    hiscore=score

            gamewindow.fill("#ffffff")
            gamewindow.blit(bgimg, (0,0))
            text_screen("SCORE:" + str(score) + "  HIGHSCORE :" +str(hiscore) ,'#ff0000',5,5)
            pygame.draw.rect(gamewindow,'#ff0000', (food_x, food_y, snake_size, snake_size))

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_lenght:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over=True


            if snake_x<0 or snake_x>screen_widht or snake_y<0 or snake_y>screen_height:
                game_over=True
                pygame.mixer.music.load("gameover.mp3")
                pygame.mixer.music.play()


            # pygame.draw.rect(gamewindow,'#000000', (snake_x, snake_y, snake_size, snake_size))
            plot_snake(gamewindow,'#000000',snk_list,snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
# gameloop()
welcome()