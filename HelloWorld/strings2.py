number = "9,223;372:036 854,775;807"
separators = ""
sobra = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char
    else:
        sobra = sobra + char

print(separators)
print(sobra)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])
