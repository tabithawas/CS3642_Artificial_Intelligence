# Course: CS 3642
# Assignment #: 2
# Due Date: 10/24/24

from tkinter import *
import heapq
import random
import time

goal_puzzle = [1, 2, 3, 8, 0, 4, 7, 6, 5]

generated_puzzle = []
generated_puzzle_string = ""

output_puzzle = []
output_puzzle_string = ""

stats_string = ""

def update_labels(): 
    global generated_puzzle

    generated_puzzle_label.config(text=generated_puzzle_string)

    output_puzzle_label.config(text=output_puzzle_string)

    stats_label.config(text=stats_string)

def clicked_generate_puzzle(): 
    global generated_puzzle 
    global generated_puzzle_string
    
    generated_puzzle = generate_eight_puzzle()

    generated_puzzle_string = format_matrix(generated_puzzle)

    update_labels()

def clicked_ucs(): 
    global generated_puzzle
    global output_puzzle_string
    global output_puzzle
    global stats_string

    if not generated_puzzle: 
        clicked_generate_puzzle()

    # Start the timer 
    start = time.time()

    # Get the results from ucs 
    results = ucs(generated_puzzle, goal_puzzle)

    # Stop the time 
    end = time.time()

    output_puzzle = results[0]
    visited = results[1]
    time_ms = (end-start) * 10**3

    stats_string = "\nNodes visited: " + str(visited) + "\n\nTime (ms, rounded): " + str(round(time_ms))

    output_puzzle_string = format_matrix(output_puzzle)

    update_labels()

def clicked_manhattan(): 
    global generated_puzzle
    global output_puzzle_string
    global output_puzzle
    global stats_string

    if not generated_puzzle: 
        clicked_generate_puzzle()

    # Start the timer 
    start = time.time()

    # Get the results from ucs 
    results = a_star_manhattan(generated_puzzle, goal_puzzle)

    # Stop the time 
    end = time.time()

    output_puzzle = results[0]
    visited = results[1]
    time_ms = (end-start) * 10**3

    stats_string = "\nNodes visited: " + str(visited) + "\n\nTime (ms, rounded): " + str(round(time_ms))

    output_puzzle_string = format_matrix(output_puzzle)

    update_labels()

def clicked_nilsson(): 
    global generated_puzzle
    global output_puzzle_string
    global output_puzzle
    global stats_string

    if not generated_puzzle: 
        clicked_generate_puzzle()

    # Start the timer 
    start = time.time()

    # Get the results from ucs 
    results = a_star_nilsson(generated_puzzle, goal_puzzle)

    # Stop the time 
    end = time.time()

    output_puzzle = results[0]
    visited = results[1]
    time_ms = (end-start) * 10**3

    stats_string = "Nodes visited: " + str(visited) + "\n\nTime (ms, rounded): " + str(round(time_ms))

    output_puzzle_string = format_matrix(output_puzzle)

    update_labels()

# Setup tkinter root 
root = Tk()
root.title("Assignment #2 - 8-Puzzle")
root.configure(height = 650, width = 750)

# Place the buttons 
button_generate_puzzle = Button(root, text="Generate Puzzle", background="gray", cursor="hand2", height=5, width=15, command=clicked_generate_puzzle)
button_generate_puzzle.place(x=30, y=30)

button_ucs = Button(root, text="UCS", background="gray", cursor="hand2", height=5, width=15, command=clicked_ucs)
button_ucs.place(x=30, y=150)

button_manhattan = Button(root, text="A* Manhattan", background="gray", cursor="hand2", height=5, width=15, command=clicked_manhattan)
button_manhattan.place(x=30, y=270)

button_nilsson = Button(root, text="A* Nilsson", background="gray", cursor="hand2", height=5, width=15, command=clicked_nilsson)
button_nilsson.place(x=30, y=390)

# Place the labels 
generated_puzzle_label = Label(root, text=generated_puzzle_string, font="Sans", background="gray", width=25, height=10)
generated_puzzle_label.place(x=200, y=30)

output_puzzle_label = Label(root, text=output_puzzle_string, font="Sans", background="gray", width=25, height=10)
output_puzzle_label.place(x=200, y=270)

stats_label = Label(root, text=stats_string, font="Sans", background="gray", width=25, height=10)
stats_label.place(x=480, y=30)

##### General puzzle operations  #####

def format_matrix(puzzle): 
    matrix = puzzle_to_matrix(puzzle)

    output_string = ""
    for row in matrix: 
        output_string += "\n"
        output_string += str(row[0])
        output_string += "\t"
        output_string += str(row[1])
        output_string += "\t"
        output_string += str(row[2])
        output_string += "\n"

    return output_string

# Generate random puzzle 
def generate_eight_puzzle(): 
    # Goal state before shuffle 
    nums = [1, 2, 3, 8, 0, 4, 7, 6, 5]

    shuffled_puzzle = nums[:]

    # Shuffle puzzle to get a solvable, random puzzle 
    num_shuffles = random.randint(0, 10000)
    for i in range(num_shuffles): 

        direction = random.randint(0, 3)
        
        shuffled_puzzle = swap(shuffled_puzzle, direction)

    return shuffled_puzzle

# Find blank square
def find_blank_square(puzzle): 
    for i in range(len(puzzle)): 
        if puzzle[i] == 0: 
            return i
    return -1

# Swap the puzzle as needed/desired 
# 0 is up, 1 is down, 2 is left, and 3 is right
def swap(puzzle, direction): 
    # Get the index of the blank square 
    blank_square_index = find_blank_square(puzzle)

    new_index = -1
    
    # Get index for swap 
    if direction == 0 and blank_square_index >= 3: 
        new_index = blank_square_index - 3
    if direction == 1 and blank_square_index <= 5: 
        new_index = blank_square_index + 3
    if direction == 2 and (blank_square_index != 0 or blank_square_index != 3 or blank_square_index != 6): 
        new_index = blank_square_index - 1
    if direction == 3 and (blank_square_index != 2 or blank_square_index != 5 or blank_square_index != 8): 
        new_index = blank_square_index + 1

    swapped_puzzle = puzzle[:]

    # Perform the swap if possible 
    if (new_index >= 0 and new_index <= 8): 
        num = puzzle[new_index]

        swapped_puzzle[blank_square_index] = num
        swapped_puzzle[new_index] = 0

        return swapped_puzzle
    else: 
        return swapped_puzzle

# Generate the swap options for puzzle solving 
def generate_options(puzzle): 
    options = []

    # Generate the options (up, down, left, and right swap branches if possible)
    puzzle_up = swap(puzzle, 0)
    if len(puzzle_up) > 0: 
        options.append(puzzle_up)

    puzzle_down = swap(puzzle, 1)
    if len(puzzle_down) > 0: 
        options.append(puzzle_down)

    puzzle_left = swap(puzzle, 2)
    if len(puzzle_left) > 0: 
        options.append(puzzle_left)

    puzzle_right = swap(puzzle, 3)
    if len(puzzle_right) > 0: 
        options.append(puzzle_right)

    return options

##### Manhattan Distance #####

def a_star_manhattan(starting_puzzle, goal_puzzle): 
    
    # Set up variables 
    visited = set()
    heap_set = set()

    start = (0, starting_puzzle)

    puzzle_pq = []

    heapq.heappush(puzzle_pq, start)
    heap_set.add(tuple(starting_puzzle))

    prev_cost = 0

    while len(puzzle_pq) > 0: 

        prev_cost, puzzle = heapq.heappop(puzzle_pq)
        heap_set.remove(tuple(puzzle))

        if tuple(puzzle) == tuple(goal_puzzle): 
            print("\nReached Goal State")
            print(puzzle)
            return puzzle, len(visited)
        
        if tuple(puzzle) not in visited: 
            visited.add(tuple(puzzle))

        options = generate_options(puzzle)

        # Determine if the option has been visited, queued, or is empty 
        for option in options: 
            if tuple(option) not in visited and tuple(option) not in heap_set and option != []: 
                # Calculate the heuristic and add to the queue 
                option_manhattan_distance = calculate_manhattan_heuristic(option, goal_puzzle)
                option_total = calculate_manhattan_total(option_manhattan_distance)
                new_cost = option_total + prev_cost
                new_entry = (new_cost, option)
                heapq.heappush(puzzle_pq, new_entry)
                heap_set.add(tuple(option))

    # Return nothing if the puzzle isn't solvable 
    print("\nNot Solvable")
    return [], -1

# Calculate the manhattan heuristic 
def calculate_manhattan_heuristic(puzzle, goal_puzzle): 

    # Convert the puzzle to a 3x3 matrix 
    puzzle_matrix = puzzle_to_matrix(puzzle)

    # Convert the goal puzzle to a 3x3 matrix 
    goal_matrix = puzzle_to_matrix(goal_puzzle)

    # Get the indices of the goal matrix  
    goal_indices = {}
    for row in goal_matrix: 
        for num in row: 
            row, column = find_square(goal_matrix, num)
            goal_indices[num] = row, column 

    # Get the indices of the puzzle matrix 
    puzzle_indices = {}
    for row in puzzle_matrix: 
        for num in row: 
            row, column = find_square(puzzle_matrix, num)
            puzzle_indices[num] = row, column 

    # Calculate and store the distances in a dictionary 
    distances = {}
    for i in range(len(goal_indices.keys())): 
        row_diff = abs(goal_indices[i][0] - puzzle_indices[i][0])
        column_diff = abs(goal_indices[i][1] - puzzle_indices[i][1])
        diff = row_diff + column_diff
        distances[i] = diff

    return distances

# Convert a single array puzzle to a 3x3 matrix 
def puzzle_to_matrix(puzzle): 
    row_one = puzzle[:3]
    row_two = puzzle[3:6]
    row_three = puzzle[6:]

    matrix = [row_one, row_two, row_three]
    
    return matrix

# Calculate the total of the manhattan distances 
def calculate_manhattan_total(distances): 
    total = 0
    for i in range(len(distances.keys())): 
        total += distances[i] 
    return total

# Find row and column of the blank square
def find_square(matrix, num): 
    row = -1 
    column = -1
    
    for row_index in range(len(matrix)): 
        if num in matrix[row_index]: 
            row = row_index
        for column_index in range(len(matrix)): 
            if matrix[row_index][column_index] == num: 
                column = column_index
    
    return row, column

##### Nilsson's Sequence ##### 

def a_star_nilsson(starting_puzzle, goal_puzzle): 
    
    # Set up variables 
    visited = set()
    heap_set = set()

    start = (0, starting_puzzle)

    puzzle_pq = []

    heapq.heappush(puzzle_pq, start)
    heap_set.add(tuple(starting_puzzle))

    prev_cost = 0

    while len(puzzle_pq) > 0: 

        prev_cost, puzzle = heapq.heappop(puzzle_pq)
        heap_set.remove(tuple(puzzle))

        if tuple(puzzle) == tuple(goal_puzzle): 
            print("\nReached Goal State")
            print(puzzle)
            return puzzle, len(visited)
        
        if tuple(puzzle) not in visited: 
            visited.add(tuple(puzzle))

        options = generate_options(puzzle)

        for option in options: 
            if tuple(option) not in visited and tuple(option) not in heap_set and option != []: 
                option_manhattan_dist = calculate_manhattan_heuristic(option, goal_puzzle)
                clockwise_tot = clockwise_total(option)
                manhattan_tot = calculate_manhattan_total(option_manhattan_dist)
                new_cost = ((3 * clockwise_tot) + manhattan_tot) + prev_cost
                new_entry = (new_cost, option)
                heapq.heappush(puzzle_pq, new_entry)
                heap_set.add(tuple(option))

    # Return nothing if the puzzle isn't solvable 
    print("\nNot Solvable")
    return [], -1

# Calculate the tile displacement total for Nilsson's Sequence 
def clockwise_total(puzzle): 
    
    total = 0

    matrix = puzzle_to_matrix(puzzle)

    clockwise_order = [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (1, 0), (1, 1)]

    for row in matrix: 
        for num in row: 
            num_row, num_column = find_square(matrix, num)
            index = clockwise_order.index((num_row, num_column))
            if index == 7: 
                index = 0
            if num_row == 1 and num_column == 1: 
                if matrix[1][1] != 0: 
                    total += 1
            elif num == 0: 
                continue 
            elif num <= 7: 
                next_row, next_column = clockwise_order[index + 1]
                next_num = matrix[next_row][next_column]
                if num + 1 != next_num: 
                    total += 2
            elif num == 8: 
                next_row, next_column = clockwise_order[index]
                next_num = matrix[next_row][next_column]
                if 1 != next_num: 
                    total += 2

    return total

##### UCS ##### 

# Perform uniform cost search on the given puzzle to find the goal puzzle 
def ucs(starting_puzzle, goal_puzzle): 
    
    # Set up variables 
    visited = set()
    heap_set = set()

    start = (0, starting_puzzle)

    puzzle_pq = []

    heapq.heappush(puzzle_pq, start)
    heap_set.add(tuple(starting_puzzle))

    cost = 0

    while len(puzzle_pq) > 0: 

        cost, puzzle = heapq.heappop(puzzle_pq)
        heap_set.remove(tuple(puzzle))

        if tuple(puzzle) == tuple(goal_puzzle): 
            print("\nReached Goal State")
            print(puzzle)
            return puzzle, len(visited)
        
        if tuple(puzzle) not in visited: 
            visited.add(tuple(puzzle))

        options = generate_options(puzzle)        

        for option in options: 
            if tuple(option) not in visited and tuple(option) not in heap_set: 
                new_cost = cost + 1
                new_entry = (new_cost, option)
                heapq.heappush(puzzle_pq, new_entry)
                heap_set.add(tuple(option))

    # Return nothing if the puzzle isn't solvable 
    print("\nNot Solvable")
    return [], -1

# Call the mainloop 
root.mainloop()