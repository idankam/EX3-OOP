from GraphInterface import GraphInterface
from src.Edge import Edge
from src.Node import Node
from src.Location import Location


class DiGraph(GraphInterface):
    WHITE = 0
    GREY = 1
    BLACK = 2

    def __init__(self):
        self.Nodes = {}  # key = id, value = node
        self.Edges = {}  # key = "src,dest" , value = edge
        self.mc = 0

    # ge set methods

    def v_size(self) -> int:
        return len(self.Nodes)

    def e_size(self) -> int:
        return len(self.Edges)

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        self.Nodes.get(str(id1)).add_edge_out(id2, weight)
        self.Nodes.get(str(id2)).add_edge_in(id1, weight)
        e = Edge(src=id1, dest=id2, w=weight)
        e_name = str(id1) + ',' + str(id2)
        self.Edges[e_name] = e

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        loc = Location(pos[0], pos[1], pos[2])
        n = Node(_id=node_id, pos=loc)
        self.Nodes[node_id] = n

    def add_exist_node(self, node: Node):
        self.Nodes[node.id] = node

    def remove_node(self, node_id: int) -> bool:
        is_removed = self.Nodes.pop(node_id)
        if is_removed is None:
            print("there is no such key!")
            return False
        else:
            for key in self.Edges.keys():
                src = key.split(',')[0]
                dest = key.split(',')[1]
                if src == str(node_id):
                    self.remove_edge(int(src), int(dest))
                    self.Nodes.get(int(dest)).remove_edge_in(int(src))
                elif dest == str(node_id):
                    self.remove_edge(int(src), int(dest))
                    self.Nodes.get(int(src)).remove_edge_out(int(dest))
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        name = str(node_id1) + ',' + str(node_id2)
        is_removed = self.Edges.pop(name)
        if is_removed is None:
            return False
        else:
            return True

    """return a dictionary of all the nodes in the Graph, each node is represented using a pair
             (node_id, node_data)
            """

    def get_all_v(self) -> dict:
        return self.Nodes

    """return a dictionary of all the nodes connected to (into) node_id ,
            each node is represented using a pair (other_node_id, weight)
             """
    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.Nodes.get(id1).edge_in

    """return a dictionary of all the nodes connected from node_id , each node is represented using a pair
            (other_node_id, weight)
            """

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.Nodes.get(id1).edge_out

    # copy
    # color white
    def colorWhite(self):
        for node in self.Nodes.values():
            node.tag = 0  # WHITE

# transpose
    def transpose(self):
        T_graph = DiGraph()
        for node in self.Nodes.values():
            copy_node = node.copy()
            copy_node.edges_out.clear()
            copy_node.edges_in.clear()

        for edge in self.Edges.values():
            T_graph.add_edge(edge.id2, edge.id1, edge.weight)

        return T_graph

