import heapq

def kth_largest(a, k):
    if k < 1 or k > len(a):
        raise ValueError("k out of range")

    heap = []
    for x in a:
        if len(heap) < k:
            heapq.heappush(heap, x)
        elif x > heap[0]:
            heapq.heapreplace(heap, x)   # pop root + push x in one step

    return heap[0]


if __name__ == "__main__":
    print(kth_largest([3, 2, 1, 5, 6, 4], 2))           
    print(kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  