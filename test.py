# TODO: At least 2 characters
# Max 6 characters
# First number can't be a 0, numbers only at the end
# No periods, spaces, or punctuation marks are allowed


def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False
    if s[0] == "0":
        return False
    for i in range(len(s)):
        if s[i].isalpha():
            return False
    return True


main()
