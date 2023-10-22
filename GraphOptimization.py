#!/usr/bin/env python
# coding: utf-8

# Python program for Kruskal's algorithm and prim's algorithm

from collections import defaultdict
import sys
from typing import List, Dict
import time


class Vertex :
    def __init__(self, arg_id) :
        self._id = arg_id

class PrimsGraph :
    def __init__(self, source : int, adjacency_list : Dict[int, List[int]]) :
        self.source = source
        self.adjlist = adjacency_list

    def Prims (self) -> int :
        queue = { Vertex(self.source) : 0 }
        visited = [False] * len(self.adjlist)
        treeCost = 0

        while queue :
            # Choose the adjacent node with the least edge cost
            node = min (queue, key=queue.get)
            cost = queue[node]

            # Remove the node from the priority queue
            del queue[node]

            if visited[node._id] == False :
                treeCost += cost
                visited[node._id] = True
                print("Node Visited : " + str(node._id) + ", cost calculated now : "+str(treeCost))

                for item in self.adjlist[node._id] :
                    adjnode = item[0]
                    adjcost = item[1]
                    if visited[adjnode] == False :
                        queue[Vertex(adjnode)] = adjcost

        return treeCost

class KrushkalGraph:
    def __init__(self, v):
        self.V = v 
        self.graph = [] 

    #adds an edge to graph
    def addEdge(self, src, dest, weight):
        self.graph.append([src, dest, weight])
    
    #find
    def find(self, parent, node):
        if parent[node] == node:
            return node
        return self.find(parent, parent[node])

    #A function that does union of two sets of x and y

    def union(self, parent, rank, a, b):
        aroot = self.find(parent, a)
        broot = self.find(parent, b)

        #Union is done based on rank
        if rank[aroot] < rank[broot]:
            parent[aroot] = broot
        elif rank[aroot] > rank[broot]:
            parent[broot] = aroot
        
        #For same rank, we make the node as same root.
        # we will increment the rank by one
        else:
            parent[broot] = aroot
            rank[aroot] += 1

        # The main function to construct MST using Kruskal's
        # algorithm
    def KruskalMST(self):
        minimumSpanningTree = []
        index = 0
        considerededges = 0
        
        #Sorting according to their weights

        self.graph = sorted(self.graph,key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # Number of edges to be taken is equal to V-1
        while considerededges < self.V - 1:

            # Step 2: Pick the smallest edge and increment
            # the index for next iteration
            src, dest, weight= self.graph[index]
            index = index + 1
            a = self.find(parent, src)
            b = self.find(parent, dest)

            #Checking for cycle
            if a != b:
                considerededges+= 1
                minimumSpanningTree.append([src, dest, weight])
                self.union(parent, rank, a, b)

        minimumCost = 0
        print ("Edges in the constructed MST")
        for src, dest, weight in minimumSpanningTree:
            minimumCost += weight
            print("%d -- %d == %d" % (src, dest, weight))
        print("Minimum Spanning Tree" , minimumCost)

def main():
    op = 0
    lst = []
    while(op != 4):
        print("Please select one of the below options\n\n 1.Kruskal’s Minimum Spanning Tree Algorithm \n 2.Prim’s Minimum Spanning Tree Algorithm \n3.Implement both algorithms \n4.exit")
        op = int(input())
        if(op == 1):
            n = int(input("HOW MANY VERTICES...? "))
            g = KrushkalGraph(n)

            print("ENTER THE - ORIGIN VERTEX, END VERTEX, WEIGHT (NOTE: Enter -1 -1 -1 at the end): ") 
            #(-1, -1, -1) as the stopping criteria at the end

            for i in range(99999):
                origin, end, weight = map(int,input().split(" "))
                if origin == -1 and end == -1 and weight == -1:
                    break
                g.addEdge(origin, end, weight)
             
            start_time = time.time()
            g.KruskalMST()
            print("Execution time in case of this graph %s seconds when used kruskal algorithm"%(time.time()-start_time))
            
        elif(op==2):
            g1_edges_from_node = {}
            lst = []
            n = int(input("HOW MANY VERTICES...? "))
            for i in range(n):
                print("Enter no of edges from node"+ str(i))
                e = int(input())
                for j in range(e):
                    print("Enter adjacent node and cost")
                    adjnode, cost = map(int, input().split(" "))
                    lst.append(tuple((adjnode,cost)))
                    g1_edges_from_node[i] = lst
            g1 = PrimsGraph(0, g1_edges_from_node)
            start_time = time.time()
            cost = g1.Prims()
            print("Cost of the minimum spanning tree in graph 1 : " + str(cost) +"\n")
            print("Execution time in case of this graph %s seconds when used prim's algorithm"% (time.time() - start_time))
            
        elif(op == 3):
            
            n = int(input("HOW MANY VERTICES...? "))
            g = KrushkalGraph(n)

            print("ENTER THE - ORIGIN VERTEX, END VERTEX, WEIGHT (NOTE: Enter -1 -1 -1 at the end): ") 
            #(-1, -1, -1) as the stopping criteria at the end

            for i in range(99999):
                origin, end, weight = map(int,input().split(" "))
                if origin == -1 and end == -1 and weight == -1:
                    break
                g.addEdge(origin, end, weight)
             
            start_time = time.time()
            g.KruskalMST()
            print("Execution time for krushkal in comparision to prims %s seconds"%(time.time()-start_time))
            
            g2_edges_from_node = defaultdict()
            for i in range(n):
                g2_edges_from_node[i] = []
            
            for i in g.graph:
               
                g2_edges_from_node[i[0]].append(tuple((i[1],i[2])))
                g2_edges_from_node[i[1]].append(tuple((i[0],i[2])))
            
                
            g2 = PrimsGraph(0, g2_edges_from_node)
            start_time = time.time()
            cost = g2.Prims()
            print("Cost of the minimum spanning tree in graph: " + str(cost) +"\n")
            print("Execution time for prims in comparision to krushkal %s seconds"%(time.time()-start_time))
            
        elif(op == 4):
            exit()
        else:
            print("Please select a valid option.")

if __name__=="__main__":
    main()