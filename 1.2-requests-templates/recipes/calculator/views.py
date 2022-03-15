from multiprocessing import context
from django.shortcuts import render

DATA = {
    "omlet": {
        "яйца, шт": 2,
        "молоко, л": 0.1,
        "соль, ч.л.": 0.5,
    },
    "pasta": {
        "макароны, кг": 0.3,
        "сыр, кг": 0.05,
    },
    "buter": {
        "хлеб, ломтик": 1,
        "колбаса, ломтик": 1,
        "сыр, ломтик": 1,
        "помидор, ломтик": 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def recipes_calc(request, recipe_name):
    try:
        servings = int(request.GET.get("servings", 1))
    except ValueError as error_text:
        print("Error in servings calculation:", error_text)
        servings = 1
    context = {}
    recipe = DATA.get(recipe_name)
    if recipe:
        context = {"recipe": recipe}
        for key, value in recipe.items():
            context["recipe"][key] = value * servings
    return render(request, "calculator/index.html", context)
