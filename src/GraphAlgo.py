import sys
from typing import List
from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface
import queue as Q


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: DiGraph):
        self.graph = graph

    # get - THERE IS NO NEED
    # set - THERE IS NO NEED
    # is connected ?
    # BFS ? - DID IT
    # dijkstra did it
    # get path after dijkstra did it
    #

    def BFS(self, g: DiGraph, node) -> None:
        WHITE = 0;
        GREY = 1;
        BLACK = 2
        g.nodes.get(node).tag = GREY
        queue = []
        queue.append(node)
        while queue:
            id = queue.pop();
            for i in g.all_out_edges_of_node():
                if (g.nodes.get(i.dest).tag == WHITE):
                    nextId = i.dest
                    g.nodes.get(nextId).tag = GREY
                    queue.append(nextId)
            g.nodes.get(id).tag = BLACK

    def load_from_json(self, file_name: str) -> bool:
        pass

    def save_to_json(self, file_name: str) -> bool:
        pass

    def shortest_path(self, id1: int, id2: int) -> (
    float, list):  ## check if first src and second dest (not nesscerry connected)
        pointers = self.dijkstra(id1)
        path = []
        prev = id2
        while prev != id1:
            path.insert(0, self.graph.nodes.get(prev))
            prev = pointers.get(prev)
        path.insert(0, self.graph.nodes.get(id1))
        return self.graph.nodes.get(id2).weight, path

    def plot_graph(self) -> None:
        pass

    def dijkstra(self, src):  ## check if weight is positive
        pqueue = Q.PriorityQueue
        prevPointer = {}  ## key = id node, val= point to(node)
        for node in self.graph.nodes:
            if node.id == src:
                node.weight = 0
                prevPointer[node.id] = None
            else:
                node.weight = sys.maxsize
                prevPointer[node.id] = -1
            pqueue.put(node)
        while not pqueue.empty():
            currNode = pqueue.get()
            for edge in self.graph.all_out_edges_of_node(currNode.id):
                nodeNeighbour = self.graph.nodes.get(edge.dest)
                newWeight = currNode.weight + edge.weight
                if newWeight < nodeNeighbour.weight:
                    nodeNeighbour.weight = newWeight
                    prevPointer[nodeNeighbour.id] = currNode.id
                    pqueue.get(nodeNeighbour)
                    pqueue.put(nodeNeighbour)

        return prevPointer

    def get_graph(self) -> GraphInterface:
        return self.graph
        """
        :return: the directed graph on which the algorithm works on.
        """

    def TSP(self, node_lst: List[int]) -> (List[int], float):

        """
        Finds the shortest path that visits all the nodes in the list
        :param node_lst: A list of nodes id's
        :return: A list of the nodes id's in the path, and the overall distance
        """

    def centerPoint(self) -> (int, float):
        minMaxNode = None
        bestMinMax = sys.maxsize  ## maxNum
        for node in self.graph.nodes:
            self.dijkstra(node.id)
            tmpMaxDist = -sys.maxsize - 1
            for checkNode in self.graph.nodes:
                if checkNode.weight > tmpMaxDist:
                    tmpMaxDist = checkNode.weight
            if tmpMaxDist < bestMinMax:
                bestMinMax = tmpMaxDist
                minMaxNode = node
        return bestMinMax, minMaxNode

        """
        Finds the node that has the shortest distance to it's farthest node.
        :return: The nodes id, min-maximum distance
        """
