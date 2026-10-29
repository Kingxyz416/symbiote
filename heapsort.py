def heapsort(a,n,i):
    lar=i
    left=2*i+1
    right=2*i+2
    if left<n and a[left]>a[lar]:
        lar=left
    if right<n and a[right]>a[lar]:
        lar=right
    if lar!=i:
        a[i],a[lar]=a[lar],a[i]
        heapsort(a,n,lar)


def heap_sort(arr):
    n=len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapsort(arr,n,i)
    for i in range(n-1, 0, -1):
        arr[0],arr[i]=arr[i],arr[0]
        heapsort(arr,i,0)
    return arr


if __name__ == "__main__":
    sample = [12, 11, 13, 5, 6, 7]
    print("Original:", sample)
    print("Sorted:", heap_sort(sample))
    
