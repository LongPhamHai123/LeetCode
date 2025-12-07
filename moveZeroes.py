#leetcode-283
# def moveZeroes(nums: list[int]) -> None:
#     """
#     Do not return anything, modify nums in-place instead.
#     """
#     last_non_zero_index = 0
#     for i in range(len(nums)):
#         if nums[i] != 0:
#             nums[last_non_zero_index] = nums[i]
#             last_non_zero_index += 1
#     for i in range(last_non_zero_index, len(nums)):
#         nums[i] = 0
def moveZeroses(num: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    left = 0
    # for right in range(len(num)):
    for right in range(len(num)):
        if num[right] != 0:
            num[right] , num[left] = num[left], num[right]
            left += 1 # left luôn chỉ đến vị trí tiếp theo cần đặt số khác 0.
    return num
if __name__ == "__main__":
    nums = [0,1,0,3,12]
    moveZeroses(nums)
    print("After moving zeroes:", nums)  # Output: [1, 3, 12, 0, 0]