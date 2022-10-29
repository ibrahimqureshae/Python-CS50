# Get the expression

x , y , z = input("Expression: ").strip().split()

x = float(x)
z = float(z)

# Split the expression to variables

# Perform the operations

match y:
    case "+":
        print(x + z)
    case "-":
        print(x - z)
    case "/":
        print(x / z)
    case "*":
        print(x * z)


# Output the result