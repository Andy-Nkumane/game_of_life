import turtle
import time

BLOCK_DIMENSION = 20

turtle.hideturtle()
screen = turtle.Screen()
turtle.pencolor("gray")

game_grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0],
]

neighbours = [
    (0, 1),  # right
    (0, -1),  # left
    (-1, 0),  # top
    (1, 0),  # bottom
    (-1, -1),  # top left
    (1, -1),  # bottom left
    (1, 1),  # bottom right
    (-1, 1),  # top right
]


def draw_obstacle(obstacle, color="white"):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(obstacle)
    turtle.pendown()
    turtle.goto((obstacle[0], obstacle[1]))
    turtle.goto((obstacle[0] + BLOCK_DIMENSION, obstacle[1]))
    turtle.goto((obstacle[0] + BLOCK_DIMENSION, obstacle[1] + BLOCK_DIMENSION))
    turtle.goto((obstacle[0], obstacle[1] + BLOCK_DIMENSION))
    turtle.goto((obstacle[0], obstacle[1]))
    turtle.penup()
    turtle.end_fill()


def get_obstacles():
    """returns the list of obstacles."""
    obstacles = []
    constant = len(game_grid) // 2
    indexes = range(-constant, constant + 1)
    for i_row, row in enumerate(game_grid):
        for i, v in enumerate(row):
            if not row[i]:
                coordinates = (
                    get_coordinate(i, indexes),
                    get_coordinate(i_row, indexes[::-1]),
                )
                if not None in coordinates:
                    obstacles.append(coordinates)
    return obstacles


def get_grid():
    grid = []
    grid_matrix = []
    constant = len(game_grid) // 2
    indexes = range(-constant, constant + 1)
    for i_row, row in enumerate(game_grid):
        row_list = []
        for i, v in enumerate(row):
            coordinates = (
                get_coordinate(i, indexes),
                get_coordinate(i_row, indexes[::-1]),
            )
            row_list.append(coordinates)
        grid.extend(row_list)
        grid_matrix.append(row_list)
    return grid, grid_matrix


def get_coordinate(r_value, indexes):
    try:
        coordinate = indexes[r_value] * BLOCK_DIMENSION - (BLOCK_DIMENSION // 2)
        if indexes[r_value] > 0:
            coordinate -= 1
        return coordinate
    except IndexError:
        pass


def check_neighbours(row, col):
    neighbour_count = 0
    for neighbour in neighbours:
        try:
            new_row = row + neighbour[0]
            new_col = col + neighbour[1]
            if game_grid[new_row][new_col] == 1:
                neighbour_count += 1
        except IndexError:
            continue
    return neighbour_count


def is_death(neighbour_count):
    if neighbour_count <= 1 or neighbour_count >= 4:
        return True
    return False


def is_birth(neighbour_count):
    if neighbour_count == 3:
        return True
    return False


def game_of_life():
    death_list = []
    birth_list = []

    for row in range(len(game_grid)):
        for col in range(len(game_grid)):
            neighbour_count = check_neighbours(row, col)
            if game_grid[row][col] == 1:
                if is_death(neighbour_count):
                    death_list.append((row, col))
            else:
                if is_birth(neighbour_count):
                    birth_list.append((row, col))

    update_grid(death_list, birth_list)


def update_grid(death_list, birth_list):
    for row, col in death_list:
        game_grid[row][col] = 0
    for row, col in birth_list:
        game_grid[row][col] = 1


grid_coord, grid_matrix = get_grid()

turtle.tracer(0)
for block in grid_coord:
    if None not in block:
        draw_obstacle(block, "black")

turtle.tracer(4, 0)
for obstacle in get_obstacles():
    draw_obstacle(obstacle)

for _ in range(20):
    game_of_life()
    time.sleep(0.3)
    turtle.clear()
    turtle.tracer(0)
    for block in grid_coord:
        if None not in block:
            draw_obstacle(block, "black")

    turtle.tracer(4, 0)
    for obstacle in get_obstacles():
        draw_obstacle(obstacle)

turtle.done()
