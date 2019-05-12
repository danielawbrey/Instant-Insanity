import math
import threading
import collections
#import networkx as nx
#import numpy as np

class Graph(object):
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size


'''
    def addEdge(self, v1, v2):
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def removeEdge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def containsEdge(self, v1, v2):
        return True if self.adjMatrix[v1][v2] > 0 else False

    def __len__(self):
        return self.size
        
    def toString(self):
        for row in self.adjMatrix:
            for val in row:
                print('{:4}'.format(val)),
            print
    '''

class Puzzle:
    number_of_cubes = 6
    number_of_faces = 6

    dictionary = {}
    adjacency_matrix = {}

    value_list = []
    array_of_cubes = []
    cube = []
    pair = []

    class Dictionary(dict):
        def __init__(self):
            self = dict() 

        def addValue(self, key, value):
            self[key].append(value)

        def addKey(self, key):
            self[key] = []

    class Node:
        opposite_pair_1 = []
        opposite_pair_2 = []
        opposite_pair_3 = []

    #node = Node()
    
puzzle = Puzzle()

def assign_coloration():

    for i in range ((puzzle.number_of_cubes * puzzle.number_of_faces)):

        puzzle.value_list.append(get_puzzle_one_coloration(i))

        puzzle.pair.append(get_puzzle_one_coloration(i))

        if ((i + 1) % 2 == 0):
            puzzle.cube.append(puzzle.pair)
            puzzle.pair = []

        if((i + 1) % 6 == 0):
            puzzle.array_of_cubes.append(puzzle.cube)
            puzzle.cube = []
            
def get_puzzle_one_coloration(cube_face):
    return(1 + (math.floor(cube_face * math.pi) % 30))    

def get_puzzle_two_coloration(cube_face):
    return(1 + (math.floor(cube_face * math.e) % 30))   

def get_puzzle_three_coloration(cube_face):
    return(1 + (math.floor(cube_face * math.sqrt(3)) % 30))   

def get_puzzle_four_coloration(cube_face):
    return(1 + (math.floor(cube_face * math.sqrt(5)) % 30))        

def create_dictionary(value_list):
    puzzle.dictionary = puzzle.Dictionary()
    for i in range(len(value_list)):
        if value_list[i] in puzzle.dictionary:
            puzzle.dictionary.addValue(value_list[i], value_list[i])

        else:     
            puzzle.dictionary.addKey(value_list[i])

def create_adjacency_matrix(value_list):
    vertices = {}
    puzzle.adjacency_matrix = puzzle.Dictionary()
    for i in range(len(value_list)):
        if not value_list[i] in puzzle.adjacency_matrix:
            puzzle.adjacency_matrix.addKey(value_list[i])

   # for key in puzzle.adjacency_matrix.items():
        #for value in puzzle.adjacency_matrix.items():
            #puzzle.adjacency_matrix.addValue(key, value)

        #for j in range(len(puzzle.adjacency_matrix)):
            #puzzle.adjacency_matrix.addValue(key, key)

    #print(puzzle.adjacency_matrix)

def create_histogram(dictionary):
    print("********** Histogram **********")
    for i in range(len(dictionary)):
        if not dictionary[puzzle.value_list[i]]:
            print( puzzle.value_list[i], 1)
        else: 
            print(puzzle.value_list[i], len(dictionary[puzzle.value_list[i]]) + 1)
    print("*******************************")

def traverse_graph():
    print(threading.currentThread().getName())

def main():
    #thread1 = threading.Thread(target=traverse_graph, name='T1')
    #thread2 = threading.Thread(target=traverse_graph, name='T2')

    #thread1.start()
    #thread2.start()

    #thread1.join()
    #thread2.join()

    assign_coloration()
    #print('\n')
    #print("Cube coloration:", puzzle.array_of_cubes)
    create_dictionary(puzzle.value_list)
    print('\n')
    print("Number of values:", len(puzzle.dictionary), "Number of cubes:", len(puzzle.array_of_cubes))
    print('\n')
    create_histogram(puzzle.dictionary)
    print('\n')
    create_adjacency_matrix(puzzle.value_list)

    graph = Graph(puzzle.number_of_cubes)

    for i in range(len(puzzle.array_of_cubes)):
        for j in range(len(puzzle.array_of_cubes[i])):
            for k in range(len(puzzle.array_of_cubes[i][j])):
                graph.addEdge(puzzle.array_of_cubes[i][j][k],puzzle.array_of_cubes[i][j][k])
                print(puzzle.array_of_cubes[i][j][k])

    #graph.addEdge(0, 1)
    #graph.addEdge(0, 2)
    #graph.addEdge(1, 2)
    #graph.addEdge(2, 0)
    #graph.addEdge(2, 3)
    #graph.toString()   

if __name__ == "__main__": 
    main()