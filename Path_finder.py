import pygame
from node import Node
import a_star_algo as astar
import bidirectional_a_star_algo as bi_astar
import djikstraz_algo as djikstraz
import dfs_algo as dfs

GRAY = (128,128,128)

def create_grid(rows, cols, width):
    grid = []
    for row in range(rows):
        current_row = []
        for col in range(cols):
            node = Node(col, row, width, rows)
            current_row.append(node)
        grid.append(current_row)
    return grid

def display_grid(surface, grid):
    for row in grid:
        for node in row:
            node.draw_node(surface)

def get_node_pos(pos, node_width):
    y, x = pos
    x = int(x//node_width)
    y = int(y//node_width)
    return x, y

if __name__ == "__main__":
    WIDTH = 800

    WIN = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("A* Path Finding Algorithm")

    ROWS = 20
    node_width = WIDTH / ROWS
    grid = create_grid(ROWS, ROWS, node_width)
    start = None
    end = None
    run = True
    started = False

    while run:
        WIN.fill(GRAY)
        display_grid(WIN, grid)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    start = None
                    end = None
                    started = False
                    grid = create_grid(ROWS, ROWS, node_width)
            if started:
                continue

            if pygame.mouse.get_pressed()[0]:   #left mouse button
                pos = pygame.mouse.get_pos()
                row, col = get_node_pos(pos, node_width)
                node = grid[row][col]

                if not start and node != end:
                    start = node
                    start.set_start()
                elif not end and node != start:
                    end = node
                    end.set_end()
                elif node != start and node != end:
                    node.set_wall()

            elif pygame.mouse.get_pressed()[2]: #right mouse button
                pos = pygame.mouse.get_pos()
                row, col = get_node_pos(pos, node_width)
                node = grid[row][col]

                if node == start:
                    node.remove_start()
                    start = None
                elif node == end:
                    node.remove_end()
                    end = None
                else:
                    node.remove_wall()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 and start != None and end != None:
                    started = True
                    for row in grid:
                        for node in row:
                            node.update_neighbours(grid)
                    astar.run_algo(lambda: display_grid(WIN, grid), grid, start, end)

                elif event.key == pygame.K_2 and start != None and end != None:
                    started = True
                    for row in grid:
                        for node in row:
                            node.update_neighbours(grid)
                    bi_astar.run_algo(lambda: display_grid(WIN, grid), grid, start, end)

                elif event.key == pygame.K_3 and start != None and end != None:
                    started = True
                    for row in grid:
                        for node in row:
                            node.update_neighbours(grid)
                    djikstraz.run_algo(lambda: display_grid(WIN, grid), grid, start, end)

                elif event.key == pygame.K_4 and start != None and end != None:
                    started = True
                    for row in grid:
                        for node in row:
                            node.update_neighbours(grid)
                    dfs.run_algo(lambda: display_grid(WIN, grid), grid, start, end)


    pygame.quit()
