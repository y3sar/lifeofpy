import pygame as pg
from pygame.locals import FULLSCREEN, DOUBLEBUF
import random

pg.init();


WIDTH, HEIGHT = 500, 500;
LINE_WIDTH = 1
win = pg.display.set_mode((WIDTH,HEIGHT));

# Colors
BLACK = (0, 0, 0);
WHITE = (255, 255, 255);

# ENV
LINESPACE = 10; # 50 X 50 Grid 

LAST_ROW = (WIDTH // LINESPACE) - 1 
LAST_COLUMN = (HEIGHT // LINESPACE) - 1


pg.display.set_caption("Game Of Life");


game_env = [[(random.randint(0,1), i+1, j+1) for i in range(0, WIDTH, LINESPACE)] for j in range(0, HEIGHT, LINESPACE)];

neighbour_count = [[0 for i in range(0, WIDTH, LINESPACE)] for j in range(0, HEIGHT, LINESPACE)];



def draw_grid(surface, color, line_spacing):
    for i in range(0, WIDTH, line_spacing):
        pg.draw.line(surface, color, (i, 0), (i, HEIGHT), LINE_WIDTH);

    pg.draw.line(surface, color, (WIDTH-1, 0), (WIDTH-1, HEIGHT-1), LINE_WIDTH);

    

    for i in range(0, HEIGHT, line_spacing):
        pg.draw.line(surface, color, (0, i), (WIDTH, i), LINE_WIDTH);
    pg.draw.line(surface, color, (0, HEIGHT-1), (WIDTH-1, HEIGHT-1), LINE_WIDTH);


def populate_cell(row, column):
    _, x, y = game_env[row][column]

    if not is_cell_alive(row, column):
        game_env[row][column] = (1, x, y);

def kill_cell(row, column):
    _, x, y = game_env[row][column];

    if is_cell_alive(row, column):
        game_env[row][column] = (0, x, y);

def is_cell_alive(row, column):
    if row > LAST_ROW or column > LAST_COLUMN or row < 0 or column < 0:
        return 0;

    return game_env[row][column][0];

def check_neighbour(row, column):
    living_neighbour = 0;

    living_neighbour += is_cell_alive(row+1, column);
    living_neighbour += is_cell_alive(row-1, column);

    living_neighbour += is_cell_alive(row, column+1);
    living_neighbour += is_cell_alive(row, column-1);

    living_neighbour += is_cell_alive(row-1, column-1);
    living_neighbour += is_cell_alive(row+1, column+1);
    living_neighbour += is_cell_alive(row-1, column+1);
    living_neighbour += is_cell_alive(row+1, column-1);

    return living_neighbour

def implement_rules():

    neighbour_counts = [[0 for i in range(0, WIDTH, LINESPACE)] for j in range(0, HEIGHT, LINESPACE)];
    for row in range(LAST_ROW + 1):
        for column in range(LAST_COLUMN + 1):
            neighbour_counts[row][column] = check_neighbour(row, column);

    for row in range(LAST_ROW + 1):
        for column in range(LAST_COLUMN + 1):

            count = neighbour_counts[row][column]

            if count < 2:
                kill_cell(row,column);

            elif count > 3:
                kill_cell(row, column);

            elif count == 3:
                populate_cell(row, column);



def render():

    for row in range(LAST_ROW + 1):
        for column in range(LAST_COLUMN + 1):
            if is_cell_alive(row, column):
                _, x, y = game_env[row][column]
                pg.draw.rect(win, BLACK, (x, y, LINESPACE-1, LINESPACE-1));


    
        
    








def main():
    clock = pg.time.Clock();
    run = True;

    while run:
        clock.tick(60);
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False;


        win.fill(WHITE);
        draw_grid(win, BLACK, LINESPACE);
        render();
        implement_rules();

        
        
        pg.display.flip();

    pg.quit();

if __name__ == '__main__':
    main();
