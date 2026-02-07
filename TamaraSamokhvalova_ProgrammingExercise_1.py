# Function 1: ask the user how many tickets they want
def ask_for_tickets():
    '''
    Prompts the user to enter the number of tickets they want to buy from 1-4.

    Parameters:
        None

    Variables:
        tickets(int): stores the number of tickets the user wants.

    Logic:
        1. prompt the user to enter the a number from 1-4.
        2. Convert the input to an integer.
        3. Return the number of tickets remaining.

    Return:
        tickets(int): the number of tickets the user wants.
    '''
    # Prompt the user to enter a number between 1 and 4
    tickets = int(input("How many tickets do you want to buy today (1 to 4)? "))

    # Return the user's input
    return tickets

# Function 2: run the ticket selling program
def sell_tickets():
    '''
    Ticket selling process, counts the buyers, updates the remaining tickets.

    Parameters:
        None

    Variables:
        tickets_left(int): the number of tickets remaining.
        buyers(int): accumulator counting the purchases.
        wanted(int): number of tickets the user wants.

    Logic:
        1. Count how many tickets are left
        2. Loop to get the remaining nuber of tickets.
        3. When all the tickets get sold, the program will display total number of buyers.

    Return:
        None
    '''

    tickets_left = 10
    buyers = 0
    while tickets_left > 0:
        # Display the currently number of tickets remaining
        print("Tickets remaining:", tickets_left)

        # Ask the user for the number of tickets requested
        wanted = ask_for_tickets()

        # Validate the number of tickets requested
        if wanted >= 1 and wanted <=4 and wanted <= tickets_left:
            tickets_left -= wanted
            buyers += 1
            print("Tickets remaining after purchase:", tickets_left)

        else:
            print("Invalid number of tickets.")

    print("All tickets have been sold.")

    print("Total number of buyers:", buyers)

#Run the program
if __name__ == "__main__":
    sell_tickets()