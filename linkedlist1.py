# create a class called as Node
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# firstNode = Node(11)
# print(firstNode.data)


# create an empty class named LinkedList
class LinkedList:

    def __init__(self, head):
        self.head = None

    def listTraversal(self):
        if self.head is None:
            print("List is empty :P")

        tempNode = self.head
        while tempNode is not None:
            print("current node -> ", tempNode.data)
            tempNode = tempNode.next


firstNode = Node(1)
secondNode = Node(2)
thirdNode = Node(3)

linkedlist = LinkedList(firstNode)
linkedlist.head = firstNode
linkedlist.head.next = secondNode
secondNode.next = thirdNode

print("Head of linkedlist -> ", linkedlist.head.data)
print("Second Node -> ", linkedlist.head.next.data)
print("Memory location of Third node -> ", secondNode.next)
print("value of Third node -> ", secondNode.next.data)
print("\n\nLinked list Traversal ")
linkedlist.listTraversal()
