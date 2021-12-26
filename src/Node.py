from src.Edge import Edge


class Node:
    def __init__(self, _id, pos, _weight=-1, edges_in={}, edges_out={}, tag=-1):
        self.id = _id
        self.edges_in = edges_in
        self.edges_out = edges_out
        self.pos = pos
        self.tag = tag
        self.weight = _weight

    def add_edge_out(self, dest, weight, tag=-1):
        self.edges_out[dest] = weight

    def add_edge_in(self, src, weight, tag=-1):
        self.edges_out[src] = weight

    # remove edge_out
    def remove_edge_out(self, dest):
        self.edges_out.pop(dest)

    # remove edge_in
    def remove_edge_in(self, src):
        self.edges_in.pop(src)

    # remove all edges_out
    def remove_all_edges_out(self):
        self.edges_out.clear()

    def remove_all_edges_in(self):
        self.edges_in.clear()

    # copy
    def copy(self):
        new_node = Node(self.id, self.pos, self.weight, self.edges_in.copy(), self.edges_out.copy(), self.tag)
        return new_node

    # compareTo
