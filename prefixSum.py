class Solution():
    def prefixSum(self, arr) -> list[int]:
      n = len(arr)
      prefix = [0] * n
      print("prefix init:", prefix)
      prefix[0] = arr[0]
      for i in range(1, n):
          prefix[i] = prefix[i - 1] + arr[i]
      return prefix
    def subarraySum(self, prefix, l: int, r: int) -> int:
        if l == 0:
            return prefix[r]
        return prefix[r] - prefix[l - 1]
# def prefixSum(arr) -> list[int]:
#     n = len(arr)
#     prefix = [0] * n
#     print("prefix init:", prefix)
#     prefix[0] = arr[0]
#     for i in range(1, n):
#         prefix[i] = prefix[i - 1] + arr[i]
#     return prefix
if __name__ == "__main__":
    a = Solution()
    arr = [2, 4, 5, 7, 1]
    prefix = a.prefixSum(arr)
    # prefix = prefixSum(arr)
    sub_sum = a.subarraySum(prefix, 1, 3)
    print("Subarray Sum from index 1 to 3:", sub_sum)  # Output: 16
    print("Prefix:", prefix)     