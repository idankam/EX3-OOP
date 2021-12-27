import pygame
import os
from graph3 import *
from GraphAlgo import *
from pygame.constants import RESIZABLE
import pygame.gfxdraw
import math
pygame.font.init()
clock = pygame.time.Clock()
FONT = pygame.font.SysFont('comicsans', 20)

def scale(data, min_screen, max_screen, min_data, max_data):
    """
    get the scaled data with proportions min_data, max_data
    relative to min and max screen dimensions
    """
    return ((data - min_data) / (max_data-min_data)) * (max_screen - min_screen) + min_screen

min_x=min_y=max_x=max_y=0
def min_max(graph):
    global min_x,min_y,max_x,max_y
    min_x = min(list(GraphAlgo.get_graph().Nodes.values()), key=lambda n: n.pos.x).pos.x
    min_y = min(list(GraphAlgo.get_graph().Nodes.values()), key=lambda n: n.pos.y).pos.y
    max_x = max(list(GraphAlgo.get_graph().Nodes.values()), key=lambda n: n.pos.x).pos.x
    max_y = max(list(GraphAlgo.get_graph().Nodes.values()), key=lambda n: n.pos.y).pos.y

class Button:
    def __init__(self, rect:pygame.Rect,color:tuple=(0,0,0)):
        self.rect=rect
        self.color=color
        self.pressed=False
    def press(self):
        self.pressed=not self.pressed

class Gui:
    def __init__(self,algo=None):
        self.algo=algo
        self.screen = pygame.display.set_mode((800, 600), depth=32, flags=RESIZABLE)
        min_max(algo.graph)
        self.button=Button(pygame.Rect(20,20,100,50),(200,200,200))
        #self.list_of_algo=[]
        self.play()

    def my_scale(self,data, x=False, y=False):
        if x:
            return scale(data, 50, self.screen.get_width() - 50, min_x, max_x)
        if y:
            return scale(data, 50, self.screen.get_height() - 50, min_y, max_y)
    def on_click(self):
        self.list_of_algo=self.algo.my_algo()



    def draw(self):
        t=[]


        pygame.draw.rect(self.screen,self.button.color,self.button.rect)
        button_text = FONT.render("ALGO",True, (0,0,250))
        self.screen.blit(button_text,(self.button.rect.x+10,self.button.rect.y+5))
        for src in self.algo.graph.nodes.values():
            x = self.my_scale(src.pos.x, x=True)
            y = self.my_scale(src.pos.y, y=True)
            radius=15
            pygame.draw.circle(self.screen,color=(0,0,0),center=(x,y),radius=radius)
            node_text=FONT.render(str(src.id),True,(250,250,250))
            self.screen.blit(node_text,(x,y))
            for dest in self.algo.graph.edges[src.id]:
                his_x=self.my_scale(algo.graph.nodes[dest].pos[0], x=True)
                his_y= self.my_scale(algo.graph.nodes[dest].pos[1], y=True)
                if (src.id,dest) in self.list_of_algo:

                    pygame.draw.line(self.screen, color=(0, 250, 0), start_pos=(x, y), end_pos=(his_x, his_y),width=5)


                else:
                    pygame.draw.line(self.screen,color=(250,0,0),start_pos=(x,y),end_pos=(his_x,his_y),width=4)


            # if len(t)>0:
            #     pygame.draw.lines(self.screen,color=(0,0,0),points=t,closed=False,width=30)

    def play(self):
        run=True
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if self.button.rect.collidepoint(event.pos):
                        self.button.press()
                        if self.button.pressed:
                            self.on_click()
                        else:
                            self.list_of_algo.clear()
            self.screen.fill((100, 100, 250))
            self.draw()

            pygame.display.update()

if __name__ == '__main__':
    g=from_json("graph3.json")
    algo=Algo()
    algo.init_graph(g)
    Gui(algo)

