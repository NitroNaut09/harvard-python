def main():
    expression = input("Enter an arithmetic expression (e.g., 1 + 1): ")
    result = calculate(expression)
    print(f"Result: {result:.1f}")


def calculate(expression):
    x, operator, z = expression.split()
    x = float(x)
    z = float(z)
    if operator == "+":
        return x + z
    elif operator == "-":
        return x - z
    elif operator == "*":
        return x * z
    elif operator == "/":
        return x / z


if __name__ == "__main__":
    main()
