def compare(string):
    if '>' in string:
        d, d1 = string.split('>')
        return int(d) > int(d1)
    if '<' in string:
        d, d1 = string.split('<')
        return int(d) < int(d1)

