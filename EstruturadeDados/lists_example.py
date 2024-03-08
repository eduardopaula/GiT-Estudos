# There are four collection data types in the Python programming language:
#
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.



# Exemplo
mylist = ["apple", "banana", "cherry"]

print('inicia no 0:', mylist[0])

#thislist = ["apple", "apple", "cherry", "banana", "cherry"]
thislist = ["apple", "apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print('aceita duplicidade, [thislist]:', thislist)
print('comprimento da lista:', len(thislist))
print('Tipo:', type(thislist))

# -1 refers to the last item, -2 refers to the second last item etc.
print('thislist[-1]: ', thislist[-1])

print('thislist[2:5]', thislist[2:5])  # inicia no segundo item "cherry" e vai até o 5 não incluso
print('thislist[:4]', thislist[:4])  # inicia no começo até "kiwi" item não incluso (começa no 0)
print('thislist[2:]', thislist[2:])  # inicia em "cherry" até o final

if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

##############################################################
# alterar o valor de um item na lista

thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

##############################################################
# Adicionar valores

thislist = ["apple", "banana", "cherry"]
thislist.insert(0, "watermelon")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

##############################################################
# Apagar valores

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

##############################################################
# Loop

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

##############################################################
# Ordenação

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

##############################################################
# Cópia

# list2 = list1 vai manter a referencia e não realizar cópia, logo
# uma alteração em uma irá refletir em outra

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)


##############################################################
# Junção

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)
