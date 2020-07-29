import numpy as np

Nodes = np.array([0, 1, 2, 3, 4])
Node_Len = len(Nodes)
Edges = np.array([(0, 1, 4), (0, 2, 1), (1, 3, 1), (2, 1, 2), (2, 3, 5), (3, 4, 3)])
Edges_Len = len(Edges)
Dist = np.array([None for i in range(0, Node_Len)])
Dist[0] = 0
Start = 0
prev = np.array([None for i in range(0, Node_Len)])


class Node:
    def __init__(self, node, dist):
        self.node = node
        self.dist = dist
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.head = None

    def push(self, node):
        if self.head is None:
            self.head = node
        else:
            trav = self.head
            if self.head.dist > node.dist:
                trav = self.head
                self.head = node
                self.head.next = trav
            else:
                while trav.next is not None and trav.next.dist < node.dist:
                    trav = trav.next
                self.printQueue()
                node.next = trav.next
                trav.next = node

    def pop(self):
        if self.head is None:
            print("No Items to delete")
        elif self.head.next is None:
            self.head = None
            print('Last Item Poped')
        else:
            self.head = self.head.next

    def printQueue(self):
        trav = self.head
        if trav is None:
            print('Nothing to print')
        else:
            while trav is not None:
                print('Printing', trav.node, trav.dist)
                trav = trav.next


# Returns all the edges relating to a particular node.
def getEdges(node):
    j = 0
    edges = []
    while j < Edges_Len:
        if Edges[j][0] == node:
            edges.append(Edges[j])
        j += 1
    return edges


NodeQueue = PriorityQueue()


def Lazy_Dijkstra_SPA():

    Dist[0] = 0
    NodeQueue.push(Node(0, 0))

    while NodeQueue.head is not None:
        current_node = NodeQueue.head.node
        current_dist = NodeQueue.head.dist
        allEdges = getEdges(current_node)
        dist_of_current = Dist[np.where(Nodes == current_node)][0]
        if dist_of_current is not None or current_dist < dist_of_current:
            for edge in allEdges:
                new_dist = dist_of_current + edge[2]
                if Dist[np.where(Nodes == edge[1])][0] is None:
                    NodeQueue.push(Node(edge[1], new_dist))
                    Dist[np.where(Nodes == edge[1])] = new_dist
                elif new_dist < Dist[np.where(Nodes == edge[1])][0]:
                    NodeQueue.push(Node(edge[1], new_dist))
                    Dist[np.where(Nodes == edge[1])] = new_dist
                prev[np.where(Nodes == edge[1])] = edge[0]
        NodeQueue.pop()


Lazy_Dijkstra_SPA()
print('Shortest distance from 0', Dist)
print('For Path', prev)
NodeQueue.printQueue()

