# def max_subarray_sum(arr,k: int) -> int:
#     n = len(arr)
#     if n == 0 or k <= 0 or k > n:
#         return 0
#     max_sum = float('-inf')
#     current_sum = sum(arr[:k])
#     max_sum = max(max_sum, current_sum)
#     for i in range(k, n):
#         current_sum += arr[i] - arr[i - k]
#         max_sum = max(max_sum, current_sum)
#     return max_sum
# def max_subarray_sum(arr,k: int) -> int:
#     n = len(arr)
#     max_sum = float('-inf')
#     for i in range(n - k + 1):
#         current_sum = 0 
#         for j in range (k):
#             current_sum += arr[i + j]
#         if current_sum > max_sum:
#             max_sum = current_sum
#             max_start_index = i
#     return arr[max_start_index:max_start_index + k], max_sum
# def max_subarray_sum(arr,k: int) -> int:
#     n = len(arr)
#     if n == 0 or k <= 0 or k > n:
#         return 0
#     max_sum = float('-inf')
#     current_sum = sum(arr[:k])
#     max_sum = max(max_sum, current_sum)
#     for i in range(k,n):
#         current_sum += arr[i] - arr[i - k]
#         max_sum = max(max_sum, current_sum)
#     return max_sum
def max_subarray_sum_sliding_window(arr,k: int) -> int:
    n = len(arr)
    max_sum = float('-inf')
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(n-k):
        window_sum = window_sum - arr[i] + arr[i + k]
        # max_sum = max(max_sum, current_sum)
        if window_sum > max_sum:
            max_sum = window_sum
            max_start_index = i + 1
    return max_sum
if __name__ == "__main__":
    arr = [2, 1, 5, 1, 3, 2]
    k = 3
    result = max_subarray_sum_sliding_window(arr, k)
    print(f"Maximum sum of a subarray of size {k} is: {result}")  # Output: 9