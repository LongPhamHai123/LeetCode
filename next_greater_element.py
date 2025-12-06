# 
# def next_greater_element(arr):
#     n = len(arr)
#     result = [-1] * n
#     stack = []
#     for i in range(n - 1 , -1, -1):
#         while stack and stack[-1] <= arr[i]:
#             stack.pop()
#         if stack:
#             result[i] = stack[-1]
#         stack.append(arr[i])
#     return result

def next_greater_element(arr):
    n = len (arr)
    result = [-1] * n
    stack = []
    for i in range(n-1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])
    return result
        # for j in range(i + 1, n):
        #     if arr[j] > arr[i]:
        #         result[i] = arr[j]
        #         break

if __name__ == "__main__":
    arr = [4, 5, 2, 10, 8]
    print("Next Greater Elements:", next_greater_element(arr))  # Output: [5, 10, 10, -1, -1]