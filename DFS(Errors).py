class Node:
    def __init__(self, matrr=None, pos=None):
        self.mat = matrr
        self.pos = pos
        self.next = None


class List:
    def __init__(self):
        self.Head = None

    def insertion(self, node):
        if self.Head is None:
            self.Head = node
        else:
            trav = self.Head
            while trav.next is not None:
                trav = trav.next
            trav.next = node

    def printlist(self):
        trav = self.Head
        if trav is None:
            print('Nothing to print')
            return
        while trav is not None:
            print('Matrix', trav.mat)
            print('Position', trav.pos)
            trav = trav.next

    def tail(self):
        trav = self.Head
        while trav.next is not None:
            trav = trav.next
        return trav

    def deletion(self):
        if self.Head is None:
            print('No Items to pop')
        elif self.Head.next is None:
            self.Head = None
        else:
            trav = self.Head
            while trav.next.next is not None:
                trav = trav.next
            visitedList.append(trav.next.mat)
            trav.next = None


def position_solve(list2, pos1):
    l1 = list2.copy()
    l2 = list2.copy()
    l3 = list2.copy()
    l4 = list2.copy()
    if pos1 == 0:
        new_list = swap(l1, 0, 1)
        if new_list not in visitedList:
            mainList.insertion(Node(new_list, 1))
        else:
            print('hello world')
        new_list = swap(l2, 0, 3)
        if new_list not in visitedList:
            mainList.insertion(Node(new_list, 3))
        else:
            print('already visited')
    elif pos1 == 1:
        new_list = swap(l1, 1, 0)
        if new_list not in visitedList:
            mainList.insertion(Node(new_list, 0))
        new_list = swap(l2, 1, 2)
        if new_list not in visitedList:
            mainList.insertion(Node(new_list, 2))
        new_list = swap(l3, 1, 4)
        if new_list not in visitedList:
            mainList.insertion(Node(new_list, 4))
    elif pos1 == 2:
        new_list = swap(l1, 2, 1)
        if new_list not in visitedList:
            mainList.insertion(Node(new_list, 1))
        new_list = swap(l2, 2, 5)
        if new_list not in visitedList:
            mainList.insertion(Node(new_list, 5))
    elif pos1 == 3:
        new_list = swap(l1, 3, 0)
        if new_list not in visitedList:
            mainList.insertion(Node(new_list, 0))
        new_list = swap(l2, 3, 4)
        if new_list not in visitedList:
            mainList.insertion(Node(new_list, 4))
        new_list = swap(l3, 3, 6)
        if new_list not in visitedList:
            mainList.insertion(Node(new_list, 6))
    elif pos1 == 4:
        new_list = swap(l1, 4, 1)
        if new_list not in visitedList:
            mainList.insertion(Node(new_list, 1))
        new_list = swap(l2, 4, 3)
        if new_list not in visitedList:
            mainList.insertion(Node(new_list, 3))
        new_list = swap(l3, 4, 5)
        if new_list not in visitedList:
            mainList.insertion(Node(new_list, 5))
        new_list = swap(l4, 4, 7)
        if new_list not in visitedList:
            mainList.insertion(Node(new_list, 7))
    elif pos1 == 5:
        new_list = swap(l1, 5, 2)
        if new_list not in visitedList:
            mainList.insertion(Node(new_list, 2))
        new_list = swap(l2, 5, 4)
        if new_list not in visitedList:
            mainList.insertion(Node(new_list, 4))
        new_list = swap(l3, 5, 8)
        if new_list not in visitedList:
            mainList.insertion(Node(new_list, 8))
    elif pos1 == 6:
        new_list = swap(l1, 6, 3)
        if new_list not in visitedList:
            mainList.insertion(Node(new_list, 3))
        new_list = swap(l2, 6, 7)
        if new_list not in visitedList:
            mainList.insertion(Node(new_list, 7))
    elif pos1 == 7:
        new_list = swap(l1, 7, 4)
        if new_list not in visitedList:
            mainList.insertion(Node(new_list, 4))
        new_list = swap(l2, 7, 6)
        if new_list not in visitedList:
            mainList.insertion(Node(new_list, 6))
        new_list = swap(l3, 7, 8)
        if new_list not in visitedList:
            mainList.insertion(Node(new_list, 8))
    elif pos1 == 8:
        new_list = swap(l1, 6, 5)
        if new_list not in visitedList:
            mainList.insertion(Node(new_list, 5))
        new_list = swap(l2, 6, 7)
        if new_list not in visitedList:
            mainList.insertion(Node(new_list, 7))


def search_solution():
    ik = 0
    while True:
        list_temp = mainList.tail()
        #print('tail matrix', list_temp.mat)
        if check_solution(list_temp.mat):
            print('Solution Found')
            return

        next_list = list_temp.mat
        next_pos = list_temp.pos
        mainList.deletion()
        # print('next list from loop' , next_list)
        # print('next position', next_pos)
        #print('pushing......')
        position_solve(next_list, next_pos)
        #ik = ik + 1


def swap(current_list, initial_pos, final_pos):
    current_list[initial_pos], current_list[final_pos] = current_list[final_pos], current_list[initial_pos]
    if check_solution(current_list):
        print('Solution Found', current_list)
        return
    return current_list


def check_solution(list1):
    for j in range(0, 9):
        if list1[j] != j:
            return False
    return True


visitedList = []

mainList = List()

initial_list = []
for i in range(0, 9):
    temp1 = int(input('Enter number to 8 puzzle'))
    if temp1 in initial_list:
        temp1 = int(input('Sorry the item is already in the list'))
    initial_list.append(temp1)
    if temp1 == 0:
        pos = i

print('initially', pos)
mainList.insertion(Node(initial_list, pos))

#Start point of the application...
search_solution()

print(visitedList)
