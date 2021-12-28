import pygame
from GraphAlgo import *
from pygame.constants import RESIZABLE
import pygame.gfxdraw
import gui_Input

pygame.font.init()
clock = pygame.time.Clock()
FONT = pygame.font.SysFont('comicsans', 10)


def scale(data, min_screen, max_screen, min_data, max_data):
    """
    get the scaled data with proportions min_data, max_data
    relative to min and max screen dimensions
    """
    return ((data - min_data) / (max_data - min_data)) * (max_screen - min_screen) + min_screen


min_x = min_y = max_x = max_y = 0


def min_max(graph):
    global min_x, min_y, max_x, max_y
    min_x = min(list(graph.Nodes.values()), key=lambda n: n.pos.x).pos.x
    min_y = min(list(graph.Nodes.values()), key=lambda n: n.pos.y).pos.y
    max_x = max(list(graph.Nodes.values()), key=lambda n: n.pos.x).pos.x
    max_y = max(list(graph.Nodes.values()), key=lambda n: n.pos.y).pos.y
    # min_x = min(list(GraphAlgo.get_graph().Nodes.values()), key=lambda n: n.pos.x).pos.x
    # min_y = min(list(GraphAlgo.get_graph().Nodes.values()), key=lambda n: n.pos.y).pos.y
    # max_x = max(list(GraphAlgo.get_graph().Nodes.values()), key=lambda n: n.pos.x).pos.x
    # max_y = max(list(GraphAlgo.get_graph().Nodes.values()), key=lambda n: n.pos.y).pos.y


class Button:
    def __init__(self, rect: pygame.Rect, color: tuple = (0, 0, 0)):
        self.rect = rect
        self.color = color
        # self.pressed = False

    def press(self):
        self.pressed = not self.pressed


# class Toolbar:
#     def __init__(self, width, height):  # And other customisation options
#         self.image = pygame.Surface(width, height)
#         self.image.fill((50, 50, 50))
#         self.rect = self.image.get_rect()
#         self.rect.topleft = (0, 0)
#         # self.leftbutton = Button(args)
#         # self.rightbutton = Button(args)
#
#     def update(self):
#         self.leftbutton.hover()  # to animate an effect if the mouse hovers over
#         self.rightbutton.hover()
#
#     def draw(self, screen):
#         screen.blit(self.image, self.rect)
#         screen.blit(self.leftbutton.draw(), self.leftbutton.getRect())
#         screen.blit(self.rightbutton.draw(), self.rightbutton.getRect())
#
#     def click(self, pos):
#         if self.leftbutton.getRect().collidepoint(pos):
#             self.leftbutton.click()
#
#         if self.rightbutton.getRect().collidepoint(pos):
#             self.rightbutton.click()


class Gui:
    def __init__(self, algo=None):
        self.algo = algo
        self.screen = pygame.display.set_mode((800, 600), depth=32, flags=RESIZABLE)
        min_max(algo.graph)
        self.button = Button(pygame.Rect(0, 0, 60, 30), (200, 200, 200))
        self.button2 = Button(pygame.Rect(60, 0, 60, 30), (220, 220, 220))
        self.button3 = Button(pygame.Rect(120, 0, 60, 30), (240, 240, 240))
        self.special_nodes = []
        self.special_edges = []
        self.list_of_algo = []
        self.input_box = pygame.Rect(300, 0, 100, 0)
        self.color_inactive = pygame.Color((0, 0, 100))
        self.color_active = pygame.Color((0, 100, 0))
        self.color = self.color_inactive
        self.active = False
        self.text = ''
        self.play()

    def my_scale(self, data, x=False, y=False):
        if x:
            return scale(data, 50, self.screen.get_width() - 50, min_x, max_x)
        if y:
            return scale(data, 50, self.screen.get_height() - 50, min_y, max_y)

    def center_clicked(self):
        (key, w) = self.algo.centerPoint()
        self.special_nodes = [key]
        self.special_edges = []

    def tsp_clicked(self, text):
        if text is None:
            pass
        else:
            try:
                keys = []
                ls = text.split(",")
                for t in ls:
                    keys.append(int(t))
                ls, dist = self.algo.TSP(keys)
                self.special_nodes = ls
                self.special_edges = []
                for i in range(0, len(ls) - 1):
                    self.special_edges.append((ls[i], ls[i + 1]))
            except:
                text = gui_Input.main("tsp")
                self.tsp_clicked(text)

    def shortest_clicked(self, text):
        if text is None:
            pass
        if len(text.split(",")) != 2:
            text = gui_Input.main("shortest")
            self.shortest_clicked(text)
        else:
            try:
                ls = text.split(",")
                dist, ls = self.algo.shortest_path(int(ls[0]), int(ls[1]))
                self.special_nodes = ls
                self.special_edges = []
                for i in range(0, len(ls) - 1):
                    self.special_edges.append((ls[i], ls[i + 1]))
            except:
                text = gui_Input.main("shortest")
                self.shortest_clicked(text)

    def draw(self):

        pygame.draw.rect(self.screen, self.button.color, self.button.rect)
        pygame.draw.rect(self.screen, self.button2.color, self.button2.rect)
        pygame.draw.rect(self.screen, self.button3.color, self.button3.rect)

        button_text = FONT.render("CENTER", True, (0, 0, 250))
        self.screen.blit(button_text, (self.button.rect.x + 4, self.button.rect.y + 1))
        button_text = FONT.render("TSP", True, (0, 0, 250))
        self.screen.blit(button_text, (self.button2.rect.x + 4, self.button2.rect.y + 1))
        button_text = FONT.render("SHORTEST", True, (0, 0, 250))
        self.screen.blit(button_text, (self.button3.rect.x + 4, self.button3.rect.y + 1))

        for src in self.algo.graph.Nodes.values():
            x = self.my_scale(src.pos.x, x=True)
            y = self.my_scale(src.pos.y, y=True)
            for dest in self.algo.graph.all_out_edges_of_node(src.id).keys():
                his_x = self.my_scale(self.algo.graph.Nodes[dest].pos.x, x=True)
                his_y = self.my_scale(self.algo.graph.Nodes[dest].pos.y, y=True)
                color = (100, 100, 100)
                if (src.id, dest) in self.special_edges:
                    color = (250, 0, 0)
                pygame.draw.line(self.screen, color=color, start_pos=(x, y), end_pos=(his_x, his_y), width=2)

        for src in self.algo.graph.Nodes.values():
            x = self.my_scale(src.pos.x, x=True)
            y = self.my_scale(src.pos.y, y=True)
            for dest in self.algo.graph.all_out_edges_of_node(src.id).keys():
                his_x = self.my_scale(self.algo.graph.Nodes[dest].pos.x, x=True)
                his_y = self.my_scale(self.algo.graph.Nodes[dest].pos.y, y=True)
                if (src.id, dest) in self.special_edges:
                    color = (250, 0, 0)
                    pygame.draw.line(self.screen, color=color, start_pos=(x, y), end_pos=(his_x, his_y), width=2)

        for src in self.algo.graph.Nodes.values():
            x = self.my_scale(src.pos.x, x=True)
            y = self.my_scale(src.pos.y, y=True)
            radius = 15
            if src.id in self.special_nodes:
                pygame.draw.circle(self.screen, color=(100, 200, 0), center=(x, y), radius=radius)
            else:
                pygame.draw.circle(self.screen, color=(1, 1, 1), center=(x, y), radius=radius)
            pygame.draw.circle(self.screen, color=(250, 250, 250), center=(x, y), radius=radius - 2)
            node_text = FONT.render(str(src.id), True, (1, 1, 250))
            self.screen.blit(node_text, (x - 5, y - 5))

    def play(self):
        run = True
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button.rect.collidepoint(event.pos):
                        self.center_clicked()

                    if self.button2.rect.collidepoint(event.pos):
                        text = gui_Input.main("tsp")
                        self.tsp_clicked(text)

                    if self.button3.rect.collidepoint(event.pos):
                        text = gui_Input.main("shortest")
                        self.shortest_clicked(text)
                    if self.input_box.collidepoint(event.pos):
                        # Toggle the active variable.
                        active = not active
                    else:
                        active = False
                    # Change the current color of the input box.
                    self.color = self.color_active if active else self.color_inactive

                if event.type == pygame.KEYDOWN:
                    if self.active:
                        if event.key == pygame.K_RETURN:
                            print(text)
                            text = ''
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode

            self.screen.fill((250, 250, 250))
            self.draw()

            pygame.display.update()


if __name__ == '__main__':
    gAlgo = GraphAlgo()
    g = gAlgo.load_from_json(r"..\data\A0.json")
    Gui(gAlgo)
