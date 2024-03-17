# Input takes an argument itself


def app():
    """
    A function that prompts the user to enter something and then prints it.
    """
    print(input("Enter something: "))


app()

# Parameters to the functions.

# For print function:
print(*objects, sep=" ", end="\n", file=sys.stdout, flush=False)

""" * means to multiply, and object means the string itself. Since there is no value for objects, it means that the print functions can take any number of strings.

Separator is used to separate the objects in the string. The default value is ' ' (a space).

End is used to end the string. The default value is '\n' (a newline).

File is used to specify the file to which the output should be written. The default value is sys.stdout.

Flush is used to flush the output buffer. The default value is False.
"""

# For example, we can modify the values of the parameters of the print function as follows:

print(1, 2, 3, sep="--")

# IF we insist on using double quotes but still want to print quotes, we can use an escape character. For eg;

print('I am "fine"')


# Example code:

name = input("Enter your name: ")
name = name.strip().title()
print(name)

# Conditional Statements


def is_even(x):
    return True if x % 2 == 0 else False


# Even cleaner code:
def even(n):
    return n % 2 == 0


# Match


name = input("Who are you? ")
if name in ["Harry Da Puttar", "Hermione", "Ron"]:
    print("GRIFYYNDORRRRRRRRR!!!!!!")
else:
    print("I don't know you!")


def sorting_hat(head):
    if head == "Gryffindor":
        return "Potter"
    elif head == "Hufflepuff":
        return "Snape"
    elif head == "Ravenclaw":
        return "Flitwick"
    else:
        return "Hagrid"


sorting_hat("Ravenclaw")


# Loops
