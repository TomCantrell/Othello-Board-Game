"""
Convert position string to indicies
"""
def strtoIndex(s):
    lst=list(s.strip())
    for _ in s.strip():
        if _==' ':
            lst.remove(_)
    if lst[0].isdigit()==True:
        lst=list(reversed(lst))
    if len(lst)!=2:
        raise ValueError("Not valid")
    col=["a","b","c","d","e","f","g","h"]
    row=[1,2,3,4,5,6,7,8]
    k=0
    c=-1
    for i in col:
        k+=1
        if i==lst[0].lower():
            c=k-1
    if c==-1:
        raise ValueError("Not a Valid move")
    l=0
    for j in row:
        l+=1
        if j==int(lst[1]):
            r=l-1             
    return (r,c)