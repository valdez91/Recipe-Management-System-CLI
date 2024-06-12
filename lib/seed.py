#!/usr/bin/env python3

from models.__init__ import get_db_connection
from models.Recipes import add_recipe
from models.Ingredients import add_ingredient
from models.RecipeIngredients import add_recipe_ingredient

def seed_database():
    conn = get_db_connection()

    # Add seed data for Recipes
    add_recipe("Pasta Carbonara", "Delicious pasta carbonara recipe.")
    add_recipe("Chicken Curry", "Spicy chicken curry with rice.")
    add_recipe("Chocolate Cake", "Decadent chocolate cake recipe.")

    # Add seed data for Ingredients
    add_ingredient("Spaghetti")
    add_ingredient("Bacon")
    add_ingredient("Eggs")
    add_ingredient("Parmesan Cheese")
    add_ingredient("Chicken")
    add_ingredient("Curry Paste")
    add_ingredient("Rice")
    add_ingredient("Chocolate")
    add_ingredient("Flour")
    add_ingredient("Sugar")
    add_ingredient("Cocoa Powder")

    # Add seed data for RecipeIngredients
    # You'll need to fetch the IDs of recipes and ingredients as necessary
    # For simplicity, I'll just assume some IDs here
    add_recipe_ingredient(1, 1, "200g")
    add_recipe_ingredient(1, 2, "100g")
    add_recipe_ingredient(1, 3, "2")
    add_recipe_ingredient(1, 4, "50g")
    add_recipe_ingredient(2, 5, "500g")
    add_recipe_ingredient(2, 6, "100g")
    add_recipe_ingredient(2, 7, "200g")
    add_recipe_ingredient(2, 8, "200g")
    add_recipe_ingredient(3, 9, "300g")
    add_recipe_ingredient(3, 10, "200g")
    add_recipe_ingredient(3, 11, "100g")

    conn.close()

if __name__ == "__main__":
    seed_database()
    print("Seeded database")
