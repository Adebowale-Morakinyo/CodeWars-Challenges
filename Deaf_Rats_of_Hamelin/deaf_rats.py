def count_deaf_rats(town_square):
    piper_position = None
    deaf_rats = 0
    
    for row_index, row in enumerate(town_square):
        for col_index, cell in enumerate(row):
            if cell == 'P':
                piper_position = (row_index, col_index)
    
    if piper_position is None:
        return 0  # The Piper is not present, so there are no deaf rats
    
    for row_index, row in enumerate(town_square):
        for col_index, cell in enumerate(row):
            if cell != ' ' and cell != 'P':
                rat_position = (row_index, col_index)
                distance = (piper_position[0] - rat_position[0])**2 + (piper_position[1] - rat_position[1])**2
                if distance > 0:
                    deaf_rats += 1
    
    return deaf_rats
