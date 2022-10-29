menu = { "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00 }


    # Prompt user for items ONE per line untll ctrl D is pressed {EOF exception}
total = 0.00
while True:
    try:
        item = input("Item: ").title().strip()
        if item in menu:
            total += menu[item]
            total = round(total, 2)
            print("Total: ${:.2f}".format(total))
    except EOFError:
        print()
        #print(f"Total: ${total}")
        print("Total: ${:.2f}".format(total))
        break
    # Display the total cost of items to two decimal points prefixed by dollar sign

    # Print a new line

    # Input should be case insensitively - Title case
