from graph3 import *

class Algo:
    def init_graph(self,g:Graph):
        self.graph=g

    def my_algo(self)-> list:
        res=[]
        for src in self.graph.nodes:
            for dest in self.graph.edges[src]:
                if (src+dest)%3==0 and (dest,src) not in res and src!=dest:
                    res.append((src,dest))
        return res

