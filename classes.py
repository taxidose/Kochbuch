class Recipe:
    def __init__(self, title=None, ingredients=None, portions=None, instruction=None, times=None, tags=None, url=None):
        self.title = title
        self.ingredients = ingredients
        self.portions = portions
        self.instruction = instruction
        self.times = times
        self.tags = tags
        self.rating = 0
        self.url = url

    def __repr__(self):
        return f"""Recipe("{self.title}", {self.ingredients}, {self.portions}, "{self.instruction[:30]}...", "{self.times}", "{self.tags}")"""

    def __str__(self):
        return f"""
        
----------------------------------------------        
----------------------------------------------        
{self.title.upper()}
----------------------------------------------
----------------------------------------------

Zutaten für {self.portions} Portionen:
{self.ingredients}

----------------------------------------------

{self.instruction}

----------------------------------------------
{self.times}
----------------------------------------------
Tags: {self.tags}
----------------------------------------------
Rating: {self.rating}
----------------------------------------------
"""

    def as_dict(self):
        return {"title": self.title, "ingredients": self.ingredients, "portions": self.portions,
                "instruction": self.instruction, "times": self.times,
                "tags": self.tags, "url": self.url}

    def update(self):
        self.title = input("Rezeptname: ")
        ingredients_list = input("Zutaten (z.B. 3 Eier, 1L Bier, etwas Salz): ").split(", ")
        ingredients_tuple_list = []
        for ingredient in ingredients_list:
            ingredient_tuple = tuple(ingredient.split())
            ingredients_tuple_list.append(ingredient_tuple)
        self.ingredients = ingredients_tuple_list
        self.portions = input("Portionen: ")
        self.instruction = input("Anleitung: ")
        self.times = input("Zeit: ")
        self.tags = input("Tags: ")
        self.url = input("Url: ")

        # print(f"Rezept {self.title} aktualisiert")

    def ingredients_formatted(self):
        ingredients_string = ""
        for ingredient in self.ingredients:
            ingredients_string += f"- {ingredient[0]} {ingredient[1]}\n"

        return f"{self.title} ({self.portions} Portionen)\n" \
               f"-------------------------------------\n" \
               f"{ingredients_string}" \
               f"-------------------------------------"






class Ingredient:
    def __init__(self, name):
        self.name = name
