food = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}

total_cost = 0  # Initialize the total cost to zero

while True:
    try:
        item = input("Item: ").title()
        if item in food:
            total_cost += food[item]
            print(f"Current Total Cost: ${total_cost:.2f}")
        else:
            print("We don't have that item")
    except ValueError:
        print("KEEP MY NAME OUT OF YOUR FISHING MOUTH!")
    except EOFError:
        break  # Exit the loop when EOFError occurs
