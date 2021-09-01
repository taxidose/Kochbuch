class Recipe:
    def __init__(self, title, ingredients, portions, instruction, times, tags, url):
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
{self.title}
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


class Ingredient:
    def __init__(self, name):
        self.name = name
