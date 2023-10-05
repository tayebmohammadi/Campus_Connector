# Author: Tayeb
# Date: 11/16/2022
# Purpose: LAb 4


from vertex import *
from bfs import *
from load_graph import *

img = load_image("dartmouth_map.png")
WINDOW_WEIGHT = 1012
WINDOW_HEIGHT = 811
FRAMERATE = 10
MPRESSED = False
MMOVE = False
press_x = 0
press_y = 0

start = None
goal = None

def draw_main():
    global press_x,press_y, MMOVE, MPRESSED,start,goal

    clear()
    draw_image(img, 0, 0)
    dictionary = load_graph("dartmouth_graph.txt")
    for v in dictionary:
        dictionary[v].draw_vertex(0,0,1)
        dictionary[v].draw_edges(0,0,1)



    for k in dictionary:
        if dictionary[k].within(press_x,press_y) and MPRESSED:
            start = dictionary[k]


    for n in dictionary:
        if dictionary[n].within(press_x, press_y) and start is not None:
            goal = dictionary[n]

            goal.draw_vertex(1,0,0)

            print(start.name)
            print(goal.name)
            path = bfs(dictionary[start.name], dictionary[goal.name])
            if path != None:
                for g in path:
                    g.draw_vertex(1, 0, 0)
            #for g in path:
                #g.draw_vertex(1, 0, 0)



    if start != None:
        start.draw_vertex(1, 0, 0)

    # if goal != None and start != None:
    #     path = bfs(start,goal)
    #
            #g.draw_edges(1, 0, 0)


def mousepress(px,py):
    global press_x,press_y, MPRESSED
    MPRESSED = True

    press_x = px
    press_y = py


def mouserelease(mx,my):
    global MPRESSED
    MPRESSED = False


def mousemove(mx, my):
    global press_x,press_y, MMOVE
    MMOVE = True

    press_x = mx
    press_y = my



start_graphics(draw_main, width=WINDOW_WEIGHT, height=WINDOW_HEIGHT, framerate = FRAMERATE,mouse_press=mousepress,mouse_move=mousemove,mouse_release=mouserelease)











