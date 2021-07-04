"""
Convert indicies to position string
"""
def indextostr(t):
    col = ["a","b","c","d","e","f","g","h"]
    return col[t[1]]+str(t[0]+1)