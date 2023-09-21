def generate_bc(url, separator):
    # Define words to ignore during acronymization
    ignore_words = ["the", "of", "in", "from", "by", "with", "and", "or", "for", "to", "at", "a"]

    # Parse the URL to extract components
    components = url.split("/")

    # Remove empty and redundant elements
    components = [c for c in components if c != "" and c != "index"]

    # Initialize the breadcrumb trail with the HOME element
    breadcrumb = ['<a href="/">HOME</a>']

    # Initialize the current path
    current_path = '/'

    for component in components:
        # Handle acronymization for long components
        if len(component) > 30:
            words = [word for word in component.split('-') if word not in ignore_words]
            acronym = ''.join(word[0].upper() for word in words)
            component = acronym

        # Update the current path
        current_path += component + '/'

        # Check if it's the last element
        if component.endswith(('.html', '.htm', '.php', '.asp')):
            breadcrumb.append('<span class="active">' + component[:-5].upper() + '</span>')
        else:
            breadcrumb.append('<a href="' + current_path + '">' + component.upper() + '</a>')

    # Join the breadcrumb elements with the separator
    result = separator.join(breadcrumb)

    return result
