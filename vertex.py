# Author: Tayeb
# Date: 11/16/2022
# Purpose: LAb 4


RADIUS = 8
THICKNESS = 3
from cs1lib import *


class Vertex:
    def __init__(self, name, xcoordinate, ycordinate):
        self.name = name
        self.adj_list = []
        self.x = int(xcoordinate)
        self.y = int(ycordinate)

    def draw_vertex(self,r,g,b):
        set_fill_color(r,g,b)
        draw_circle(self.x,self.y,RADIUS)

    def draw_edge(self, reference,r,g,b):
        set_stroke_color(r,g,b)
        set_stroke_width(3)
        draw_line(self.x,self.y,reference.x,reference.y)

    def draw_edges(self,r,g,b):
        for v in self.adj_list:
            self.draw_edge(v,r,g,b)

    def within(self,mousex,mousey):
        return self.x - 5 <= mousex <= self.x + 5 and self.y - 5 <= mousey <= self.y + 5



    def __str__(self):
        string_list = ""
        for i in range(len(self.adj_list)):
            adj_names = self.adj_list[i].name
            if i == len(self.adj_list) - 1:
                string_list = string_list + adj_names
            else:
                string_list = string_list + adj_names + ","

        return str(self.name) + "; " + "Location: " + str(self.x) + ", " + str(self.y) + "; " + "Adjacent vertices: " + string_list
