spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names=[]
    for spicy_food in spicy_foods:
        names.append(spicy_food["name"])
    return names


def get_spiciest_foods(spicy_foods):
    spicy=[]
    for spicy_food in spicy_foods:
        if spicy_food["heat_level"]>5:
            spicy.append(spicy_food)
    return spicy

        

def print_spicy_foods(spicy_foods):
    for spicy_food in spicy_foods:
        high_heat_re = "🌶" * spicy_food["heat_level"]
        print(f'{spicy_food["name"]} ({spicy_food["cuisine"]}) | Heat Level: {high_heat_re}')


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for spicy_food in spicy_foods:
        if spicy_food["cuisine"] == cuisine:
            return spicy_food

def print_spiciest_foods(spicy_foods):
    for spicy_food in spicy_foods:
        high_heat_rep = "🌶" * spicy_food["heat_level"]
        if spicy_food["heat_level"]>5:
            print(f'{spicy_food["name"]} ({spicy_food["cuisine"]}) | Heat Level: {high_heat_rep}')

def get_average_heat_level(spicy_foods):
    spiciest=[]
    for spicy_food in spicy_foods:
        spiciest.append(spicy_food["heat_level"])
    avarage= sum(spiciest)/ len(spiciest)
    return avarage
    


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods