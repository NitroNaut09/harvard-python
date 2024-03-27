while True:
    try:
        frac = input("Fraction: ")
        x, y = frac.split("/")
        percentage = int(x) / int(y) * 100

        def fuel():
            if percentage <= 0.01:
                return "E"
            elif percentage <= 1:
                return "F"
            else:
                return f"{percentage:.2f}%"

        print(fuel())

    except ValueError:
        print("Error: Please enter a valid fraction.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
