# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 19:24:50 2023

@author: PC
"""

import pandas as pd

# Read the CSV file into a DataFrame
recipe_data = pd.read_csv('recipes.csv', low_memory=False)

def is_numeric(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def clean_recipe_ingredients(recipe_id, recipe_cat, ingredients_str):
    # Skip the line if the RecipeId is not numeric or RecipeCategory or RecipeIngredientParts field is empty
    if not is_numeric(recipe_id) or pd.isnull(recipe_cat) or pd.isnull(ingredients_str):
        return ""
    
    # Check if the value is NaN
    if pd.isnull(ingredients_str):
        return ""  # Return an empty string or some default value
    
    # Remove 'c(' and ')' characters from the IngredientParts column
    ingredients_str = ingredients_str.replace('c(', '').replace(')', '')

    # Split the string by commas and remove any extra whitespace and quotes
    ingredients_list = [ingredient.strip().strip('\"') for ingredient in ingredients_str.split(",")]

    # Convert the list back to a comma-separated string
    ingredients_str_cleaned = ", ".join(ingredients_list)

    return ingredients_str_cleaned

# Clean the format of "RecipeIngredientParts" column and convert it to a comma-separated string
recipe_data["RecipeIngredientParts"] = recipe_data.apply(lambda row: clean_recipe_ingredients(row["RecipeId"], row["RecipeCategory"], row["RecipeIngredientParts"]), axis=1)

# Drop rows where "RecipeIngredientParts" is empty after cleaning
recipe_data = recipe_data[recipe_data["RecipeIngredientParts"] != ""]

def find_ingredient_counts(recipe_data):
    ingredient_count_result = []

    for index, recipe in recipe_data.iterrows():
        ingredients = recipe["RecipeIngredientParts"]
        recipe_category = recipe["RecipeCategory"] 
        for ingredient in ingredients.split(", "):
            ingredient_count_result.append({
                "RecipeCategory": recipe_category,
                "Ingredient": ingredient,
                "Count": 1
            })

    return ingredient_count_result

# Perform ingredient count analysis for all recipes
ingredient_count_result = find_ingredient_counts(recipe_data)

# Create a DataFrame to store the ingredient count
ingredient_count_df = pd.DataFrame(ingredient_count_result)

# Group the DataFrame by "RecipeCategory" and "Ingredient" and sum the "Count" for each group
ingredient_count_df = ingredient_count_df.groupby(["RecipeCategory", "Ingredient"], as_index=False)["Count"].sum()

# Save the DataFrame to a CSV file directly 
ingredient_count_df.to_csv('ingredient_count_results.csv', index=False)
