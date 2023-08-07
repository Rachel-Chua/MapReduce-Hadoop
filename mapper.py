#!/usr/bin/env python3

import sys
import csv

def is_numeric(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# Read each line from input and process it
reader = csv.reader(sys.stdin)
for columns in reader:
    # Check if the line contains the expected number of columns
    if len(columns) < 28:
        continue

    # Extract relevant columns
    recipe_id = columns[0].strip()
    recipe_category = columns[10].strip()
    ingredients_str = columns[13].strip()

    # Skip the line if the RecipeId is not numeric or RecipeCategory or RecipeIngredientParts field is empty
    if not is_numeric(recipe_id) or not recipe_category or not ingredients_str:
        continue

    # Remove 'c(' and ')' characters from the IngredientParts column
    ingredients_str = ingredients_str.replace('c(', '').replace(')', '')

    # Split the string by commas and emit key-value pairs
    ingredients_list = [ingredient.strip().strip('\"') for ingredient in ingredients_str.split(",")]
    for ingredient in ingredients_list:
        # Emit key-value pairs where the key is a combination of "RecipeCategory" and "Ingredient"
        print(f"{recipe_category}\t{ingredient}\t1")
