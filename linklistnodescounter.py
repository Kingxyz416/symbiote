def find_largest_smallest(arr):
    largest = arr[0]
    smallest = arr[0]
 
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
        if arr[i] < smallest:
            smallest = arr[i]
 
    return largest, smallest
 
 
arr = [12, 45, 2, 89, 33, 7]
a = find_largest_smallest(arr)
print("Largest element:", a)

