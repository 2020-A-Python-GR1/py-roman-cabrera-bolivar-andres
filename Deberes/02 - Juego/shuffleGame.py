import pygame
import numpy as np

COLUMNS = 4
ROWS = 4
RANDOM_MVS = 50
height, width = 660, 660
dim_width = width / ROWS
dim_height = height / COLUMNS

hor_border = pygame.Surface((int(dim_width), 2))
ver_border = pygame.Surface((2, int(dim_height)))


image = pygame.image.load('image.jpg')
pieces = {}
for row in range(ROWS):
    for col in range(COLUMNS):
        piece = image.subsurface(int(row*dim_height), int(col*dim_width), int(dim_height), int(dim_width))
        piece.blit(hor_border, (0, 0))
        piece.blit(ver_border, (0, 0))
        pieces[(row,col)] = piece


black_piece = (np.random.randint(3),np.random.randint(3))
pieces[black_piece].fill((0,0,0))
(blackCol, blackRow) = black_piece
initial_state = {(row,col): (row,col) for row in range(ROWS) for col in range(COLUMNS)}
state = {(row,col): (row,col) for row in range(ROWS) for col in range(COLUMNS)}

pygame.init()
display = pygame.display.set_mode((height,width))
pygame.display.set_caption("shift-puzzle")
display.blit (image, (0, 0))
pygame.display.flip()



def swap(c,r):
     global blackCol, blackRow
     display.blit(pieces[state[(c, r)]],(int(blackCol*dim_width), int(blackRow*dim_height)))
     display.blit(pieces[black_piece],(int(c*dim_width), int(r*dim_height)))
     state[(blackCol, blackRow)] = state[(c, r)]
     state[(c, r)] = black_piece
     (blackCol, blackRow) = (c, r)
     pygame.display.flip()
     print(state)


def rearrange_game():
    for i in range(RANDOM_MVS):
        swap(np.random.randint(3),np.random.randint(3))
        pygame.time.delay(100)


def message_display(text):
    font = pygame.font.Font('freesansbold.ttf',115)
    TextSurf = font.render(text,True, (255,255,255))
    TextRect = TextSurf.get_rect()
    TextRect.center = (int(width/2),int(height/2))
    display.blit(TextSurf, TextRect)
    pygame.display.update()



rearrange_game()
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        quit()
    elif event.type == pygame.MOUSEBUTTONDOWN:
        clic = pygame.mouse.get_pos() 
        rw = int(clic[1] / dim_width)
        cl = int(clic[0] / dim_height)
        swap(cl,rw)
        if (initial_state == state):
            message_display("Game over")