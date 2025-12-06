class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.value < l2.value:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return dummy.next
    def reverseList(self, head: ListNode) -> ListNode:
        # prev = None
        # current = head

        # while current:
        #     next_node = current.next
        #     current.next = prev
        #     prev = current
        #     current = next_node

        # return prev
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
    def append(self, head: ListNode, value: int) -> ListNode:
        new_node = ListNode(value)
        if not head:
            return new_node
        current = head
        while current.next:
            current = current.next
        current.next = new_node
        return head

    def display(self, head: ListNode) -> None:
        current = head
        values = []
        while current:
            values.append(current.value)
            current = current.next
        print("LinkedList:", " -> ".join(map(str, values)))
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
    # def deleteNode(self, head, target):
    #     if not head:
    #         return None
        
    #     if head.val == target:
    #         return head.next
        
    #     curr = head
    #     while curr.next:
    #         if curr.next.val == target:
    #             curr.next = curr.next.next
    #             break
    #         curr = curr.next
    #     return head
    def deleteNode(self, head, target):
        if not head:
            return None
        if head.value == target:
            return head.next
        current = head
        while current.next:
            if current.next.value == target:
                current.next = current.next.next
                break
            current = current.next
        return head
    # def getMiddleNode(self, head: ListNode) -> ListNode:
    #     slow = head
    #     fast = head

    #     while fast and fast.next:
    #         slow = slow.next
    #         fast = fast.next.next

    #     return slow
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        while current and current.next:
            if current.value == current.next.value:
                current.next = current.next.next
            else:
                current = current.next
        return head
