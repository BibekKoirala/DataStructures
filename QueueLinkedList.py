class Node:
    def __init__(self,value=None):
        self.data=value
        self.next=None

class Queue:
    def __init__(self):
        self.head=None

    def insertion(self, value):
        insertval=self.head

        if self.head is None:
            self.head=value
        else:
            while insertval.next is not None:
                insertval=insertval.next
            insertval.next=value

    def deletion(self):
        if self.head is None:
            print("No Items to delete")
        elif self.head.next is None:
            self.head=None
        else:
            self.head = self.head.next

    def printQueue(self):
        printval=self.head
        while True:
            if(printval is not None):
                print(printval.data)
                printval=printval.next
            else:
                break


Queue1 = Queue()
for item in range(0,10):
    Queue1.insertion(Node(item))

print("........Itempushed...........")

Queue1.printQueue()


Queue1.deletion()

print(".........Item Popped............")
Queue1.printQueue()

