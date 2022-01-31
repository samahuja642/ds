def counting_sort(ls,div):
    pos = [0 for temp in range(10)]
    sum = len(ls)
    output = [0 for temp in range(len(ls))]
    for i in ls:
        i = (i//div)%10
        pos[i] += 1
    for i in range(9,-1,-1):
        sum -= pos[i]
        pos[i] = sum
    for i in ls:
        j = int(i)
        i = (i//div)%10
        output[pos[i]]=j
        pos[i]+=1
    for i in range(len(ls)):
        ls[i] = output[i]
def radix_sort(ls):
    m = -1
    for i in ls:
        m = max(i,m)
    div = 1
    while m/div>0:
        counting_sort(ls,div)
        div *= 10
ls = [123,253,65,7,80,68]
radix_sort(ls)
print(ls)
