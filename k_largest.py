import heapq

def k_largest_elements(arr, k):
    if k <= 0:
        return []
    if k >= len(arr):
        return arr
    min_heap = []
    for num in arr:
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        else:
            if num > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, num)
    return min_heap
arr = [3, 2, 1, 5, 6, 4]
k = 2
print(k_largest_elements(arr, k))  # [5,6]
    # return heapq.nlargest(k, nums)