def expand(cs, to_append=""):
    expanded = ""
    
    if "[" not in cs:
        return cs
    
    for i in range(len(cs)):
        if cs[i].isnumeric():
            no = int(cs[i])
        elif cs[i].isalpha():
            to_append += cs[i] 
        elif cs[i] == "[":
            return to_append + no * expand(cs[i+1:-1])

    return expanded

expand("2[a2[b]]")