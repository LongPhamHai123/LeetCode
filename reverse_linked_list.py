def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next = current.next # lưu trữ nút tiếp theo
        current.next = prev # đảo chiều liên kết
        prev = current # di chuyển prev lên nút hiện tại
        current = next # di chuyển current lên nút tiếp theo
    return prev