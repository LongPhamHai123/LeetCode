# leetcode - 11
def maxArea(height: list[int]) -> int:
    left = 0
    right = len(height) - 1
    max_area = 0
    while left < right:
        # Calculate the area formed by the lines at the left and right pointers
        current_area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, current_area)
        # Move the pointer pointing to the shorter line inward
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area