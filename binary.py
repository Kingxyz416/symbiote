def binary(x, target):
    n=len(x)
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if x[mid]==target:
            return mid
        elif x[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1
