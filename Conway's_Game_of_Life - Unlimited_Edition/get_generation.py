def get_generation(cells, generations):
    def get_neighbors(x, y):
        # Generate the coordinates of all 8 neighbors
        neighbors = [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1),
                     (x, y - 1), (x, y + 1),
                     (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)]
        return neighbors

    def count_live_neighbors(x, y, current_gen):
        # Count the number of live neighbors for a cell
        live_count = 0
        for nx, ny in get_neighbors(x, y):
            if 0 <= nx < len(current_gen) and 0 <= ny < len(current_gen[0]):
                if current_gen[nx][ny] == 1:
                    live_count += 1
        return live_count

    def apply_rules(x, y, current_gen):
        live_neighbors = count_live_neighbors(x, y, current_gen)
        if current_gen[x][y] == 1:
            # Cell is currently alive
            if live_neighbors < 2 or live_neighbors > 3:
                return 0  # Cell dies due to underpopulation or overcrowding
            else:
                return 1  # Cell survives
        else:
            # Cell is currently dead
            if live_neighbors == 3:
                return 1  # Cell becomes alive due to reproduction
            else:
                return 0  # Cell remains dead

    for _ in range(generations):
        next_gen = [[0] * len(cells[0]) for _ in range(len(cells))]
        for i in range(len(cells)):
            for j in range(len(cells[0])):
                next_gen[i][j] = apply_rules(i, j, cells)
        cells = next_gen

    return cells
