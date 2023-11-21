# 反转链表
# 1->2->3->4->5反转后 5->4->3->2->1
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverselist(self, head):
        prev, curr = None, head  # 注意初始化 两个辅助指针
        if head.next is None:
            return head
        while head.next:
            next = curr.next  # 注意，提出next指针，进行辅助作用
            curr.next = prev  # 核心代码，进行方向变换
            prev = curr
            curr = next
        return prev
