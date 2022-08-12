class Node:
    def __init__(self,value = None):
        self.value = value
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node :
            yield node
            node = node.next

    def createDLL(self,nodevalue):
        node = Node(nodevalue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return 'The Double Linked List is Created Successfully'

    # Insertion in Doubly Linked List
    def insertDLL(self,nodevalue,location):
        if self.head is None:
            print('The Node cannot be inserted')
        else:
            newNode = Node(nodevalue)
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == 1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempnode = self.head
                index = 0
                while index < location-1 :
                    tempnode = tempnode.next
                    index += 1
                #print(tempnode.value)
                newNode.next = tempnode.next
                newNode.prev = tempnode
                newNode.next.prev = newNode
                tempnode.next = newNode

    def traverseDLL(self):
        if self.head is None:
            print("There is no element to Traverse")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next

    def RevtraverseDLL(self):
        if self.head is None:
            print("There is no element to Traverse")
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev


doublelinkedlist = DLL()
doublelinkedlist.createDLL(5)
doublelinkedlist.insertDLL(1,0)
doublelinkedlist.insertDLL(3,1)
doublelinkedlist.insertDLL(10,2)
print([node.value for node in doublelinkedlist])
doublelinkedlist.RevtraverseDLL()