import json

"""
Dieses Programm passt die Mengenangaben eines Rezepts an eine gegebene Anzahl von Personen an.
"""


def load_recipe(json_string):
    """
    Wandelt einen JSON-String in ein Python-Dictionary um.
    """
    return json.loads(json_string)


def adjust_recipe(recipe, num_persons):
    """
    Passt die Mengenangaben eines Rezepts an die angegebene Anzahl von Personen an.
    """
    # Berechne den Skalierungsfaktor basierend auf der neuen Anzahl von Personen
    scale_factor = num_persons / recipe['servings']

    # Erstelle ein neues Dictionary mit angepassten Mengenangaben
    adjusted_ingredients = {
        ingredient: round(quantity * scale_factor, 2)
        for ingredient, quantity in recipe['ingredients'].items()
    }

    # Erstelle ein neues Rezept-Dictionary mit den angepassten Zutaten und der neuen Portionsgröße
    adjusted_recipe = {
        'title': recipe['title'],
        'ingredients': adjusted_ingredients,
        'servings': num_persons
    }

    return adjusted_recipe


if __name__ == '__main__':
    # Beispiel für die Datenstruktur eines Rezepts als JSON-String
    recipe_json = '{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, ' \
                  '"Minced Meat": 500}, "servings": 4} '

    # Rezept als Python-Dictionary laden
    recipe = load_recipe(recipe_json)

    # Neue Anzahl an Personen
    new_persons = 2

    # Rezept für die neue Anzahl an Personen anpassen
    adjusted_recipe = adjust_recipe(recipe, new_persons)

    # Ausgabe des angepassten Rezepts
    print('Angepasstes Rezept:', json.dumps(adjusted_recipe, indent=4))
