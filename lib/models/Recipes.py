from . import get_db_connection

def add_recipe(name, instructions):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("INSERT INTO Recipes (name, instructions) VALUES (?, ?)", (name, instructions))
    conn.commit()
    conn.close()

def get_all_recipes():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT id, name FROM Recipes")
    recipes = c.fetchall()
    conn.close()
    return recipes

def get_recipe_by_id(recipe_id):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM Recipes WHERE id = ?", (recipe_id,))
    recipe = c.fetchone()
    conn.close()
    return recipe

def update_recipe(recipe_id, name, instructions):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("UPDATE Recipes SET name = ?, instructions = ? WHERE id = ?", (name, instructions, recipe_id))
    conn.commit()
    conn.close()

def delete_recipe(recipe_id):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("DELETE FROM RecipeIngredients WHERE recipe_id = ?", (recipe_id,))
    c.execute("DELETE FROM Recipes WHERE id = ?", (recipe_id,))
    conn.commit()
    conn.close()
