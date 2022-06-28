class Node:
    def __init__(self,value = None):
        self.value = value         # O(1)
        self.next = None           # O(1)

class SLinkedList:
    def __init__(self):
        self.head = None           # O(1)
        self.tail = None          # O(1)


Singlylinkedlist = SLinkedList()
node1 = Node(1)
node2 = Node(2)
Singlylinkedlist.head=node1
Singlylinkedlist.head.next=node2         # O(1)
Singlylinkedlist.tail=node2

#Space Complexity : O(1)
#Time Complexity : O(1)