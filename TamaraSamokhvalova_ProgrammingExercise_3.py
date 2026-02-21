from functools import reduce

# Function to calculate total expense
def calculate_total(expenses):
    return reduce(lambda x, y: x + y[1], expenses, 0)


# Function to find the highest expense
def find_highest(expenses):
    return reduce(lambda x, y: x if x[1] > y[1] else y, expenses)


# Function to find the lowest expense
def find_lowest(expenses):
    return reduce(lambda x, y: x if x[1] < y[1] else y, expenses)


# Main function
def main():
    count = int(input("How many expenses do you have? "))
    expenses = []

    for i in range(count):
        name = input("Enter expense name: ")
        amount = float(input("Enter expense amount: "))
        expenses.append((name, amount))

    total = calculate_total(expenses)
    highest = find_highest(expenses)
    lowest = find_lowest(expenses)

    print("\nTotal expense:", total)
    print("Highest expense:", highest[0], "-", highest[1])
    print("Lowest expense:", lowest[0], "-", lowest[1])

# Call the main function
main()