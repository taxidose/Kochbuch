import sqlite3
from sqlite3 import Error
from classes import Recipe

CREATE_TABLE_RECIPES = """CREATE TABLE IF NOT EXISTS recipes (
                                        title TEXT PRIMARY KEY,
                                        instruction TEXT NOT NULL,
                                        times TEXT,                                        
                                        rating REAL,
                                        url TEXT
                                    );"""

CREATE_TABLE_INGREDIENTS = """CREATE TABLE IF NOT EXISTS ingredients (
                                        name TEXT PRIMARY KEY                                        
                                    );"""

CREATE_TABLE_RECIPE_INGREDIENTS = """CREATE TABLE IF NOT EXISTS recipe_ingredients (
                                        recipe_title TEXT NOT NULL,
                                        ingredient_amount TEXT,
                                        ingredient_name TEXT NOT NULL,
                                        portions INTEGER,
                                        FOREIGN KEY (recipe_title) REFERENCES recipes (title) ON DELETE CASCADE,
                                        FOREIGN KEY (ingredient_name) REFERENCES ingredients (name)                                        
                                    );"""

CREATE_TABLE_RECIPE_TAGS = """CREATE TABLE IF NOT EXISTS recipe_tags (
                                        recipe_title TEXT NOT NULL,
                                        tag TEXT NOT NULL,
                                        FOREIGN KEY (recipe_title) REFERENCES recipes (title) ON DELETE CASCADE                                                                               
                                    );"""

TABLE_LIST = [CREATE_TABLE_RECIPES, CREATE_TABLE_INGREDIENTS, CREATE_TABLE_RECIPE_INGREDIENTS,
              CREATE_TABLE_RECIPE_TAGS]


def connect_to_db(path):
    conn = None
    try:
        conn = sqlite3.connect(path)
        print(f"[INFO] DB-Connection established ({path})")
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
        table_ = create_table_sql.split()[5]
        print(f"[INFO] Table {table_} ok")
    except Error as e:
        print(f"[ERROR] {e}, ({create_table_sql})")


def insert_into(conn, insert_into_sql, values: tuple):
    try:
        c = conn.cursor()
        c.execute(insert_into_sql, values)
        conn.commit()
        # print(f"[INFO] Entry inserted ({insert_into_sql})")
    except Error as e:
        print(f"[ERROR] {e} ({insert_into_sql})")


def save_new_recipe(conn, recipe: dict):
    sql_recipe_table = "INSERT INTO recipes (title, instruction, times, url) VALUES (?, ?, ?, ?)"
    recipe_values = (recipe["title"], recipe["instruction"], recipe["times"], recipe["url"])
    insert_into(conn, sql_recipe_table, recipe_values)

    try:
        c = conn.cursor()

        sql_ingredients_insert = "INSERT OR IGNORE INTO ingredients VALUES (?)"
        ingredient_list = [ingredient[1] for ingredient in recipe["ingredients"]]
        for ingredient in ingredient_list:
            c.execute(sql_ingredients_insert, (ingredient,))

        sql_recipe_ingredients_insert = "INSERT OR IGNORE INTO recipe_ingredients VALUES (?, ?, ?, ?)"
        recipe_ingredients_values = [(recipe["title"], ingredient[0], ingredient[1], recipe["portions"]) for ingredient
                                     in recipe["ingredients"]]
        c.executemany(sql_recipe_ingredients_insert, recipe_ingredients_values)

        sql_recipe_tags_insert = "INSERT OR IGNORE INTO recipe_tags VALUES (?, ?)"
        recipe_tags_values = [(recipe["title"], tag) for tag in recipe["tags"]]
        c.executemany(sql_recipe_tags_insert, recipe_tags_values)

        conn.commit()

        print(f"[INFO] {recipe['title']} successfully saved in DB")

    except Error as e:
        print(f"[ERROR] {e} [save_new_recipe()]")


def get_recipe_by_title(conn, title):
    sql_recipe = "SELECT * FROM recipes WHERE title LIKE ?"
    title_value = (f"{title}%",)

    sql_recipe_ingredients = "SELECT * FROM recipe_ingredients WHERE recipe_title LIKE ?"

    sql_recipe_tags = "SELECT * FROM recipe_tags WHERE recipe_title LIKE ?"

    try:
        c = conn.cursor()
        c.execute(sql_recipe, title_value)
        recipe = c.fetchone()
        c.execute(sql_recipe_ingredients, title_value)
        ingredients = c.fetchall()
        portions = ingredients[0][3]
        ingredients = [(ingredient[1], ingredient[2]) for ingredient in ingredients]

        c.execute(sql_recipe_tags, title_value)
        tags = c.fetchall()
        tags = [tag[1] for tag in tags]

        return Recipe(recipe[0], ingredients, portions, recipe[1], recipe[2], tags,
                      recipe[4])

    except Error as e:
        print(f"[ERROR] {e}")

    except IndexError:
        return "Rezept nicht gefunden..."


def get_all_recipe_titles(conn):
    sql = "SELECT * FROM recipes"

    try:
        c = conn.cursor()
        c.execute(sql)
        recipes = c.fetchall()
        recipe_titles = [title[0] for title in recipes]

        if not recipes:
            return "Keine Rezepte gespeichert..."

        return recipe_titles


    except Error as e:
        print(f"[ERROR] {e}")