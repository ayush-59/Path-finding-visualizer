import pygame

YELLOW = (255, 255, 0)

# heuristic function which estimates distance of goal from given node
def heuristic(pos1, pos2):
    y1, x1 = pos1
    y2, x2 = pos2
    return abs(x1-x2) + abs(y1-y2)

# function that returns node in open list having lowest f_score
def choose_best_node(open_list):
    best_node = open_list[0]

    for spot in open_list:
        if spot['f_score'] < best_node['f_score']:
            best_node = spot

    return best_node

def is_common(list1, list2):
    for ele in list1:
        if any(ele['pos'] == item['pos'] for item in list2):
            return ele
    return None

# Returns Path found using backtracking
def get_path(draw, current_from_start, current_from_goal, start, goal, grid):
    first_half_path = []

    current = current_from_start
    while True:
        if current == None:
            break
        col, row = current.get_pos()
        if current != start and current != goal:
            grid[row][col].set_color(YELLOW)
        first_half_path.append(current.get_pos())
        if current == start:
            break
        current = current.get_prev()
        draw()
        pygame.display.update()

    second_half_path = []

    current = current_from_goal
    while True:
        if current == None:
            break
        col, row = current.get_pos()
        if current != goal and current != goal:
            grid[row][col].set_color(YELLOW)
        second_half_path.append(current.get_pos())
        if current == goal:
            break
        current = current.get_prev()
        draw()
        pygame.display.update()
    return second_half_path


def run_algo(draw, grid, start, goal):
    open_list_from_start = []
    open_list_from_goal = []
    
    g_start = 0
    h_start = heuristic(start.get_pos(), goal.get_pos())
    f_start = g_start + h_start

    current_from_start = {'pos': start.get_pos(), 'f_score': f_start, 'g_score': g_start, 'h_score': h_start}
    open_list_from_start.append(current_from_start)

    g_goal = 0
    h_goal = heuristic(goal.get_pos(), start.get_pos())
    f_goal = g_goal + h_goal

    current_from_goal = {'pos': goal.get_pos(), 'f_score': f_goal, 'g_score': g_goal, 'h_score': h_goal}
    open_list_from_goal.append(current_from_goal)
    sol_found = False
    while not sol_found:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        open_list_from_start.remove(current_from_start)
        col1, row1 = current_from_start['pos']
        grid[row1][col1].set_visited()
        neighbours = grid[row1][col1].get_neighbours()


        for node in neighbours:
            if node.has_visited():
                continue
            if len(list(filter(lambda ele: ele['pos'] == node.get_pos(), open_list_from_start))) > 0:
                continue
            g = current_from_start['g_score'] + 1
            h = heuristic(node.get_pos(), goal.get_pos())
            f = g + h
            node.set_open()
            if node.get_prev():
                sol_found = True
                current_from_start = grid[row1][col1]
                current_from_goal = node.get_prev()
                node.set_color(YELLOW)
                break
            node.set_prev(grid[row1][col1])
            node_info = {'pos': node.get_pos(), 'f_score': f, 'g_score': g, 'h_score': h}
            open_list_from_start.append(node_info)

        if sol_found:
            break

        open_list_from_goal.remove(current_from_goal)
        col2, row2 = current_from_goal['pos']
        grid[row2][col2].set_visited()
        neighbours = grid[row2][col2].get_neighbours()


        for node in neighbours:
            if node.has_visited():
                continue
            if len(list(filter(lambda ele: ele['pos'] == node.get_pos(), open_list_from_goal))) > 0:
                continue
            g = current_from_goal['g_score'] + 1
            h = heuristic(node.get_pos(), start.get_pos())
            f = g + h
            node.set_open()
            if node.get_prev():
                sol_found = True
                current_from_start = node.get_prev()
                current_from_goal = grid[row2][col2]
                node.set_color(YELLOW)
                break
            node.set_prev(grid[row2][col2])
            node_info = {'pos': node.get_pos(), 'f_score': f, 'g_score': g, 'h_score': h}
            open_list_from_goal.append(node_info)

        if sol_found:
            break

        draw()
        pygame.display.update()
        if not open_list_from_start or not open_list_from_goal:
            break
        current_from_start = choose_best_node(open_list_from_start)
        current_from_goal = choose_best_node(open_list_from_goal)



    if not sol_found:
        print("No Valid Path")
    else:
        path = get_path(draw, current_from_start, current_from_goal, start, goal, grid)
        print(path)
