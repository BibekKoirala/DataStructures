import numpy as np

# Initial state of the problem '.' represents free path, '#' represents blocked path, 'E' represents exit
state = np.array([['.', '.', '.', '#', '.', '.', '.','.'],
                  ['.', '#', '.', '.', '.', '#', '.','.'],
                  ['.', '#', '.', '.', '.', '.', '.','#'],
                  ['.', '.', '#', '#', '.', '.', '.','.'],
                  ['#', '.', '#', 'E', '.', '#', '.','#']])


# Array to keep track of visited nodes
visited = np.array([[False, False, False, False, False, False, False, False],
                    [False, False, False, False, False, False, False, False],
                    [False, False, False, False, False, False, False, False],
                    [False, False, False, False, False, False, False, False],
                    [False, False, False, False, False, False, False, False]])


path_array = np.array([[False, False, False, False, False, False, False, False],
                    [False, False, False, False, False, False, False, False],
                    [False, False, False, False, False, False, False, False],
                    [False, False, False, False, False, False, False, False],
                    [False, False, False, False, False, False, False, False]])

# Array to keep track of previous element
prev = np.array([[None for item in range(0,8)],
                [None for item in range(0,8)],
                [None for item in range(0,8)],
                [None for item in range(0,8)],
                [None for item in range(0,8)]])

ini_row = 0
ini_col = 0

state_row = 4
state_col = 7

path = (4, 3)


# Node for tipple that defines tuple
class Node:
    def __init__(self, pos):
        self.pos = pos
        self.next = None


# Queue and its operations for BFS traversal
class Queue:
    def __init__(self):
        self.head = None

    def enqueue(self, node):
        if self.head is None:
            self.head = node
        else:
            trav = self.head
            while trav.next is not None:
                trav = trav.next
            trav.next = node

    def dequeue(self):
        if self.head is None:
            print('No item to remove')
        elif self.head.next is None:
            print('Queue is empty now')
            top = self.head.pos
            self.head = None
            return top
        else:
            top = self.head.pos
            self.head = self.head.next
            return top


# Main BFS logic
def BFS():
    main_queue.enqueue(Node((ini_row, ini_col)))
    i = 0
    visited[ini_row][ini_col] = True
    while i < state.size - 1:
        current_pos = main_queue.dequeue()
        print(visited)
        if checksol(current_pos):
            print('Found Exit')
            break
        else:
            print('Not found')
            findPath(current_pos)
            # insert more items
        i += 1


# Functon to trace to new positions
def findPath(ind):
    if ind[0] != 0:
        new_pos = (ind[0] - 1, ind[1])
        if not (visited[new_pos[0]][new_pos[1]] or state[new_pos[0]][new_pos[1]] == '#'):
            visited[new_pos[0]][new_pos[1]] = True
            main_queue.enqueue(Node(new_pos))
            parent_pos = ind
            child_pos = new_pos
            prev[child_pos[0], child_pos[1]] = parent_pos

    if ind[1] != 0:
        new_pos = (ind[0], ind[1] - 1)
        if not (visited[new_pos[0]][new_pos[1]] or state[new_pos[0]][new_pos[1]] == '#'):
            visited[new_pos[0]][new_pos[1]] = True
            main_queue.enqueue(Node(new_pos))
            parent_pos = ind
            child_pos = new_pos
            prev[child_pos[0], child_pos[1]] = parent_pos

    if ind[1] != state_col:
        new_pos = (ind[0], ind[1] + 1)
        if not (visited[new_pos[0]][new_pos[1]] or state[new_pos[0]][new_pos[1]] == '#'):
            visited[new_pos[0]][new_pos[1]] = True
            main_queue.enqueue(Node(new_pos))
            parent_pos = ind
            child_pos = new_pos
            prev[child_pos[0], child_pos[1]] = parent_pos

    if ind[0] != state_row:
        new_pos = (ind[0] + 1, ind[1])
        if not (visited[new_pos[0]][new_pos[1]] or state[new_pos[0]][new_pos[1]] == '#'):
            visited[new_pos[0]][new_pos[1]] = True
            main_queue.enqueue(Node(new_pos))
            parent_pos = ind
            child_pos = new_pos
            prev[child_pos[0], child_pos[1]] = parent_pos


# Function to check if given node is the solution
def checksol(val):
    if state[val[0]][val[1]] == 'E':
        return True
    else:
        return False


main_queue = Queue()
BFS()

print(prev)


while path is not None:
    print(path)
    path_array[path[0]][path[1]] = True
    path = prev[path[0]][path[1]]


# path of the solution
print(path_array)