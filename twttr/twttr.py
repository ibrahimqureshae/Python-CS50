# Take an Input
input = input("Input: ")

# iterate through input for AEIOU
# Print Non AEIOU Only.
for character in input:
    if character not in ["A","E","I","O","U","a","e","i","o","u"]:
        print(character, end="")

# New line
print()

