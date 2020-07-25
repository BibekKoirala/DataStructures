class Node:
    def __init__(self , value=None):
        self.data=value
        self.next=None

class CircularLinkedList:
    def __init__(self):
        self.head=None
    
    def insertion(self,value):
        if self.head is None:
            self.head=value
            self.head.next=self.head
        else:
            insert=self.head
            while insert.next is not self.head:
                insert=insert.next
            insert.next=value
            insert.next.next=self.head
    
    def deletionByValue(self,value=None):
        if self.head is None:
            print("No items to delete")  
        elif self.head.next is self.head:
            if self.head.data is not value:
                print("sorry value not found")
            else:
                self.head=None
                print("list is Now empty");
        else:
            deleteval=self.head
            flag=False
            while deleteval.next is not self.head:
                if deleteval.next.data is value:
                    deleteval.next=deleteval.next.next
                    flag=True
                deleteval=deleteval.next
            
            if flag is True:
                print(".......Item Deleted........")
            else:
                print(".....No Item in the list to delete.......")

    def printCircular(self):
        printval=self.head

        if self.head is None:
            print('No Items to Print')
        elif self.head.next is self.head:
            print(self.head.value)
        else:
            loop1=True
            while True:
                if(printval is not self.head or loop1):
                    print(printval.data)
                    printval=printval.next
                else:
                    break
                loop1=False

                

Circular = CircularLinkedList()

print("......1/////////")

Circular.printCircular()

print(".......2............")

for item in range(0,10):
    Circular.insertion(Node(item))

Circular.printCircular()
Circular.insertion(Node(20))

print("..........3............")
Circular.printCircular()
Circular.deletionByValue(6)

print("..........4..........")
Circular.printCircular()