ls = [1,0,36,7,0,0]
def insertion_sort(ls):
    for i in range(1,len(ls),1):
        j=i-1
        temp = i
        while(j>=0 and ls[temp]<ls[j]):
            ls[temp],ls[j] = ls[j],ls[temp]
            j-=1
            temp -= 1
insertion_sort(ls)
for i in ls:
    print(i,end=" ")