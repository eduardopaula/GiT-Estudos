menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    # ["chuva", ["spam", ["spam", ["spam"]]]],
]

# for meal in menu:
#     for item in meal:
#         if item != "spam":
#             print(item)
#     print()

for meal in menu:
    for index in range(len(meal) - 1, -1, -1):
        # for index in range(len(meal)):
        #     print(index)
        if meal[index] == "spam":
            del meal[index]

    print(meal)
