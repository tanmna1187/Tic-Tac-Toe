
import pygame, sys, os
from pygame.locals import *


pygame.init()
pygame.display.set_caption('Tic-Tac-Toe')

clock = pygame.time.Clock() 
screen_height = 600
screen_width = 600
screen = pygame.display.set_mode((screen_width,screen_height))
row1 = pygame.Rect(screen_width/2 - 90, screen_height/2 - 250, 10, 500)
row2 = pygame.Rect(screen_width/2 + 90, screen_height/2 - 250, 10, 500)
column1 = pygame.Rect(screen_width/2 - 250, screen_height/2 - 90, 500, 10)
column2 = pygame.Rect(screen_width/2 - 250, screen_height/2 + 90, 500, 10)
bg_color = pygame.Color('black')
white = (255,255,255)
white_x = pygame.image.load("white x.png")
white_o = pygame.image.load("white o.png")
grey_square=  pygame.image.load("grey_square.png")
you_won = pygame.image.load("winner.png")
x_wins = pygame.image.load("x_wins.png")
o_wins = pygame.image.load("o_wins.png")
cat_wins = pygame.image.load("cat_game.png")
squares = [(80,80), (265,80), (430,80), (80,260), (265,260), (430,260), (80,440), (265,440),(430,440)]
winning_squares =[[0,1,2], [3,4,5], [2,4,6], [0,4,8], [0,3,6], [2,5,8], [1,4,7], [6,7,8]]
listx = winning_squares[0]
winner = 'none'
reset_code  = False

def main():
    global square
    global player
    x_squares = []
    o_squares = []
    all_squares = []
    used_square = False
    square = 0
    counter = 0 
    player = True #Player 1 = True Player 2 = False


    def key_handeling():
        global square
        global space
        global winner
        space = False
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    square -= 1
                elif event.key == pygame.K_RIGHT:
                    square += 1
                elif event.key == pygame.K_UP:
                    square -= 3
                elif event.key == pygame.K_DOWN:
                    square += 3
                elif event.key == pygame.K_SPACE:
                    space = True
                elif event.key == pygame.K_RETURN:
                    reset_code = True
                    reset()
                    winner = 'none'


        if square >= 8:
            square = 8
        if square <= 0:
            square = 0


    def draw_board():
        screen.fill(bg_color)
        pygame.draw.rect(screen, white, row1)
        pygame.draw.rect(screen, white, row2)
        pygame.draw.rect(screen, white, column1)
        pygame.draw.rect(screen, white, column2)

    def draw_x():
        global player
        global used_square
        used_square = False
        if space == True:
            all_squares = x_squares + o_squares
            for n in range(len(all_squares)):
                if square == all_squares[n]:
                    used_square = True
            if used_square == False:
                x_squares.append(square)
                player = False
        for i in range(len(x_squares)):
            screen.blit(white_x,squares[x_squares[i]])
        screen.blit(grey_square,squares[square])
        for o in range(len(o_squares)):
            screen.blit(white_o,squares[o_squares[o]])


    def draw_o():
        global player
        global used_square
        used_square = False
        screen.blit(grey_square,squares[square])
        if space == True:
            all_squares = x_squares + o_squares
            for n in range(len(all_squares)):
                if square == all_squares[n]:
                    used_square = True
            if used_square == False:
                o_squares.append(square)
                player = True
        for i in range(len(o_squares)):
            screen.blit(white_o,squares[o_squares[i]])
        for x in range(len(x_squares)):
            screen.blit(white_x,squares[x_squares[x]])


    def winx():
        global counter
        global winner
        for m in range(len(winning_squares)):
            counter = 0
            listx = winning_squares[m]
            for l in range(len(x_squares)):
                for i in range(len(listx)):
                    x_squares.sort()
                    if x_squares[l - 1] == listx[i - 1]:
                        counter += 1
                        if counter == 3:
                            winner = 'x'
                            counter = 0


    def wino():
        global counter
        global winner
        for m in range(len(winning_squares)):
            counter = 0
            listx = winning_squares[m]
            for l in range(len(o_squares)):
                for i in range(len(listx)):
                    o_squares.sort()
                    if o_squares[l - 1] == listx[i - 1]:
                        counter += 1
                        if counter == 3:
                            winner = 'o'





    def cat_game():
        global winner
        used_squares = len(x_squares) + len(o_squares)
        if used_squares >= 9:
            winner = 'cat'
            print('cat')

    def reset():
        x_squares.clear()
        o_squares.clear()
        all_squares = []
        used_square = False
        square = 0
        counter = 0 
        winner ='none'
        player = True
              
    


    while True:
        global winner
        while winner == 'none':
            winner = 'none'
            key_handeling()
            draw_board()
            if player == True:
                draw_x()
            elif player == False:
                draw_o()

            cat_game()
            winx()
            wino()
            pygame.display.flip()
            clock.tick(60)


        while winner != 'none':
            if winner == 'x':
                screen.blit(x_wins,(0,0))
                key_handeling()

            elif winner == 'o':
                screen.blit(o_wins,(0,0))
                key_handeling()
            elif winner == 'cat':
                screen.blit(cat_wins,(0,0))
                key_handeling()




            pygame.display.flip()
            clock.tick(60)
main()