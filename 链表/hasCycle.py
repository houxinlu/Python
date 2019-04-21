# -*-coding:utf-8 -*-

"""
链表环问题
1. 判断链表有没有环
2. 判断链表环的入口位置

"""


class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class Resolue():
    def detectCycle(self, head):
        """ 快慢指针 """
        slow = fast = head
        Cycle = False
        if head is None:
            return head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                Cycle = True
                break

        if Cycle:
            ptr = head
            if ptr != slow:
                ptr = ptr.next
                slow = slow.next
            return ptr
        else:
            return None


if __name__ == '__main__':
    ll = Resolue()
    ll.next = ll1 = Node(1)
    print ll.detectCycle(ll)

    ll1.next = ll2 = Node(2)
    ll2.next = ll3 = Node(3)
    ll3.next = ll

    print ll.detectCycle(ll)
