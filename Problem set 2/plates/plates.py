def main():
    plate = input("Plate: ").upper().strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if  len(s) > 6 or len(s) < 2:
        return False


    if s[0:2].isalpha() == False:
        return False

    for character in s:
        if character.isalpha() == False:
            if character == "0":
                return False
            else:
                break

    for i in range(len(s)):
        if s[i].isdigit():
            if not s[i:].isdigit():
                return False

    if s.isalnum() == True:
        return True

main()
