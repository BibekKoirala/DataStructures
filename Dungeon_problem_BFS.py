import numpy as np

state = np.array([['.', '.', '.', '#', '.', '.', '.','.'],
                  ['.', '#', '.', '.', '.', '#', '.','.'],
                  ['.', '#', '.', '.', '.', '.', '.','#'],
                  ['.', '.', '#', '#', '.', '.', 'E','.'],
                  ['#', '.', '#', '.', '.', '#', '.','#']])

visited = np.array([[False, False, False, False, False, False, False, False],
                    [False, False, False, False, False, False, False, False],
                    [False, False, False, False, False, False, False, False],
                    [False, False, False, False, False, False, False, False],
                    [False, False, False, False, False, False, False, False]])

ini_row = 0
ini_col = 0

state_row = 4
state_col = 7


class Node:
    def __init__(self, pos):
        self.pos = pos
        self.next = None


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


def findPath(ind):
    if ind[0] != 0:
        new_pos = (ind[0] - 1, ind[1])
        if not (visited[new_pos[0]][new_pos[1]] or state[new_pos[0]][new_pos[1]] == '#'):
            visited[new_pos[0]][new_pos[1]] = True
            main_queue.enqueue(Node(new_pos))

    if ind[1] != 0:
        new_pos = (ind[0], ind[1] - 1)
        if not (visited[new_pos[0]][new_pos[1]] or state[new_pos[0]][new_pos[1]] == '#'):
            visited[new_pos[0]][new_pos[1]] = True
            main_queue.enqueue(Node(new_pos))

    if ind[1] != state_col:
        new_pos = (ind[0], ind[1] + 1)
        if not (visited[new_pos[0]][new_pos[1]] or state[new_pos[0]][new_pos[1]] == '#'):
            visited[new_pos[0]][new_pos[1]] = True
            main_queue.enqueue(Node(new_pos))

    if ind[0] != state_row:
        new_pos = (ind[0] + 1, ind[1])
        if not (visited[new_pos[0]][new_pos[1]] or state[new_pos[0]][new_pos[1]] == '#'):
            visited[new_pos[0]][new_pos[1]] = True
            main_queue.enqueue(Node(new_pos))


def checksol(val):
    if state[val[0]][val[1]] == 'E':
        return True
    else:
        return False


main_queue = Queue()
BFS()

