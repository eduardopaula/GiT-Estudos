numbers = (0, 1, 2, 3, 4, 5)

# print(numbers, sep=";")
# print(numbers, numbers, sep=";")
# print(*numbers, sep=";")
# print(0, 1, 2, 3, 4, 5, sep=";")


def tet_star(*args):
    print(args)
    for x in args:
        print(x)


tet_star(0, 1, 2, 3, 4, 5)
