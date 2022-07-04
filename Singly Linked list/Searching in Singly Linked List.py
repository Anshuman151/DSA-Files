class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class SLL():
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):                     #we use this function to make our linked list printable
        node = self.head
        while node:
            yield node
            node = node.next
    #insert in Linked List
    def insertSLL(self,value,location):
        newnode=Node(value)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            if location == 0 :
                newnode.next = self.head       # here self.head had stored previous first node location in it
                self.head = newnode
            elif location == -1:               # -1 shows we are inserting at last node
                self.tail.next = None
                self.tail = newnode
            else:                             # adding element any where in middle of linked list
                # traversing the linkedlist
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index+=1
                nextNode = tempNode.next
                tempNode.next = newnode
                newnode.next = nextNode
                if tempNode == self.tail:
                    self.tail=newnode

    #Traversal in Linked List      T.C -> O(n) , S.C -> O(1)
    def traverseSLL(self):
        if self.head is None :
            print('The Singly Linked List doesnot exist')
        else:
            node=self.head
            while node is not None :
                print(node.value)
                node = node.next

    #Search in Linked List
    def Search(self,nodevalue):                 # T.C -> O(n) , S.C -> O(1)
        if self.head is None:
            return 'The List does not exist'
        else:
            node = self.head
            while node is not None:
                if node.value == nodevalue:
                    return node.value
                node = node.next
            return 'The value doesnot exist in the first'


SingleLinkedList = SLL()
SingleLinkedList.insertSLL(1, 1)
SingleLinkedList.insertSLL(2, 1)
SingleLinkedList.insertSLL(3, 1)
SingleLinkedList.insertSLL(4, 1)
SingleLinkedList.insertSLL(0, 0)
SingleLinkedList.insertSLL(0, 4)
print([node.value for node in SingleLinkedList])
print('----------------------')
SingleLinkedList.traverseSLL()
print('----------------------')
print(SingleLinkedList.Search(3))
print(SingleLinkedList.Search(33))

