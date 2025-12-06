# Định nghĩa node của Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        # Di chuyển fast đi trước n bước
        for _ in range(n):
            fast = fast.next

        # Di chuyển cả fast và slow cho đến cuối
        while fast.next:
            fast = fast.next
            slow = slow.next

        # Xóa node thứ n từ cuối
        slow.next = slow.next.next
        return dummy.next
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

sol = Solution()
new_head = sol.removeNthFromEnd(head, 2)
while new_head:
    print(new_head.val)
    new_head = new_head.next