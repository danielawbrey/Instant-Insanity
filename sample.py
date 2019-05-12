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
        print(v) 
  
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
    number_of_cubes = 40
    number_of_faces = 6

    set_of_values = []
    selection_count_array = []
    value_list = []
    array_of_cubes = []
    cube = []
    pair = []
    solution_array = []

    class Node:
        opposite_pair_1 = []
        opposite_pair_2 = []
        opposite_pair_3 = []

    #node = Node()
    
puzzle = Puzzle()

def get_value_index(selection_value):
    for i in range (len(puzzle.set_of_values)):
        if(puzzle.set_of_values[i] == selection_value):
            #print(selection_value, i)
            return i 
            
def mark_selection(index):
    print('Updated selection count array:', puzzle.selection_count_array)
    print(' ')
    for i in range (len(puzzle.selection_count_array)):
        if(i == index):
            if(puzzle.selection_count_array[i] < 2):
                puzzle.selection_count_array[i] += 1
        '''
            else:
                #print(' ') 
                #print("Error: too many selections of value", puzzle.set_of_values[i])
                #print(' ') 
        '''

def make_selection(array_of_cubes):
    for i in range (len(array_of_cubes)):
        for j in range (len(array_of_cubes[i])):
            correct_solution_found = check_selection_correctness(array_of_cubes[i][j])
            if (correct_solution_found):
                puzzle.solution_array.append(array_of_cubes[i][j])
                for k in range (len(array_of_cubes[i][j])):
                    mark_selection(get_value_index(array_of_cubes[i][j][k]))                    
                break


def remove_half_solution(half_solution):
    copy_of_array = []

    available_pairs = []

    for i in range (len(half_solution)):
        for j in range (len(puzzle.array_of_cubes[i])):
            if (half_solution[i] != puzzle.array_of_cubes[i][j]):
                available_pairs.append(puzzle.array_of_cubes[i][j])
        copy_of_array.append(available_pairs)
        available_pairs = []

    return copy_of_array


    '''    
        for j in range (len(puzzle.array_of_cubes[i])):
            for k in range (len(puzzle.array_of_cubes[j])):
                if (half_solution[i] == puzzle.array_of_cubes[j][k]):
                    #print(half_solution[i], puzzle.array_of_cubes[i][j])
                    #print(i, puzzle.array_of_cubes[i][j])
                    print(puzzle.array_of_cubes[j][k])
                    #delete_list_item.delete(puzzle.array_of_cubes, i, j)
                    #del(puzzle.array_of_cubes[i][j])
    '''

def check_selection_correctness(cube_pair_selection):
    selection_is_correct = False
    for i in range (len(cube_pair_selection)):
        value_index = get_value_index(cube_pair_selection[i])
        for i in range(value_index):
            if (i == (value_index - 1) and puzzle.selection_count_array[i] < 2):
                selection_is_correct = True
    return selection_is_correct

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

        puzzle.value_list.append(get_puzzle_two_coloration(i))

        puzzle.pair.append(get_puzzle_two_coloration(i))

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

def main():
    assign_coloration()

    print(' ')
    print('Array of cubes')
    print('--------------')
    print(puzzle.array_of_cubes)
    print(' ')

    print('Set of values')
    print('--------------')
    puzzle.set_of_values = get_value_set()
    print(puzzle.set_of_values)
    print(' ')

    print('Count of each value')
    print('-------------------')
    print(get_value_count(get_value_set()))
    print(' ')

    puzzle.selection_count_array = get_selection_counter()

    print("Number of values: ", len(puzzle.set_of_values), ',', "number of cubes: ", len(puzzle.array_of_cubes))
    print(' ')

    if(len(puzzle.set_of_values) < len(puzzle.array_of_cubes)):
        print("Values are unequal to cubes,", "minimum obstacle at least", len(puzzle.set_of_values))
        print(' ')

        while(len(puzzle.set_of_values) < len(puzzle.array_of_cubes)):
            puzzle.array_of_cubes.pop()

        print('Reduced array of cubes')
        print('----------------------')
        print(puzzle.array_of_cubes)
        print(' ')

    print('Starting selection process')
    print('--------------------------')
    make_selection(puzzle.array_of_cubes)

    print('Half solution 1')
    print('---------------')
    print(puzzle.solution_array)
    print(' ')

    puzzle.array_of_cubes = remove_half_solution(puzzle.solution_array)

    print('New array of cubes with half solution removed')
    print('---------------------------------------------')
    print(puzzle.array_of_cubes)
    print(' ')

    puzzle.solution_array = []
    puzzle.selection_count_array = get_selection_counter()

    print('Starting selection process')
    print('--------------------------')
    make_selection(puzzle.array_of_cubes)

    print('Half solution 2')
    print('---------------')
    print(puzzle.solution_array)
    print(' ')

'''
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
                
    print ("Following is Depth First Traversal")
    g.DFS()
    print(' ')
    print(g.return_graph()) 
    print(' ')
'''

if __name__ == "__main__": 
    main()