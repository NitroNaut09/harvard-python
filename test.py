def main():
    amount_due = 50
    total_inserted = 0

    while total_inserted < amount_due:
        coin = int(input("Insert a coin (25, 10, or 5 cents): "))
        if coin in [25, 10, 5]:
            total_inserted += coin
            print(f"Amount due: {amount_due - total_inserted} cents remaining")
        else:
            print("Invalid coin. Please insert 25, 10, or 5 cents.")

    change = total_inserted - amount_due
    print(f"You inserted enough coins. Your change is: {change} cents.")


if __name__ == "__main__":
    main()
