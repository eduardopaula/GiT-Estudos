available_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat",
                  "hdmi cable",
                  "dvd"
                  ]

#valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))

current_choise = "-"
computer_parts = [] # create an empty list

while current_choise != '0':
    if current_choise in valid_choices:
        index = int(current_choise) - 1
        chosen_part = available_parts[index]
        print("Index: {}".format(str(index)))
        print("Chosen part: {}".format(chosen_part))
        if chosen_part in computer_parts:
            # it's already in, so remove it
            print("Removing {}".format(current_choise))
            computer_parts.remove(chosen_part)
        else:
            print("Adding {}".format(current_choise))
            computer_parts.append(chosen_part)
        print("Your list now contains: {}".format(computer_parts))
    else:
        print("Please add options from the list below:")
        for number, part in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, part))

    current_choise = input()

print(computer_parts)
