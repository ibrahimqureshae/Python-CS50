def check(x):
    if x == "42" or x == "FORTY TWO" or x ==  "FORTY-TWO":
        print("Yes")

    else:
        print("No")


def main():
    x = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().upper()
    check(x)



main()