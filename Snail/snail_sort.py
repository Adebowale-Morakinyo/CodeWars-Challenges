def snail(snail_map):
    result = []
    
    while snail_map:
        result += snail_map[0]
        snail_map.pop(0)
        
        if snail_map and snail_map[0]:
            result += [row.pop() for row in snail_map]
            
        if snail_map:
            result += snail_map[-1][::-1]
            snail_map.pop()
        
        if snail_map and snail_map[0]:
            result += [row.pop(0) for row in snail_map[::-1]]
    
    return result
