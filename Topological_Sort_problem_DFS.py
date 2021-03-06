import numpy as np

# Graph must be directed acyclic graph
# Graph is represented as Edge list. Here
Edges = np.array([('A', 'D'), ('B', 'D'), ('C', 'A'), ('C', 'B'), ('D', 'G'), ('D', 'H'),
                  ('E', 'A'), ('E', 'D'), ('E', 'F'), ('F', 'K'), ('F', 'J'), ('G', 'I'),
                  ('H', 'I'), ('H', 'J'), ('I', 'L'), ('J', 'L'), ('J', 'M'), ('K', 'J')])

# Nodes of the graph can be represented as a simple list
Nodes = np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'])

# Length of the traversal or total number of edges.
Length = len(Nodes)
Edges_Length = len(Edges)

# Visited array for the edges that have been traversed
visited_nodes = np.array([False for i in range(0, Length)])


# Solution array of array of topological sorted nodes.
Topo_Sort = []


# Stack For both Nodes and Edges
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
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
        if self.head is None:
            print('Nothing to pop!')
        elif self.head.next is None:
            print('Last item poped')
            self.head = None
        else:
            trav = self.head
            while trav.next.next is not None:
                trav = trav.next
            trav.next = None

    def printStack(self):
        trav = self.head
        if trav is None:
            print('Nothing to print')
        else:
            while True:
                print(trav.val)
                if trav.next is None:
                    break
                trav = trav.next


# Returns Edge to a given Node
def selectEdge(node):
    i = 0
    Current_Edge = None
    while i < Edges_Length:
        if Edges[i][0] == node and not checkVisited(Edges[i][1]):
            Current_Edge = Edges[i]
            break
        i += 1
    i = 0
    if Current_Edge is not None:
        while i < Length:
            if Nodes[i] == Current_Edge[1]:
                visited_nodes[i] = True
            i += 1
        return Current_Edge
    else:
        return None


Node_Stack = Stack()
Edge_Stack = Stack()


# Checks if the given node is visited or not.
def checkVisited(node):
    i = 0
    while i < Length:
        if Nodes[i] == node:
            if visited_nodes[i]:
                return True
            else:
                return False
        i += 1


# Main Topological sort algorithm...
def Topological_Sort():
    if False in visited_nodes:
        i = 0
        rand_node = np.random.choice(Nodes)
        while checkVisited(rand_node):
            rand_node = np.random.choice(Nodes)
        while i < Length:
            if Nodes[i] == rand_node:
                visited_nodes[i] = True
                break
            i += 1
        edge = selectEdge(rand_node)
        if edge is None:
            Node_Stack.push(Node(rand_node))
        else:
            Edge_Stack.push(Node(edge))
            while Edge_Stack.head is not None:
                trav = Edge_Stack.head
                while trav.next is not None:
                    trav = trav.next
                next_edge = selectEdge(trav.val[1])
                if next_edge is None:
                    Node_Stack.push(Node(trav.val[1]))
                    for_head = trav.val
                    Edge_Stack.pop()
                    if Edge_Stack.head is None:
                        edge_for_head = selectEdge(for_head[0])
                        if edge_for_head is None:
                            Node_Stack.push(Node(for_head[0]))
                        else:
                            Edge_Stack.push(Node(edge_for_head))
                else:
                    Edge_Stack.push(Node(next_edge))
                Edge_Stack.printStack()
        Topological_Sort()


Topological_Sort()
Node_Stack.printStack()