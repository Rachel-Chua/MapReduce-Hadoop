#!/usr/bin/env python3

import sys

# Initialize variables to keep track of the current category and ingredient
current_category = None
current_ingredient = None
current_count = 0

# Read key-value pairs from standard input
for line in sys.stdin:
    # Strip leading/trailing whitespaces and split the line into category, ingredient, and count
    category, ingredient, count = line.strip().split('\t')
    
    # Convert count to an integer
    count = int(count)
    
    # Check if the current category and ingredient are different from the previous ones
    if current_category != category or current_ingredient != ingredient:
        # If they are different, print the result for the previous category and ingredient
        if current_category is not None and current_ingredient is not None:
            print(f"{current_category}\t{current_ingredient}\t{current_count}")
        
        # Update the current category, ingredient, and count
        current_category = category
        current_ingredient = ingredient
        current_count = count
    else:
        # If they are the same, add the count to the current count
        current_count += count

# Print the result for the last category and ingredient
if current_category is not None and current_ingredient is not None:
    print(f"{current_category}\t{current_ingredient}\t{current_count}")
