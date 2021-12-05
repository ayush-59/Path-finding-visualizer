import pygame
import random

YELLOW = (255, 255, 0)


# Returns Path found using backtracking
def get_path(draw, start, goal, grid, path):
    current = path.pop()
    while len(path) > 0:
        col, row = current
        if current != start.get_pos() and current != goal.get_pos():
            grid[row][col].set_color(YELLOW)
        if current == start:
            break
        current = path.pop()
        draw()
        pygame.display.update()
    return path

def search_neighbour(draw, grid, current, goal, path, path_found):
    draw()
    pygame.display.update()
    if current.get_pos() == goal.get_pos():
        return True
    col, row = current.get_pos()
    grid[row][col].set_visited()
    neighbours = grid[row][col].get_neighbours()
    while len(neighbours) > 0:
        node  = random.choice(neighbours)
        neighbours.remove(node)
        if node.has_visited():
            continue
        path.append(node.get_pos())
        path_found = search_neighbour(draw, grid, node, goal, path, path_found)
        if path_found:
            return path_found
        path.pop()
    return path_found

def run_algo(draw, grid, start, goal):
    path = []
    path_found = search_neighbour(draw, grid, start, goal, path, False)
    if path_found:
        get_path(draw, start, goal, grid, path)
    else:
        print("No path found!")
    # st = Stack()
    # current = start
    # st.push([current, 0])
    #
    # while current.get_pos() != goal.get_pos():
    #     if st.peek()[1] >= 7:
    #         current = st.pop()[0]
    #     else:
    #         [current, i] = st.pop()
    #         st.push([current, i+1])
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #
    #     open_list.remove(current)
    #
    #     col, row = current['pos']
    #     grid[row][col].set_visited()
    #     neighbours = grid[row][col].get_neighbours()
    #
    #     for node in neighbours:
    #         if node.has_visited():
    #             continue
    #         if len(list(filter(lambda ele: ele['pos'] == node.get_pos(), open_list))) > 0:
    #             continue
    #         g = current['g_score'] + 1
    #         h = heuristic(node.get_pos(), goal.get_pos())
    #         f = g + h
    #         node.set_open()
    #         node.set_prev(grid[row][col])
    #         node_info = {'pos': node.get_pos(), 'f_score': f, 'g_score': g, 'h_score': h}
    #         open_list.append(node_info)
    #
    #
    #     draw()
    #     pygame.display.update()
    #     if not open_list:
    #         break
    #     current = choose_best_node(open_list)



    # if current['pos'] != goal.get_pos():
    #     print("No Valid Path")
    # else:
    #     path = get_path(draw, start, goal, grid)
    #     print(path)
