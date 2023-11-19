# LRUCache LRU缓存，最近最少使用
# 使用双向链表，时间复杂的 put,get 时间复杂度为 O(1)
# 想起O(1)时间复杂度，势必想起dict结构


class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache():
    def __init__(self, cap: int):
        self.cache = dict()
        # 构建head和tail，避免做判空判断
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cap = cap
        self.size = 0

    def get(self, key: int):
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            # 将访问的数据放到首位
            self.moveToHead(node)

    def put(self, key: int, value: int):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)
        else:
            node = DLinkedNode(key, value)
            self.cache[key] = value
            self.addHead(node)
            self.size = self.size + 1
            if self.size >= self.cap:
                removed = self.removeTail()
                self.cache.pop(removed.key)
                self.size = self.size - 1

    def addHead(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        node.prev = self.head
        self.head.next = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node):
        self.remove(node)
        self.addHead(node)

    def removeTail(self):
        node = self.tail.prev
        self.remove(node)
        return node