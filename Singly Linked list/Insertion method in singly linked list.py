class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
class SLL:
    def __int__(self):
        self.head=None
        self.next=None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    #insert in Linked List
    def insertSLL(self,):

print(node.value for node in SLL)

