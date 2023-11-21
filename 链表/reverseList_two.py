# Definition for singly-linked list.
# 反转链表Ⅱ，单链表 head 和两个整数 left/right,其中left <= right.
# 请反转left到right的位置
# 输入：head = [1,2,3,4,5],left = 2 ,right = 4
# 输出：[1,4,3,2,5]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int):
        dummy_node = ListNode(-1)
        dummy_node.next = head
        pre = dummy_node

        for _ in range(left - 1):
            pre = pre.next

        curr = pre.next
        for _ in range(right - left):
            next = curr.next
            curr.next = next.next
            next.next = pre.next
            pre.next = next

        return dummy_node.next
