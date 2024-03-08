# There are four collection data types in the Python programming language:
#
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    #  "year": 2020, #  não aceita duplicidade
}
print(thisdict)

print(thisdict["year"])
print(len(thisdict))
print(type(thisdict))
thisdict = dict(name="John", age=36, country="Norway")
print(thisdict)

##############################################################
# acessar o valor de um item

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "color": "Red",
    "km": 45000,
    "last": "John Doe",
}
x = thisdict["model"]
x = thisdict.get("model")
x = thisdict.keys()
print('Chaves:', x)
x = thisdict.values()
print('Valores: ', x)
x = thisdict.items()
print(x, type(x))

thisdict["color"] = "blue"
print(thisdict)

if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

thisdict["year"] = 2018
print('Atualizar:', thisdict)
thisdict.update({"year": 2020})
print('Update:', thisdict)
thisdict.pop("model")
print('Remover POP:', thisdict)
thisdict.popitem()
print('Remover último item inserido:', thisdict)
del thisdict["year"]
print('Remover DEL: ', thisdict)

for keys, values in thisdict.items():
    print(keys, values)


child1 = {
    "name" : "Emil",
    "year" : 2004
}
child2 = {
    "name" : "Tobias",
    "year" : 2007
}
child3 = {
    "name" : "Linus",
    "year" : 2011
}

myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}

print(myfamily["child2"]["name"])
