# Algorithm to Solve the problem faced by Dijkstra Algorithms
# Dijkstra algorithms dont work will with negative edge cost
# Bellman Ford algorithm work well with negative edge cost

import numpy as np

Edges = np.array([(0,1,5),(1,2,20),(1,5,30),(1,6,60),(2,3,10),(2,4,75),
                  (3,2,-15),(4,9,100),(5,4,25),(5,8,50),(5,6,5),(6,7,-50),
                  (7,8,-10)])

Nodes = np.array([0,1,2,3,4,5,6,7,8,9])
Dist = np.array([np.inf for item in Nodes])

No_Edges = len(Edges)
No_Nodes = len(Nodes)


def Bellman_Ford():
    Dist[0] = 0
    for v in range(0, No_Nodes):
        for edge in Edges:
            print(Dist)
            if Dist[np.where(Nodes == edge[0])] + edge[2] < Dist[np.where(Nodes == edge[1])]:
                Dist[np.where(Nodes == edge[1])] = Dist[np.where(Nodes == edge[0])] + edge[2]

    for v in range(0, No_Nodes):
        for edge in Edges:
            if Dist[np.where(Nodes == edge[0])] + edge[2] < Dist[np.where(Nodes == edge[1])]:
                Dist[np.where(Nodes == edge[1])] = -np.inf

    print(Dist)


Bellman_Ford()