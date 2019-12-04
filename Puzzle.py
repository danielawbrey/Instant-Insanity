import math
import threading
import collections
from collections import defaultdict 

class Puzzle:
    def __init__(self, number_of_cubes):
        self.number_of_cubes = number_of_cubes
        self.number_of_faces = 6
        self.solution_array = []
        self.selection_count_array = []
        self.value_count_array = []
        self.value_list = []
        self.array_of_cubes = []

        self.assign_coloration()
        self.set_of_values = self.get_value_set()
        self.value_count_array = self.get_value_count()
        self.selection_count_array = self.get_selection_counter()
    
    def get_value_index(self,selection_value):
        for i in range (len(self.set_of_values)):
            if(self.set_of_values[i] == selection_value):
                return i 
                
    def mark_selection(self,pair_selection):
        for i in range(len(pair_selection)):
            index = self.get_value_index(pair_selection[i])
            for j in range(len(self.selection_count_array)):
                if(j == index):
                    self.selection_count_array[j] += 1

    def make_selection(self,array_of_cubes):
        error_counter = 0
        for i in range(len(array_of_cubes)):
            for j in range(len(array_of_cubes[i])):
                if (self.check_selection(array_of_cubes[i][j])):
                    self.solution_array.append(array_of_cubes[i][j])
                    print('Selection made for row', i, '-', array_of_cubes[i][j])
                    self.mark_selection(array_of_cubes[i][j])
                    #print('Updated selection count array:', self.selection_count_array)
                    break
                else:
                    error_counter += 1
                    if(error_counter == len(array_of_cubes[i])):
                        #print('Selection impossible for cube', i, '-', array_of_cubes[i])
                        error_counter = 0

    def remove_half_solution(self,half_solution):
        copy_of_array = []
        available_pairs = []
        for i in range (24):
            for j in range (len(self.array_of_cubes[i])):
                if (half_solution[i] != self.array_of_cubes[i][j]):
                    available_pairs.append(self.array_of_cubes[i][j])
            copy_of_array.append(available_pairs)
            available_pairs = []
        self.array_of_cubes = copy_of_array
        self.solution_array = []
        return self.array_of_cubes

    # TODO: Refactor 
    def check_selection(self,cube_pair_selection):
        pair_selection_counter = 0
        selection_is_correct = False
        for i in range(len(cube_pair_selection)):
            index = self.get_value_index(cube_pair_selection[i])
            for j in range(len(self.selection_count_array)):
                if(j == index and self.selection_count_array[j] < 2):
                    pair_selection_counter += 1
                    if(pair_selection_counter == 2):
                        selection_is_correct = True
                        pair_selection_counter = 0 
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

    def get_value_count(self):
        self.value_count_array = [0] * len(self.set_of_values)
        for i in range(len(self.array_of_cubes)):
            for j in range(len(self.array_of_cubes[i])):
                for k in range(len(self.array_of_cubes[i][j])):
                    if(self.array_of_cubes[i][j][k] in self.set_of_values):
                        self.mark_value_occurence(self.get_value_index(self.array_of_cubes[i][j][k])) 
        return self.value_count_array

    def mark_value_occurence(self,index):
        for i in range(len(self.set_of_values)):
            if(i == index):
                self.value_count_array[i] += 1

    def get_selection_counter(self):
        selection_count_array = []
        for i in range (len(self.set_of_values)):
            selection_count_array.append(0)
        return selection_count_array

    def assign_coloration(self):
        cube = []
        pair = []
        for i in range ((self.number_of_cubes * self.number_of_faces)):
            self.value_list.append(self.get_puzzle_four_coloration(i))
            pair.append(self.get_puzzle_four_coloration(i))
            if ((i + 1) % 2 == 0):
                cube.append(pair)
                pair = []
            if((i + 1) % 6 == 0):
                self.array_of_cubes.append(cube)
                cube = []
                                
    def get_puzzle_one_coloration(self,cube_face):
        return(1 + (math.floor(cube_face * math.pi) % 30))    

    def get_puzzle_two_coloration(self,cube_face):
        return(1 + (math.floor(cube_face * math.e) % 30))   

    def get_puzzle_three_coloration(self,cube_face):
        return(1 + (math.floor(cube_face * math.sqrt(3)) % 30))   

    def get_puzzle_four_coloration(self,cube_face):
        return(1 + (math.floor(cube_face * math.sqrt(5)) % 30))