import Puzzle as puzzle_object

def main():
    puzzle = puzzle_object.Puzzle(40)

    puzzle.assign_coloration()

    print(' ')
    print('Array of cubes')
    print('--------------')
    print(puzzle.array_of_cubes)
    print(' ')
    print('Set of values')
    print('--------------')
    puzzle.set_of_values = puzzle.get_value_set()
    print(puzzle.set_of_values)

    print(' ')
    print('Count of each value')
    print('-------------------')
    print(puzzle.get_value_count(puzzle.get_value_set()))

    print(' ')
    puzzle.selection_count_array = puzzle.get_selection_counter()

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
    puzzle.make_selection(puzzle.array_of_cubes)
    print(' ')

    print('Half solution 1')
    print('---------------')
    print(len(puzzle.solution_array))
    print(puzzle.solution_array)
    print(' ')

    puzzle.array_of_cubes = puzzle.remove_half_solution(puzzle.solution_array)

    print('New array of cubes with half solution removed')
    print('---------------------------------------------')
    print(puzzle.array_of_cubes)
    print(' ')

    puzzle.solution_array = []
    puzzle.selection_count_array = puzzle.get_selection_counter()

    print('Starting selection process')
    print('--------------------------')
    puzzle.make_selection(puzzle.array_of_cubes)
    print(' ')

    print('Half solution 2')
    print('---------------')
    print(len(puzzle.solution_array))
    print(puzzle.solution_array)
    print(' ')

if __name__ == "__main__": 
    main()