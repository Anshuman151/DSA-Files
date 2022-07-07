class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None
class CSLL:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.tail.next:
                break
            node = node.next
    #Creation of circular singly linked list
    def createCSLL(self,nodevalue):
        node = Node(nodevalue)
        node.next = node
        self.head = node
        self.tail = node
        return 'The CSLL has been Created'

CirSinglyLL = CSLL()
CirSinglyLL.createCSLL(1)
print([node.value for node in CirSinglyLL])