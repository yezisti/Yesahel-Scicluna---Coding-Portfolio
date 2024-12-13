# Generate a representation of a random UK bingo card

'''
Task Description:
Write a program which generates UK Bingo cards (90 numbers). Create a 3x9
grid for the Bingo card. Ensure no duplicate numbers appear on the card.
Column 1 should contain numbers 1-9, column 2 should contain numbers 10-19,
..., column 9 should contain numbers 80-90. Each rowcontains exactly 5 numbers
and 4 blank spaces, totalling 15 numbers on the entire card. After placing
numbers in the grid, ensure that the numbers within each column are sorted
in ascending order. Each column (and row) must contain at least one number.
Each column should align neatly for readability
'''

import random

# Initialise an empty 9x3 list of lists by which to encode the bingo card
card = [[None for col in range(9)] for row in range(3)]

# Fill column 1 with 3 sorted random numbers
random_nums = []
while len(random_nums) < 3 :
    random_num = random.randint(1, 9)
    if random_num not in random_nums:
        random_nums.append(random_num)
random_nums.sort()
for row in range(3):          
    card[row][0] = random_nums[row]

# Fill columns 2-9 with 3 sorted random numbers each
for col in range(1, 9):
    random_nums = []
    while len(random_nums) < 3 :
        random_num = random.randint((col * 10), (col * 10 + 9))
        if random_num not in random_nums:
            random_nums.append(random_num)
    random_nums.sort()
    for row in range(3):          
        card[row][col] = random_nums[row]

# Remove 12 numbers randomly, making sure to leave at least one number per row
# and column
total_removed = 0
while total_removed < 12:
    random_row = random.randint(0, 2)
    random_col = random.randint(0, 8)
    row_count = 0
    for col in range(9):
        if card[random_row][col] is not None:
            row_count += 1
        if row_count == 2:
            break
    col_count = 0
    for row in range(3):
        if card[row][random_col] is not None:
            col_count += 1
        if col_count == 2:
            break   
    if col_count == 2 and row_count == 2:
        if card[random_row][random_col] is not None:
            card[random_row][random_col] = None
            total_removed += 1 

# Print the bingo card
print("--" * 23)
for row in range(3):
    for col in range(9):
        if card[row][col] is not None: 
            print(f"| {card[row][col]:02} ", end="")
        else:
            print("|    ", end="")
    print("|", "--" * 23, sep="\n")
