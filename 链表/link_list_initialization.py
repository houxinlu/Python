# -*- coding:UTF-8 -*-


"""
链表基本操作：
    链表初始化
    判空：isEmpty()
    长度：listSize()
    头插：addAtHead()
    尾插：addAtTail()
    查找：search()
    遍历：ergodic()
    获取node的位置：getIndex()
    任意位置插入：addAtIndex()
    根据：node位置删除node:delAtIndex()
    跟进node值删除node:delAtItem()

"""


class Node():
    """节点"""

    def __init__(self, item):
        self.item = item
        self.next = None

    def getItem(self):
        return self.item


class MyLinkedList(object):
    """链表创建"""

    def __init__(self):
        """链表初始化"""
        self.head = None
        self.size = 0

    def isEmpty(self):
        """链表判空"""
        return self.head == None

    def listSize(self):
        """链表长度"""
        count = 0
        head = self.head
        while head:
            count += 1
            head = head.next
        return count

    def addAtHead(self, item):
        """首插"""

        item = Node(item)
        item.next = self.head
        self.head = item

    def addAtTail(self, item):
        """尾插"""
        head = self.head
        item = Node(item)
        if self.isEmpty():
            self.head = item
        while head.next != None:
            head = head.next
        head.next = item

    def search(self, item):
        """查找元素是否存在"""
        head = self.head
        while head:
            if head.item == item:
                return True
            else:
                head = head.next
        return False

    def ergodic(self):
        """链表遍历"""

        link_list = []
        head = self.head
        l = self.listSize()
        count = 0
        if head is None:
            return None
        while count < l:
            link_list.append(head.item)
            count += 1
            head = head.next
        return link_list

    def getIndex(self, item):
        """查找node位置"""
        count = 0
        head = self.head
        while head:
            if head.item == item:
                return count
            count += 1
            head = head.next

    def addAtIndex(self, index, item):
        """链表任意位置插入"""
        head = self.head
        l = self.listSize()
        count = 0
        if index <= 0:
            self.addAtHead(item)
        elif index > l - 1:
            self.addAtTail(item)
        else:
            item = Node(item)
            while count < index:
                count += 1
                head = head.next
            item.next = head.next
            head.next = item

    def delAtIndex(self, index):
        """删除index位置"""
        head = self.head
        pre = None
        count = 0

        while head is not None and count <= index:
            if count == index:
                if index == 0:
                    self.head = head.next
                else:
                    pre.next = head.next
                break
            else:
                count += 1
                pre = head
                head = head.next

    def delAtItem(self, item):
        """删除告诉的node值 """
        head = self.head
        pre = None
        while head:
            if head.item == item:
                if not pre:
                    self.head = head.next
                else:
                    pre.next = head.next
                break
            else:
                pre = head
                head = head.next


if __name__ == "__main__":
    # node = Node(100)  # 先创建一个节点传进去

    ll = MyLinkedList()
    print "ll是否位None: ", (ll.isEmpty())
    print"ll的listSize为: ", (ll.listSize())
    ll.addAtHead(6)
    ll.addAtHead(8)
    ll.addAtTail(9)
    print"添加了node:6，8，9后，ll的listSize为: ", (ll.listSize())
    print"node(8)的是否存在: ", (ll.search(8))
    print"node(9)的位置在: ", (ll.getIndex(9))
    ll.addAtIndex(1, 7)
    print"在原链表中的第二位添加node(7)后，ll的listSize为: ", (ll.listSize())
    print"node(7)是否存在: ", (ll.search(7))
    print"node(7)在链表的位置为: ", (ll.getIndex(7))
    print"遍历链表: ", (ll.ergodic())
    ll.delAtIndex(2)
    print"删除链表的第二位后，链表的长度: ", (ll.listSize())
    print"遍历链表: ", (ll.ergodic())
    ll.delAtItem(8)
    print"删除node(8)后，链表的长度: ", (ll.listSize())
    print"遍历链表: ", (ll.ergodic())
