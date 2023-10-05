# Author: Tayeb
# Date: 11/16/2022
# Purpose: LAb 4

from vertex import Vertex


def load_graph(filename):

    vertex_dict = {}
    file = open(filename, "r")

    for line in file:
        section_split = line.split(";")
        vertex_name = section_split[0].strip()
        coordinates = section_split[2].split(",")
        x = coordinates[0].strip()
        y = coordinates[1].strip()
        v_obj = Vertex(vertex_name, x, y)
        vertex_dict[vertex_name] = v_obj

    file.close()


    file = open(filename, "r")
    for line in file:
        data_list = line.split(";")

        vertex_name = data_list[0].strip()
        adjacent_list = data_list[1].split(",")

        for element in adjacent_list:
            vertex_dict[vertex_name].adj_list.append(vertex_dict[element.strip()])


    file.close()
    return vertex_dict

dict =load_graph("dartmouth_graph.txt")
# print(x.values().name)

