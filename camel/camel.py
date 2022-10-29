# Prompt the name in camel case
camelCase = input("Camel case: ")
new_string = ""

# iterate string. if upper => insert _ and then concatenate else only concatenate
for character in camelCase:
    if character.isupper():
        new_string = new_string + "_" + character
    else:
        new_string += character

# lowercase all letters
new_string = new_string.lower()

# Output the name in snake case
print(new_string)