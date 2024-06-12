from . import get_db_connection

def add_ingredient(name):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("INSERT INTO Ingredients (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

def get_ingredient_by_name(name):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT id FROM Ingredients WHERE name = ?", (name,))
    ingredient = c.fetchone()
    conn.close()
    return ingredient

def get_all_ingredients():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM Ingredients")
    ingredients = c.fetchall()
    conn.close()
    return ingredients
