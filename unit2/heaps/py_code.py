def max_heapify(heap,n,x):
    l = heap[2*x] if 2*x<=n else heap[0]
    r = heap[2*x+1] if 2*x+1<=n else heap[0]
    largest = 0
    if heap[x]>l and heap[x]>r:
        return
    elif l>r and l>heap[x]:
        l,heap[x] = heap[x],l
        largest = l
        print(l)
        print(heap[x])
    else:
        r,heap[x] = heap[x],r
        largest = r
    max_heapify(heap,n,largest)
heap = [-1,6,1,4,2,5,3]
n = len(heap)-1
x = 1
max_heapify(heap,n,x)
print(heap)
