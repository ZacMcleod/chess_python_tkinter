import pygame as pg

pg.init()

screen_width = 400

screen_height = 400

square_size = screen_width // 8

screen = pg.display.set_mode((screen_width, screen_height))

pg.display.set_caption("Chessboard")

white = (255, 255, 255)

black = (0, 0, 0)

def draw_chessboard():
    for row in range(8):
        for col in range(8):
            if (row + col) % 2 == 0:
                color = white
            else:
                color = black
                pg.draw.rect(screen, color, (col * square_size, row * square_size, square_size, square_size))

running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    screen.fill(white)
    draw_chessboard()
    pg.display.flip()

pg.quit()