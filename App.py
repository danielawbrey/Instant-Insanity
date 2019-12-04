import Puzzle as puzzle_object

def main():
    puzzle = puzzle_object.Puzzle(40)

    print(' ')
    print('Array of cubes')
    print('--------------')
    print(puzzle.array_of_cubes)

    print(' ')
    print('Set of values')
    print('--------------')
    print(puzzle.set_of_values)

    print(' ')
    print('Count of each value')
    print('-------------------')
    print(puzzle.value_count_array)

    print(' ')
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
    print('Solution length:', len(puzzle.solution_array))
    #print(puzzle.solution_array)
    print(' ')

    # Removes half solution from array of cubes used for selection
    puzzle.remove_half_solution(puzzle.solution_array)

    print('New array of cubes with half solution removed')
    print('---------------------------------------------')
    print(puzzle.array_of_cubes)
    print(' ')

    # Create empty selection counter
    puzzle.selection_count_array = puzzle.get_selection_counter()

    print('New value count')
    print('---------------')
    print(puzzle.get_value_count())
    print(' ')

    print('Starting selection process')
    print('--------------------------')
    puzzle.make_selection(puzzle.array_of_cubes)
    print(' ')

    print('Half solution 2')
    print('---------------')
    print('Solution length:', len(puzzle.solution_array))
    #print(puzzle.solution_array)
    print(' ')

if __name__ == "__main__": 
    main()