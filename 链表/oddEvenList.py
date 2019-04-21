# -*- coding:UTF-8 -*-

"""
奇偶链表
把链表的奇数位和偶数位拼接在一起

"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class Solution(object):
    def oddEvenList(self, head):
        """奇偶链表"""

        odd = head
        eve = head.next
        eveHead = head.next

        if head == None or head.next == None or head.next.next == None:
            return head

        while odd.next and eve.next:
            odd.next = eve.next
            odd = odd.next
            eve.next = odd.next
            eve = eve.next
        odd.next = eveHead
        return head


if __name__ == '__main__':
    sol = Solution()
    ll = Node(1)
    ll.next = ll1 = Node(2)
    ll1.next = ll2 = Node(3)
    ll2.next = ll3 = Node(4)

    res = sol.oddEvenList(ll)

    while res:
        print res.value
        res = res.next
