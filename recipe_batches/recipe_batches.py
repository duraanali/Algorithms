#!/usr/bin/python

import math
import operator


def recipe_batches(recipe, ingredients):
    batches = {}
    print("Recipe Items", recipe.items())

    for item, amount in recipe.items():
        if item not in ingredients:
            return 0
        batches[item] = ingredients[item] // amount
        print("batches[item]", batches[item])
    return min(batches.items(), key=operator.itemgetter(1))[1]


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
