while True:
    try:
        x,y = input("Fraction: ").strip().split(sep = "/")
        # each x and y are integers
        x = int(x)
        y = int(y)
        percentage = round((x/y)*100)
        if percentage<=100:
            if percentage <= 1:
                print("E")
            elif percentage >=99:
                print("F")
            else:
                print(f"{percentage}%")
            break
    except (ValueError, ZeroDivisionError):
        pass

# Output a percentage rounded off to nearest integer


