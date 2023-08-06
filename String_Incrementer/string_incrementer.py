import re

def increment_string(strng):
    match = re.search(r'(\d*)$', strng)
    
    if match:
        num_str = match.group(0)
        if num_str:
            num = int(num_str) + 1
            return strng[:-len(num_str)] + str(num).zfill(len(num_str))
    
    return strng + '1'
