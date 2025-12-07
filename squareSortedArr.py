#leetcode 977
def sortedSquares(nums: list[int]) -> list[int]:
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    pos = n - 1
    while left <= right:
        # left_square = nums[left] ** 2
        # right_square = nums[right] ** 2

        if abs(nums[left]) > abs(nums[right]):
            result[pos] = nums[left] ** 2
            left += 1
        else:
            result[pos] = nums[right] ** 2
            right -= 1
        pos -= 1
    return result
def sortedSquares2(self, nums: list[int]) -> list[int]:
    res = [0] * len(nums)
    left, right = 0, len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            res[i] = nums[left] ** 2
            left += 1
        else:
            res[i] = nums[right] ** 2
            right -= 1
    return res
if __name__ == "__main__":
    nums = [-7, -3, 2, 3, 11]
    print("Sorted Squares:", sortedSquares(nums))