# # Author: Tayeb
# # Date: 11/16/2022
# # Purpose: LAb 4
#
from collections import deque
from vertex import *
from load_graph import *

def bfs(start,goal):
    visited_dict = {}
    frontier = deque()
    frontier.append(start)
    visited_dict[start] = None

    while len(frontier) != 0:
        curr_v = frontier.popleft()
        for v in curr_v.adj_list:
            if v not in visited_dict:
                frontier.append(v)
                visited_dict[v] = curr_v
        if goal in visited_dict:
            break

    path = []
    v = goal

    print("vis dict")
    for x in visited_dict.keys():
        print(x.name)
    while v is not None:
        print("on v ", v.name)

        path.append(v)
        #print("hey")
        if v in visited_dict:
            print("In dict")
        else:
            print("not in dict: ", v.name)
            return None
        v = visited_dict[v]
        #print("hey2")

    return path
#
x = bfs(dict["Blunt"],dict["Gilman"])

for i in x:
    print(i)
    print(i.name)
