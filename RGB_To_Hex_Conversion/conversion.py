def rgb(r, g, b):
    # Ensure the values are within the valid range
    r = min(max(r, 0), 255)
    g = min(max(g, 0), 255)
    b = min(max(b, 0), 255)
    
    # Convert decimal values to hexadecimal and format as a 6-character string
    hex_value = '{:02X}{:02X}{:02X}'.format(r, g, b)
    
    return hex_value
