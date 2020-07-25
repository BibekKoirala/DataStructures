class Node:
    def __init__(self , value=None):
        self.data=value
        self.right=None
        self.left=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None

    def insertion(self,value=None):
        if value==None:
            print("plaease enter something")
        elif self.head==None:
            self.head=value
        else:
            insertval=self.head
            while insertval.right is not None:
                insertval=insertval.right
            insertval.right=value
            insertval.right.left=insertval

    def deletehead(self):
        self.head=self.head.right
        self.head.left=None

    def deleteByValue(self, value=None):
        if value is None:
            print("Give a value")
        elif value is not None:
            deleteval=self.head
            while deleteval.right.data is not value:
                if deleteval.right is None:
                    break
                deleteval=deleteval.right
            if deleteval.right is None:
                print("No Value found")
            else:
                deleteval.right=deleteval.right.right

    def deleteFromLast(self):
        deleteval=self.head
        while deleteval.right.right is not None:
            deleteval=deleteval.right
        deleteval.right=None
            
    
    def printQueue(self):
        printval=self.head
        while True:
            if(printval is not None):
                print(printval.data)
                printval=printval.right
            else:
                break

    

DoublyLinked = DoublyLinkedList()

for item in range(0,9):
    DoublyLinked.insertion(Node(item))


            
DoublyLinked.printQueue()
print(".....................................................")
DoublyLinked.deletehead()

DoublyLinked.printQueue()
print(".....................................................")
DoublyLinked.deleteByValue(6)
DoublyLinked.printQueue()
print(".....................................................")
DoublyLinked.deleteFromLast()
DoublyLinked.printQueue()