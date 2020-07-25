class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def printList(self):
        printval=self.headval
        if printval is None:
            print("No item to print")
        else:
            while True:
                print(printval.dataval)
                if printval.nextval is None:
                    break
                printval=printval.nextval 

    def addToList(self,Node=None):
        if headval.dataval is None:
            headval=Node
        else:
        addval= self.headval
        while addval.nextval is not None:
            addval=addval.nextval
        addval.nextval=Node

    def popLastItem(self):
        popval=self.headval
        if popval is None:
            print("No Item in list to pop")
        elif popval.nextval is None:
            returnVal = popval.dataval
            popval = None
            print("The List is now empty")
            return returnVal
        else:
            nextVal=self.headval
            while popval.nextval.nextval is not None:
                popval=popval.nextval
            popval.nextval=None

    def popItemByValue(self,value=None):
        if value is None:
            print("Please Give value some value")         
        elif self.headval.dataval is value:
            self.headval.nextval=self.headval
        else:
            popval=self.headval
            while popval.nextval.dataval is not value:
                popval=popval.nextval
            
            popval.nextval=popval.nextval.nextval


list1 = SLinkedList()

list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

list1.headval.nextval = e2
e2.nextval = e3

print("First.................")
list1.printList()

list1.addToList(Node("Fri"))
list1.addToList(Node("Sat"))
list1.addToList(Node("Sun"))

print("second............")
list1.printList()
list1.popLastItem()

print("Third.............")
list1.printList()

list1.popItemByValue("Tue")

print("Fourth................")
list1.printList()

list1.popItemFromTail()

print("Fifth..............")
list1.printList()