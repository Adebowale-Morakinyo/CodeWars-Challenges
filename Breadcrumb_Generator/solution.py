def generate_bc(url, separator):
    # Define words to ignore during acronymization
    ignore_words = ["the", "of", "in", "from", "by", "with", "and", "or", "for", "to", "at", "a"]

    # Split the URL into components, ignoring query parameters and anchors
    url_parts = url.split('?')[0].split('#')[0].split('/')

    # Remove empty and redundant elements
    url_parts = [part for part in url_parts if part and part != "index"]

    # Initialize the breadcrumb trail with the HOME element
    breadcrumb = ['<a href="/">HOME</a>']

    # Initialize the current path
    current_path = '/'

    for part in url_parts:
        # Handle acronymization for long components
        if len(part) > 30 and part != url_parts[-1]:
            words = [word for word in part.split('-') if word not in ignore_words]
            acronym = ''.join(word[0].upper() for word in words)
            part = acronym

        # Update the current path
        current_path += part + '/'

        # Check if it's the last element
        if part == url_parts[-1]:
            # Check for common extensions
            if any(part.endswith(ext) for ext in ['.html', '.htm', '.php', '.asp']):
                part = part.rsplit('.', 1)[0]  # Remove extension

        # Check if it's the last element (again)
        if part == url_parts[-1]:
            breadcrumb.append('<span class="active">' + part.upper() + '</span>')
        else:
            breadcrumb.append('<a href="' + current_path + '">' + part.upper() + '</a>')

    # Join the breadcrumb elements with the separator
    result = separator.join(breadcrumb)

    return result
