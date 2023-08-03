def generate_hashtag(s):
    # Remove leading and trailing whitespaces and split the string into words
    words = s.strip().split()
    
    # Check if the input string is empty or results in an empty list of words
    if not words:
        return False
    
    # Capitalize the first letter of each word and join them with an empty space
    result = '#' + ''.join(word.capitalize() for word in words)
    
    # Check if the final hashtag is longer than 140 characters
    if len(result) > 140:
        return False
    
    return result
