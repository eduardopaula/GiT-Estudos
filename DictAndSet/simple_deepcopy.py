from contents import recipes

def my_deepcopy(d: dict) -> dict:
    """
    Copy a dictionary, creating copies of the `list`or `dict`values.

    The function will crash with AttributeError if the values aren't
    lists or dictionaries.

    :param d: The dictionary to copy.
    :return: A copy of `d, with the values being copies of the original values.
    """
    saida = {}
    for key, value in d.items():
        new_value = value.copy()
        saida[key] = new_value
    return saida


recipes_copy = my_deepcopy(recipes)
print(recipes_copy)

recipes_copy = my_deepcopy(recipes)
recipes_copy["Butter chicken"]["ginger"] = 300
print(recipes_copy["Butter chicken"]["ginger"])
print(recipes["Butter chicken"]["ginger"])
