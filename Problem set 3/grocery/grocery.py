grocery_dictionary = {}


while True:
    try:
        item = input().upper()
        if item in grocery_dictionary:
            grocery_dictionary[item] += 1

        else:
            grocery_dictionary[item] = 1



    except EOFError:
        for item in sorted(grocery_dictionary.keys()):
            print(grocery_dictionary[item],item)
        break