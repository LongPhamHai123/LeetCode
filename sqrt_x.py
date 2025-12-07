# leetcode - 11
def sqrt_x(x: int) -> int:
    if x < 2:
        return x
    left, right = 2, x // 2
    while left <= right:
        mid = left + (right - left) // 2
        squared = mid * mid
        if squared == x:
            return mid
        elif squared < x:
            left = mid + 1
        else:
            right = mid - 1
    return right
def sqrt_x_linear(x: int) -> int:
    if x < 2:
        return x
    for i in range(1, x):
        if i * i > x:
            return i - 1

def sqrt_x_builtin(x: int) -> int:
    return int(x**0.5)

def sqrt_x_newton(x: int) -> int:
    if x < 2:
        return x
    r = x
    while r * r > x:
        r = (r + x // r) // 2
    return r

if __name__ == "__main__":
    number = 8
    result = sqrt_x(number)
    print(f"The integer square root of {number} is {result}")  # Output: 2