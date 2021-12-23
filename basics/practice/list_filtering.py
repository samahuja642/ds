# Link :- https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python
def filter_list(l):
    ls = []
    for i in l:
        if type(i)!=type('str'):
            ls.append(i)
    return ls  
ls = [1,2,'a','b']
fls = filter_list(ls)