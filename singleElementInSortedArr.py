# leetcode - 540 
def singleNonDuplicate(nums: list[int]) -> int:
  left, right = 0, len(nums) - 1
  while left < right:
      mid = left + (right - left) // 2
      # Ensure mid is even for comparison
      if mid % 2 == 1:
          mid -= 1
      if nums[mid] == nums[mid + 1]:
          left = mid + 2 # phần tử duy nhất nằm bên phải mid
      else:
          right = mid # phần tử duy nhất nằm bên trái mid hoặc chính mid
  return nums[left]

def singleNonDuplicates(nums: list[int]) -> int:
  for i in range(0, len(nums) - 1, 2):
     if nums[i] != nums[i + 1]:
        return nums[i]
  return nums[-1]
  