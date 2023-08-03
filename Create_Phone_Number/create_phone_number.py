def create_phone_number(n):
    # Convert the list of integers to a string
    num_str = ''.join(map(str, n))
    
    # Format the phone number
    return f"({num_str[:3]}) {num_str[3:6]}-{num_str[6:]}"

