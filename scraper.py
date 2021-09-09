from bs4 import BeautifulSoup
import requests


def get_valid_url(url=None):
    if url is None:
        while True:
            url = input("Chefkoch URL eingeben: ")
            if len(url) > 20 and (url[:3] == "http" or "www."):
                return url
            print("Ungültige URL...")

    if len(url) > 20 and (url[:3] == "http" or "www."):
        return url

    return None


def get_data(url=None) -> dict:
    if not url:
        url = get_valid_url()
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, "lxml")

    try:
        title = soup.find("h1").text

        ingredients = soup.find_all("tr")

        ingredient_list = []

        for ingredient in ingredients:
            ingredient_name = ingredient.find("td", class_="td-right").text.strip()
            ingredient_amount = ingredient.find("td", class_="td-left").text.replace(" ", "").strip()
            ingredient_list.append((ingredient_amount, ingredient_name))

        # portions = soup.find_all("div", class_="recipe-servings ds-box")
        portions = soup.find("input", class_="ds-input").get("value")

        #instructions = soup.find_all("div", class_="ds-box")
        main_container = soup.find("main", class_="ds-container rds")
        instruction = main_container.find("article", class_="ds-or-3").find("div", class_="ds-box").text.strip()

        #tags = instructions[15].text.replace(" ", "").splitlines()

        tags = main_container.find_all("a", class_="ds-tag bi-tags")

        tags = [tag.text.strip() for tag in tags if tag]

        times = soup.find("small", class_="ds-recipe-meta rds-recipe-meta").text.replace("", "").replace(
            "                    ", "").replace("                ", "").splitlines()
        times = [time for time in times if time]

    except AttributeError as e:
        print(f"Fehler: ({e})")

    return {"title": title, "ingredients": ingredient_list, "portions": portions, "instruction": instruction,
            "times": " / ".join(times), "tags": tags, "url": url}


