def wrap(string, max_width):
    a=list(textwrap.wrap(string,max_width))
    return '\n'.join(a)
