def heading(text, level=1):
    c = '#'
    if level < 1:
        pass
    elif level > 6:
        c = '#' * 6
    else:
        c = c * level

    return f'{c} {text}'
