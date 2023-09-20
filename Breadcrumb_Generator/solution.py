def generate_bc(url, separator):
    # Define words to ignore while acronymizing
    ignore_words = ["the", "of", "in", "from", "by", "with", "and", "or", "for", "to", "at", "a"]

    # Split the URL by '/' and remove empty elements
    path_components = [component for component in url.split('/') if component]

    # Handle the root/home case
    if not path_components:
        return '<span class="active">HOME</span>'

    # Initialize the breadcrumb with the HOME element
    breadcrumb = ['<a href="/">HOME</a>']

    # Initialize the path to the root
    path = '/'

    # Process each path component
    for component in path_components:
        # Remove common extensions
        if '.' in component:
            component, ext = component.split('.', 1)
            if ext in ("html", "htm", "php", "asp"):
                component = component.rsplit('-', 1)[0]

        # Handle "index.something" as if it's not there
        if component.startswith("index."):
            continue

        # Remove anchors and parameters
        if '#' in component:
            component = component.split('#', 1)[0]
        if '?' in component:
            component = component.split('?', 1)[0]

        # Acronymize long components
        component = ''.join(word[0] for word in component.split('-') if word not in ignore_words)

        # Shorten if longer than 30 characters
        if len(component) > 30:
            words = component.split('-')
            component = '-'.join(word[0] for word in words if word not in ignore_words)

        # Build the path
        path += component + '/'

        # Create the breadcrumb element
        breadcrumb.append(f'<a href="{path}">{component.upper()}</a>')

    # Set the last element as active
    breadcrumb[-1] = f'<span class="active">{breadcrumb[-1]}</span>'

    # Join the breadcrumb elements with the separator
    return separator.join(breadcrumb)

# Test cases
print(generate_bc("mysite.com/pictures/holidays.html", " : "))
print(generate_bc("www.codewars.com/users/GiacomoSorbi", " / "))
