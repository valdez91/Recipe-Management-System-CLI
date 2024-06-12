from . import get_db_connection

def add_recipe_ingredient(recipe_id, ingredient_id, quantity):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("INSERT INTO RecipeIngredients (recipe_id, ingredient_id, quantity) VALUES (?, ?, ?)", (recipe_id, ingredient_id, quantity))
    conn.commit()
    conn.close()

def get_ingredients_for_recipe(recipe_id):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''
        SELECT Ingredients.name, RecipeIngredients.quantity
        FROM Ingredients
        JOIN RecipeIngredients ON Ingredients.id = RecipeIngredients.ingredient_id
        WHERE RecipeIngredients.recipe_id = ?
    ''', (recipe_id,))
    ingredients = c.fetchall()
    conn.close()
    return ingredients

def get_recipes_for_ingredient(ingredient_id):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''
        SELECT Recipes.id, Recipes.name
        FROM Recipes
        JOIN RecipeIngredients ON Recipes.id = RecipeIngredients.recipe_id
        WHERE RecipeIngredients.ingredient_id = ?
    ''', (ingredient_id,))
    recipes = c.fetchall()
    conn.close()
    return recipes
