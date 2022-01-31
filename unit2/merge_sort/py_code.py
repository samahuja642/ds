ls = [1,2,7,36,9,0]
def merge(a,b):
    lasta = 0
    lastb = 0
    c = []
    while(lasta==len(a) and lastb==len(b)):
        if(lastb == len(b) or (lasta != len(a) and a[lasta]<=b[lastb])):
            c.append(a[lasta])
            lasta+=1
        else:
            c.append(b[lastb])
            lastb+=1
    return c
def merge_sort(ls):
    if(len(ls)==1):
        return ls
    a = merge_sort(ls[:len(ls)//2])
    b = merge_sort(ls[len(ls)//2:])
    c = merge(a,b)
    return c
ls = merge([1,3],[2,4])
# ls = merge_sort(ls)
for i in ls:
    print(i,end=" ")
