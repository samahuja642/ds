#include<iostream>
using namespace std;
void print_array(int arr[],int n){
    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}
void insertion_sort(int arr[],int n){
    for(int i=1;i<n;i++){
        int j=i-1;
        int temp = i;
        while(j>=0 && arr[temp]<arr[j]){
            swap(arr[temp],arr[j]);
            temp--;
            j--;
        }
    }
}
int main(){
    int arr[]={1,6,36,7,9,0};
    int n = sizeof(arr)/sizeof(arr[0]);
    insertion_sort(arr,n);
    print_array(arr,n);
    return 0;
}