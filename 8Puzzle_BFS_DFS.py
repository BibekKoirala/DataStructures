solution = [1, 2, 3, 4, 5, 6, 7, 8, 0]
visited = []
initial_list = []


# Node for Board
class Board:
    def __init__(self, board_item, pos):
        self.val = board_item
        self.pos = pos
        self.next = None


# Stack data structures for Depth first search
class Stack:
    def __init__(self):
        self.head = None

    def push(self, node):
        trav = self.head
        if self.head is None:
            self.head = node
        else:
            while trav.next is not None:
                trav = trav.next
            trav.next = node

    def pop(self):
        trav = self.head
        if self.head is None:
            print('Nothing in the stack')
        elif self.head.next is None:
            pos1 = trav.pos
            val = trav.val.copy()
            self.head = None
        else:
            while trav.next.next is not None:
                trav = trav.next
            pos1 = trav.next.pos
            val = trav.next.val
            trav.next = None

        return [pos1, val]

    def printstack(self):
        trav = self.head
        if self.head is None:
            print('Empty stack')
        else:
            while trav.next is not None:
                print(trav.val)
                trav = trav.next

            print(trav.val)


# Queue data structures for Breadth first search
class Queue:
    def __init__(self):
        self.head = None

    def push(self, node):
        if self.head is None:
            self.head = node
        else:
            trav = self.head
            while trav.next is not None:
                trav = trav.next
            trav.next = node

    def pop(self):
        val = self.head.val
        pos10 = self.head.pos
        self.head = self.head.next
        return [pos10, val]

    def printstack(self):
        trav = self.head
        if self.head is None:
            print('Empty stack')
        else:
            while trav.next is not None:
                print(trav.val)
                trav = trav.next

            print(trav.val)


# Main entry point for defth first search algorithm
def DFS():
    while True:
        top_of_stack = main_stack.pop()
        # print('top of stack',top_of_stack)
        if CheckSolution(top_of_stack[1]):
            visited.append(top_of_stack[1])
            print('Solution Found', top_of_stack[1])
            break
        else:
            print('not true')
            visited.append(top_of_stack[1])
            newBoardForDFS(top_of_stack[1], top_of_stack[0])


# Main entry ppoint for Breadth first search
def BFS():
    while True:
        top_of_Queue = main_Queue.pop()
        if CheckSolution(top_of_Queue[1]):
            visited.append(top_of_Queue[1])
            print('Solution Found', top_of_Queue[1])
            break
        else:
            print('not true')
            visited.append(top_of_Queue[1])
            newBoardForBFS(top_of_Queue[1], top_of_Queue[0])


# Function for adding new nodes into Queue
def newBoardForBFS(currentBoard, pos4):
    move1 = currentBoard.copy()
    move2 = currentBoard.copy()
    move3 = currentBoard.copy()
    move4 = currentBoard.copy()
    if pos4 == 0:
        swapforqueue(move1, pos4, 1)
        swapforqueue(move2, pos4, 3)
    elif pos4 == 1:
        swapforqueue(move1, pos4, 0)
        swapforqueue(move2, pos4, 2)
        swapforqueue(move3, pos4, 4)
    elif pos4 == 2:
        swapforqueue(move1, pos4, 1)
        swapforqueue(move2, pos4, 5)
    elif pos4 == 3:
        swapforqueue(move1, pos4, 0)
        swapforqueue(move2, pos4, 4)
        swapforqueue(move3, pos4, 6)
    elif pos4 == 4:
        swapforqueue(move1, pos4, 1)
        swapforqueue(move2, pos4, 3)
        swapforqueue(move3, pos4, 5)
        swapforqueue(move4, pos4, 7)
    elif pos4 == 5:
        swapforqueue(move1, pos4, 2)
        swapforqueue(move2, pos4, 4)
        swapforqueue(move3, pos4, 8)
    elif pos4 == 6:
        swapforqueue(move1, pos4, 3)
        swapforqueue(move2, pos4, 7)
    elif pos4 == 7:
        swapforqueue(move1, pos4, 4)
        swapforqueue(move2, pos4, 6)
        swapforqueue(move3, pos4, 8)
    elif pos4 == 8:
        swapforqueue(move1, pos4, 5)
        swapforqueue(move2, pos4, 7)
    else:
        print('Something went wrong')


# Function for adding new nodes into stack
def newBoardForDFS(currentBoard, pos3):
    move1 = currentBoard.copy()
    move2 = currentBoard.copy()
    move3 = currentBoard.copy()
    move4 = currentBoard.copy()
    if pos3 == 0:
        swapforstack(move1, pos3, 1)
        swapforstack(move2, pos3, 3)
    elif pos3 == 1:
        swapforstack(move1, pos3, 0)
        swapforstack(move2, pos3, 2)
        swapforstack(move3, pos3, 4)
    elif pos3 == 2:
        swapforstack(move1, pos3, 1)
        swapforstack(move2, pos3, 5)
    elif pos3 == 3:
        swapforstack(move1, pos3, 0)
        swapforstack(move2, pos3, 4)
        swapforstack(move3, pos3, 6)
    elif pos3 == 4:
        swapforstack(move1, pos3, 1)
        swapforstack(move2, pos3, 3)
        swapforstack(move3, pos3, 5)
        swapforstack(move4, pos3, 7)
    elif pos3 == 5:
        swapforstack(move1, pos3, 2)
        swapforstack(move2, pos3, 4)
        swapforstack(move3, pos3, 8)
    elif pos3 == 6:
        swapforstack(move1, pos3, 3)
        swapforstack(move2, pos3, 7)
    elif pos3 == 7:
        swapforstack(move1, pos3, 4)
        swapforstack(move2, pos3, 6)
        swapforstack(move3, pos3, 8)
    elif pos3 == 8:
        swapforstack(move1, pos3, 5)
        swapforstack(move2, pos3, 7)
    else:
        print('Something went wrong')


# Function where swapping of elements in board happens and pushed into stack
def swapforstack(board, ini_pos, fin_pos):
    board[ini_pos], board[fin_pos] = board[fin_pos], board[ini_pos]
    if board not in visited:
        main_stack.push(Board(board.copy(), fin_pos))
        return
    else:
        return


# Function where swapping of elements in board happens and pushed into queue
def swapforqueue(board, ini_pos, fin_pos):
    board[ini_pos], board[fin_pos] = board[fin_pos], board[ini_pos]
    if board not in visited:
        main_Queue.push(Board(board.copy(), fin_pos))
        return
    else:
        return


# Function to check if given Node is the solution
def CheckSolution(checkinglist):
    if checkinglist == solution:
        return True
    else:
        return False


# Entry point of the program
for i in range(0, 9):
    temp1 = int(input('Enter number to 8 puzzle'))
    if temp1 in initial_list:
        temp1 = int(input('Sorry the item is already in the list'))
    initial_list.append(temp1)
    if temp1 == 0:
        pos: int = i
method_type = int(input('Enter 1 for BFS and 2 for DFS'))
if method_type == 1:
    main_Queue = Queue()
    main_Queue.push(Board(initial_list, pos))
    BFS()
elif method_type == 2:
    main_stack = Stack()
    main_stack.push(Board(initial_list, pos))
    DFS()

for item in visited:
    print(item)
