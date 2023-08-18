def validate_battlefield(field):
    def is_valid_ship(x, y, length, direction):
        if direction == 'horizontal':
            for i in range(x, x + length):
                if i >= 10 or field[y][i] != 1:
                    return False
        else:
            for i in range(y, y + length):
                if i >= 10 or field[i][x] != 1:
                    return False
        return True
    
    ship_lengths = {4: 1, 3: 2, 2: 3, 1: 4}
    ship_counts = {1: 0, 2: 0, 3: 0, 4: 0}
    
    for y in range(10):
        for x in range(10):
            if field[y][x] == 1:
                if y == 0 or field[y - 1][x] == 0:
                    # Check horizontal ship
                    length = 1
                    while x + length < 10 and field[y][x + length] == 1:
                        length += 1
                    if length not in ship_lengths:
                        return False
                    ship_counts[length] += 1
                    if ship_counts[length] > ship_lengths[length]:
                        return False
                    if not is_valid_ship(x, y, length, 'horizontal'):
                        return False
                elif x == 0 or field[y][x - 1] == 0:
                    # Check vertical ship
                    length = 1
                    while y + length < 10 and field[y + length][x] == 1:
                        length += 1
                    if length not in ship_lengths:
                        return False
                    ship_counts[length] += 1
                    if ship_counts[length] > ship_lengths[length]:
                        return False
                    if not is_valid_ship(x, y, length, 'vertical'):
                        return False
    
    return ship_counts == ship_lengths
