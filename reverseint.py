class Solution:
    def reverse(self, x: int) -> int:
        """
        Đảo ngược các chữ số của số nguyên x
        Trả về 0 nếu vượt quá phạm vi 32-bit signed integer
        """
        # Giới hạn của 32-bit signed integer
        INT_MIN = -2**31  # -2147483648
        INT_MAX = 2**31 - 1  # 2147483647
        # Lưu dấu của số
        sign = -1 if x < 0 else 1
        # Làm việc với giá trị tuyệt đối
        x = abs(x)
        # Đảo ngược số
        reversed_num = 0
        while x > 0:
            digit = x % 10
            # Nếu reversed_num > INT_MAX // 10, thì reversed_num * 10 sẽ overflow
            if reversed_num > INT_MAX // 10:
                return 0
            # Thêm chữ số vào kết quả
            reversed_num = reversed_num * 10 + digit
            # Bỏ chữ số cuối cùng
            x //= 10
        # Thêm dấu vào kết quả
        reversed_num *= sign
        # Kiểm tra overflow cuối cùng
        if reversed_num < INT_MIN or reversed_num > INT_MAX:
            return 0
        return reversed_num
a = Solution()
print(a.reverse(-123))  # Output: -321