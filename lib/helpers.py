# helpers.py
from models import get_db_connection
from models.Recipes import add_recipe, get_all_recipes, get_recipe_by_id,  update_recipe as update_recipe_model, delete_recipe as delete_recipe_model
from models.Ingredients import add_ingredient, get_ingredient_by_name, get_all_ingredients
from models.RecipeIngredients import add_recipe_ingredient, get_ingredients_for_recipe, get_recipes_for_ingredient

def exit_program():
    print("Goodbye!")
    exit()

def list_recipes():
    recipes = get_all_recipes()
    for recipe in recipes:
        print(f"{recipe['id']}. {recipe['name']}")

def find_recipe_by_name():
    name = input("Enter the recipe's name: ")
    recipes = get_all_recipes()
    for recipe in recipes:
        if recipe['name'].lower() == name.lower():
            print_recipe(recipe['id'])
            return
    print(f"Recipe '{name}' not found")

def find_recipe_by_id():
    id_ = input("Enter the recipe's id: ")
    recipe = get_recipe_by_id(id_)
    if recipe:
        print_recipe(recipe['id'])
    else:
        print(f"Recipe '{id_}' not found")

def create_recipe():
    name = input("Enter the recipe's name: ")
    ingredients_input = input("Enter ingredients (format: ingredient1, quantity1; ingredient2, quantity2): ")
    instructions = input("Enter instructions: ")

    ingredients_list = [i.strip() for i in ingredients_input.split(';')]
    add_recipe(name, instructions)
    recipe_id = get_all_recipes()[-1]['id']

    for item in ingredients_list:
        ingredient_name, quantity = item.split(',')
        ingredient = get_ingredient_by_name(ingredient_name.strip())
        if not ingredient:
            add_ingredient(ingredient_name.strip())
            ingredient_id = get_ingredient_by_name(ingredient_name.strip())['id']
        else:
            ingredient_id = ingredient['id']

        add_recipe_ingredient(recipe_id, ingredient_id, quantity.strip())

    print(f"Recipe '{name}' added successfully.")

def update_recipe():
    id_ = input("Enter the recipe's id: ")
    recipe = get_recipe_by_id(id_)
    if recipe:
        # Convert sqlite3.Row to dictionary
        recipe_dict = dict(recipe)

        new_name = input("Enter new recipe name (leave blank to keep current): ")
        new_ingredients = input("Enter new ingredients (leave blank to keep current): ")
        new_instructions = input("Enter new instructions (leave blank to keep current): ")

        if new_name:
            recipe_dict['name'] = new_name
        if new_ingredients:
            # Delete old ingredients
            conn = get_db_connection()
            c = conn.cursor()
            c.execute("DELETE FROM RecipeIngredients WHERE recipe_id = ?", (id_,))
            conn.commit()
            conn.close()
            ingredients_list = [i.strip() for i in new_ingredients.split(';')]
            for item in ingredients_list:
                ingredient_name, quantity = item.split(',')
                ingredient = get_ingredient_by_name(ingredient_name.strip())
                if not ingredient:
                    add_ingredient(ingredient_name.strip())
                    ingredient_id = get_ingredient_by_name(ingredient_name.strip())['id']
                else:
                    ingredient_id = ingredient['id']

                add_recipe_ingredient(id_, ingredient_id, quantity.strip())

        if new_instructions:
            recipe_dict['instructions'] = new_instructions

        # Use the correct update function
        update_recipe_model(id_, recipe_dict['name'], recipe_dict['instructions'])
        print(f"Recipe '{recipe_dict['name']}' updated successfully.")
    else:
        print(f"Recipe '{id_}' not found")



def delete_recipe():
    id_ = input("Enter the recipe's id: ")
    if get_recipe_by_id(id_):
        delete_recipe_model(id_)
        print(f"Recipe '{id_}' deleted successfully.")
    else:
        print(f"Recipe '{id_}' not found")

def search_recipes_by_ingredient():
    ingredient_name = input("Enter the ingredient's name: ")
    ingredient = get_ingredient_by_name(ingredient_name)
    if not ingredient:
        print(f"Ingredient '{ingredient_name}' not found")
        return
    recipes = get_recipes_for_ingredient(ingredient['id'])
    if not recipes:
        print(f"No recipes found containing '{ingredient_name}'")
        return

    for recipe in recipes:
        print(f"{recipe['id']}. {recipe['name']}")

def print_recipe(recipe_id):
    recipe = get_recipe_by_id(recipe_id)
    ingredients = get_ingredients_for_recipe(recipe_id)
    print(f"Recipe ID: {recipe['id']}")
    print(f"Name: {recipe['name']}")
    print("Ingredients:")
    for ingredient in ingredients:
        print(f"  - {ingredient['name']}: {ingredient['quantity']}")
    print("Instructions:")
    print(recipe['instructions'])
