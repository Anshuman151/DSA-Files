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

    #Insertion of node in circular singly linked list
    def insertCSLL(self,value,location):       #T.C -> O(n)    S.C -> O(1)
        if self.head is None:
            return 'The head reference is None'
        else:
            newNode = Node(value)
            if location == 0:        #Inserting element in Begining of Linked List
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                # self.tail = newNode
                # newNode.next = self.head
                # self.tail.next = newNode
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
            return ' The node has been sucessfully created'

    #Traversal of a node in circular singly Linked List
    def traversalinCSLL(self):         #T.C -> O(n)      S.C -> O(1)
        if self.head is None:
            return 'The head reference is None'
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break

    # Searching a node in circular singly Linked List
    def searchSLL(self, nodeValue):     #T.C ->  O(n)    S.C -> O(1)
        if self.head is None:
            return "There is not any node in this CSLL"
        else:
            tempNode = self.head
            while tempNode:
                tempNode = tempNode.next
                if tempNode.value == nodeValue:
                    return tempNode.value
                elif tempNode == self.tail.next:
                    return 'The node doesnot exist in this CSLL'

    # Deletion of a node in circular singly Linked List
    def deletenode(self,location):     #T.C -> O(n)        S.C -> O(1)
        if self.head is None:
            print('There is not any node in CSLL')
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = self.head
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    def deleteCSLL(self):         # T.C -> O(1)      S.C -> O(1)
        self.head = None
        self.tail.next = None
        self.tail = None

circularSLL = CSLL()
print(circularSLL.createCSLL(0))
print('-----------------')
circularSLL.insertCSLL(0,0)
circularSLL.insertCSLL(2,1)
circularSLL.insertCSLL(3,1)
circularSLL.insertCSLL(4,1)
print('-----------------')
circularSLL.traversalinCSLL()
print('-----------------')
print(circularSLL.searchSLL(4))
print([node.value for node in circularSLL])
circularSLL.deleteCSLL()
print([node.value for node in circularSLL])