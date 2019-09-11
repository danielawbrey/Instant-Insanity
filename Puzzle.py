import math
import threading
import collections
from collections import defaultdict 

class Puzzle:
    def __init__(self, number_of_cubes):
        self.number_of_cubes = number_of_cubes
        self.number_of_faces = 6
        self.set_of_values = []
        self.selection_count_array = []
        self.value_list = []
        self.array_of_cubes = []
        self.cube = []
        self.pair = []
        self.solution_array = []
    
    def get_value_index(self,selection_value):
        for i in range (len(self.set_of_values)):
            if(self.set_of_values[i] == selection_value):
                #print(selection_value, i)
                return i 
                
    def mark_selection(self,index):
        #print('Updated selection count array:', self.selection_count_array)
        #print(' ')
        for i in range (len(self.selection_count_array)):
            if(i == index):
                if(self.selection_count_array[i] < 2):
                    self.selection_count_array[i] += 1
                else:
                    #print(' ') 
                    #print("Error: too many selections of value", self.set_of_values[i])
                    #print(' ')
                    return self.set_of_values[i]

    def make_selection(self,array_of_cubes):
        cube_selection_made = False
        value_error = None 
        number_of_incorrect_selections = 0

        for i in range (len(array_of_cubes)):
            for j in range (len(array_of_cubes[i])):
                correct_solution_found = self.check_selection_correctness(array_of_cubes[i][j])
                if (correct_solution_found):
                    cube_selection_made = True
                    for k in range (len(array_of_cubes[i][j])):
                        value_error = self.mark_selection(self.get_value_index(array_of_cubes[i][j][k]))
                    self.solution_array.append(array_of_cubes[i][j])
                    #print('Selection made:', array_of_cubes[i][j])
                    #print('Updated selection count array:', self.selection_count_array)
                    break
                else:
                    number_of_incorrect_selections += 1
                    if (number_of_incorrect_selections > 2): # No selections in the row are possible; backtrack
                            print("No element selection possible for cube", i, '...', 'too many selections of value', value_error)
            number_of_incorrect_selections = 0

    def remove_half_solution(self,half_solution):
        copy_of_array = []

        available_pairs = []

        for i in range (24):
            for j in range (len(self.array_of_cubes[i])):
                if (half_solution[i] != self.array_of_cubes[i][j]):
                    available_pairs.append(self.array_of_cubes[i][j])
            copy_of_array.append(available_pairs)
            available_pairs = []
        return copy_of_array

    def check_selection_correctness(self,cube_pair_selection):
        selection_is_correct = False
        for i in range (len(cube_pair_selection)):
            value_index = self.get_value_index(cube_pair_selection[i])
            for i in range(value_index):
                if (i == (value_index - 1) and self.selection_count_array[i] < 2):
                    selection_is_correct = True
        return selection_is_correct

    def get_value_set(self):
        set_of_values = []
        for i in range (len(self.value_list)):
            if(i == 0):
                set_of_values.append(self.value_list[i]) 
            else:
                if not self.value_list[i] in set_of_values:
                    set_of_values.append(self.value_list[i])
        
        return set_of_values

    def get_value_count(self,set_of_values):
        value_count_array = []
        for i in range (len(self.value_list)):
            for j in range(len(set_of_values)): 
                if not value_count_array:
                    value_count_array = [0] * len(set_of_values)
                if self.value_list[i] == set_of_values[j]:
                    value_count_array[j] += 1

        return value_count_array

    def get_selection_counter(self):
        selection_count_array = []
        for i in range (len(self.set_of_values)):
            selection_count_array.append(0)

        return selection_count_array

    def assign_coloration(self):
        for i in range ((self.number_of_cubes * self.number_of_faces)):

            self.value_list.append(self.get_puzzle_four_coloration(i))

            self.pair.append(self.get_puzzle_four_coloration(i))

            if ((i + 1) % 2 == 0):
                self.cube.append(self.pair)
                self.pair = []

            if((i + 1) % 6 == 0):
                self.array_of_cubes.append(self.cube)
                self.cube = []
                                
    def get_puzzle_one_coloration(self,cube_face):
        return(1 + (math.floor(cube_face * math.pi) % 30))    

    def get_puzzle_two_coloration(self,cube_face):
        return(1 + (math.floor(cube_face * math.e) % 30))   

    def get_puzzle_three_coloration(self,cube_face):
        return(1 + (math.floor(cube_face * math.sqrt(3)) % 30))   

    def get_puzzle_four_coloration(self,cube_face):
        return(1 + (math.floor(cube_face * math.sqrt(5)) % 30))