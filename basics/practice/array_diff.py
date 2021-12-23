# Link :- 
def array_diff(a, b):
    ls = a[::]
    for i in a:
        if i in b:
            ls.remove(i)
    return ls
    