from scraper import get_data
from ui import UI
from database import save_new_recipe, connect_to_db, get_recipe_by_title, TABLE_LIST, create_table, \
    get_all_recipe_titles
from time import sleep
from classes import Recipe
from telegram_bot import send_msg

DB_PATH = r"C:\Users\taxi\Nextcloud\Sicherung\recipe.db"


def main():
    db = connect_to_db(DB_PATH)
    for table in TABLE_LIST:
        create_table(db, table)
    interface = UI
    while True:
        choice = interface.home()

        if choice == "0":
            new_recipe_data = get_data()
            save_new_recipe(db, new_recipe_data)

        elif choice == "9":
            new_custom_recipe = Recipe()
            new_custom_recipe.update()
            save_new_recipe(db, new_custom_recipe.as_dict())

        elif choice == "1":
            print(""
                  "Zufälliges Rezept tbd"
                  "")  # TODO: zufälliges rezept implementieren
            sleep(2)

        elif choice == "2":
            recipe_title = input("Rezeptname eingeben: ")
            recipe = get_recipe_by_title(db, recipe_title)

            if recipe:
                print(recipe)
                choice_recipe_menu = interface.recipe_menu()
                if choice_recipe_menu == "1":
                    send_msg(recipe.ingredients_formatted())

        elif choice == "3":
            recipes = get_all_recipe_titles(db)
            print()
            print(recipes)

        print()
        input("Enter drücken um fortzufahren...")


if __name__ == "__main__":
    main()
