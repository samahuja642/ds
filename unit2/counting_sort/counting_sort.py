def counting_sort(ls):
    pos = [0 for temp in range(10)]
    sum = len(ls)
    output = [0 for temp in range(len(ls))]
    for i in ls:
        pos[i] += 1
    for i in range(len(ls)-1,0,-1):
        sum -= pos[i]
        pos[i] = sum
    for i in ls:
        output[pos[i]]=i
        pos[i]+=1
    return output
if __name__ == '__main__':
    ls = [2,6,1,3,5,3,2,6,2]
    print(counting_sort(ls))
