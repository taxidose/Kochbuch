from scraper import get_data
from ui import UI
from database import save_new_recipe, connect_to_db, get_recipe_by_title, TABLE_LIST, create_table, \
    get_all_recipe_titles
from time import sleep


def main():
    db = connect_to_db("recipe.db")
    for table in TABLE_LIST:
        create_table(db, table)
    interface = UI
    while True:
        choice = interface.home()

        if choice == "0":
            new_recipe_data = get_data()
            save_new_recipe(db, new_recipe_data)

        elif choice == "1":
            print(""
                  "Zufälliges Rezept tbd"
                  "")  # TODO: zufälliges rezept implementieren
            sleep(2)

        elif choice == "2":
            recipe_title = input("Rezeptname eingeben: ")
            recipe = get_recipe_by_title(db, recipe_title)
            print(recipe)

        elif choice == "3":
            recipes = get_all_recipe_titles(db)
            print()
            print(recipes)

        print()
        input("Enter drücken zum Fortfahren...")


if __name__ == "__main__":
    main()
