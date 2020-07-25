class Node:
    def __init__(self,val=None):
        self.data=val
        self.next=None

class Stack:
    def __init__(self):
        self.head=None

    def pushLast(self,Node=None):
        if self.head is None:
            self.head=Node
        
        else:
            push=self.head
            while push.next is not None:
                push=push.next
            push.next=Node

    def popLast(self):
        popval=self.head
        while popval.next.next is not None:
                popval=popval.next
        popval.next=None

    def printStack(self):
        printval=self.head
        while True:
            if(printval is not None):
                print(printval.data)
                printval=printval.next
            else:
                break


Stack1 = Stack()
for item in range(0,10):
    Stack1.pushLast(Node(item))

print("........Itempushed...........")

Stack1.printStack()


Stack1.popLast()

print(".........Item Popped............")
Stack1.printStack()