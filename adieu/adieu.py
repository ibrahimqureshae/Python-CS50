import inflect

p = inflect.engine()
name_list = []



while True:
        try:
                name = input("Name: ")
                name_list.append(name)
        except:
                break



# Perform the function
names = p.join(name_list)
print(f"Adieu, adieu, to " + names)