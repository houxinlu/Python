# -*- coding:UTF - 8 -*-

"""
    链表反转
    反向链表相加

"""


class Node():
    def __init__(self, item):
        self.item = item
        self.next = None


class Solution():
    """ 两个逆序链表（node值从大到小）相加 """

    def reverse(self, node):
        """ 链表反转 """
        pre = None

        while node != None:
            next = node.next
            node.next = pre
            pre = node
            node = next
        return pre

    def addTwoNumbers(self, l1, l2):
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        pre = None
        node = None
        carry = 0

        while l1 or l2:
            x = l1.item if l1 else 0
            y = l2.item if l2 else 0
            n = x + y + carry
            carry = n // 10
            node = Node(n % 10)
            node.next = pre
            pre = node
            if (l1 != None): l1 = l1.next
            if (l2 != None): l2 = l2.next
        if carry > 0:
            node = Node(1)
            node.next = pre
            pre = node
        self.reverse(l1)
        self.reverse(l2)
        return node


if __name__ == '__main__':

    sol = Solution()
    l1 = Node(4)
    l1.next = l11 = Node(5)
    l11.next = Node(6)

    l2 = Node(7)
    l2.next = l21 = Node(8)
    l21.next = l22 = Node(9)

    res = sol.addTwoNumbers(l1, l2)

    while res:
        print(res.item)
        res = res.next
