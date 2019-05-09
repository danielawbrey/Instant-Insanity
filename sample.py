import math
import threading
import collections
from collections import defaultdict 

class Graph: 

    # Constructor 
    def __init__(self): 
  
        # default dictionary to store graph 
        self.graph = defaultdict(list) 
  
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    # A function used by DFS 
    def DFSUtil(self, v, visited): 
  
        # Mark the current node as visited and print it 
        visited = True
        print v, 
  
        # Recur for all the vertices adjacent to 
        # this vertex 
        for i in self.graph[v]: 
            if visited == False: 
                self.DFSUtil(i, visited)
  
    # The function to do DFS traversal. It uses 
    # recursive DFSUtil() 
    def DFS(self): 
        V = len(self.graph)  #total vertices 
  
        # Mark all the vertices as not visited 
        visited =[False]*(V) 
  
        # Call the recursive helper function to print 
        # DFS traversal starting from all vertices one 
        # by one 
        for i in range(V): 
            if visited[i] == False: 
                self.DFSUtil(i, visited) 

    def return_graph(self):
        #print(self.graph)
        return self.graph

class Puzzle:
    number_of_cubes = 6
    number_of_faces = 6

    set_of_values = []
    selection_count_array = []
    value_list = []
    array_of_cubes = []
    cube = []
    pair = []

    class Node:
        opposite_pair_1 = []
        opposite_pair_2 = []
        opposite_pair_3 = []

    #node = Node()
    
puzzle = Puzzle()

def get_value_index(selection_value):
    for i in range (len(puzzle.set_of_values)):
        if(puzzle.set_of_values[i] == selection_value):
            #print(i)
            return i 
            
def mark_selection(index):
    for i in range (len(puzzle.selection_count_array)):
        if(i == index):
            if(puzzle.selection_count_array < 2):
                puzzle.selection_count_array += 1
            else: 
                print("Error: too many selections of a value made")

def get_value_set():
    set_of_values = []
    for i in range (len(puzzle.value_list)):
        if(i == 0):
            set_of_values.append(puzzle.value_list[i]) 
        else:
            if not puzzle.value_list[i] in set_of_values:
                set_of_values.append(puzzle.value_list[i])
    
    return set_of_values

def get_value_count(set_of_values):
    value_count_array = []
    for i in range (len(puzzle.value_list)):
        for j in range(len(set_of_values)): 
            if not value_count_array:
                value_count_array = [0] * len(set_of_values)
            if puzzle.value_list[i] == set_of_values[j]:
                value_count_array[j] += 1

    return value_count_array

def get_selection_counter():
    selection_count_array = []
    for i in range (len(puzzle.set_of_values)):
        selection_count_array.append(0)

    return selection_count_array

def assign_coloration():

    for i in range ((puzzle.number_of_cubes * puzzle.number_of_faces)):

        puzzle.value_list.append(get_puzzle_one_coloration(i))

        #puzzle.pair.append(get_puzzle_one_coloration(i))
        puzzle.cube.append(get_puzzle_one_coloration(i))

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

def main():
    #thread1 = threading.Thread(target=traverse_graph, name='T1')
    #thread2 = threading.Thread(target=traverse_graph, name='T2')

    #thread1.start()
    #thread2.start()

    #thread1.join()
    #thread2.join()

    assign_coloration()
    print(puzzle.array_of_cubes)
    print(' ')

    puzzle.set_of_values = get_value_set()
    print(puzzle.set_of_values)
    print(' ')

    print(get_value_count(get_value_set()))
    print(' ')

    #puzzle.selection_counter_array = get_selection_counter()
    #print(puzzle.selection_counter_array)
    #print(' ')
    #mark_selection(get_value_index(29.0))
    
    g = Graph() 

    for i in range (len((puzzle.array_of_cubes))):
        for j in range(6):
            if(not (j+1) % 2 == 0):
                source = puzzle.array_of_cubes[i][j]
                #print(j, source)
            if((j+1) % 2 == 0):
                destination = puzzle.array_of_cubes[i][j]
                #print(j, destination)
                #print(source, destination)
                #print(int(source),int(destination))
                g.addEdge(int(source),int(destination))
                
    print "Following is Depth First Traversal"
    g.DFS()
    print(' ')
    print(g.return_graph()) 
    print(' ')

    print("Number of values:", len(puzzle.set_of_values), "Number of cubes:", len(puzzle.array_of_cubes))

if __name__ == "__main__": 
    main()