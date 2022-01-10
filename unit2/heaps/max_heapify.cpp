#include<iostream>
#include<algorithm>
using namespace std;
int left(int i,int n){
    return 2*i<=n?2*i:0;
}
int right(int i,int n){
    return 2*i+1<=n?2*i+1:0;
}
void max_heapify(int heap[],int n,int x){
    int l = left(x,n);
    int r = right(x,n);
    int largest = 0;
    if(heap[r]>heap[l] && heap[x]<heap[r]){
        largest = r;
    }
    else if(heap[l]<heap[x] && heap[r]<heap[x]){
        return;
    }
    else{
        largest = l;
    }
    int temp = heap[x];
    heap[x]=heap[largest];
    heap[largest]=temp;
    max_heapify(heap,n,largest);
}
void print(int heap[],int n){
    for(int i=1;i<=n;i++){
        cout<<heap[i]<<" ";
    }
    cout<<endl;
}
void Build_Heap(int heap[],int n){
    for(int i=n/2;i>=1;i--){
        max_heapify(heap,n,i);
    }
}
void heap_sort(int arr[],int n){
    Build_Heap(arr,n);
    int len = n;
    for(int i=1;i<=n;i++){
        swap(arr[1],arr[len]);
        len--;
        max_heapify(arr,len,1);
    }
}
int main(){
    int heap[] = {-1,1,6,4,2,5,3};
    int n = sizeof(heap)/sizeof(heap[0])-1;
    int x = 1;
    max_heapify(heap,n,x);
    print(heap,n);
    int heap2[]={-1,7,2,9,5,4,8,0};
    n = sizeof(heap2)/sizeof(heap2[0])-1;
    Build_Heap(heap2,n);
    print(heap2,n);
    int arr[]={-1,8,9,1,6,2,3,5};
    n = sizeof(arr)/sizeof(arr[0])-1;
    print(arr,n);
    heap_sort(arr,n);
    print(arr,n);
    return 0;
}