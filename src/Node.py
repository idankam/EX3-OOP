class Node:
    def __init__(self, _id, pos,  _weight, edges_in = {}, edges_out = {}, tag=-1):
        self.id = _id
        self.edges_in = edges_in
        self.edges_out = edges_out
        self.pos = pos
        self.tag = tag
        self.weight = _weight

    # getters and setters

    # remove edge_out
    # remove edge_in
    # remove all edges_out

    # copy

    # compareTo
