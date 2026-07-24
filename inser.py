a=[3,4,6,8,2,11,67,90,43]
n=len(a)
for i in range (1,n):
    b=a[i]
    j=i-1
    while j>=0 and a[j]>b:
        a[j+1]=a[j]
        j-=1

    a[j+1]=b
print(a)


