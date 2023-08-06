import re

def pig_it(text):
    words = text.split()
    result = []

    for word in words:
        if re.match(r'[a-zA-Z]', word):
            new_word = word[1:] + word[0] + 'ay'
            result.append(new_word)
        else:
            result.append(word)
    
    return ' '.join(result)
