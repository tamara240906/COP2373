import random
class Deck():

    def __init__(self, size):
        # Create a list of numbers from 0 to size-1
        self.card_list = [i for i in range(size)]

        # Shuffle the deck randomly
        random.shuffle(self.card_list)
        self.current_card = 0
        self.size = size

    def deal(self):
        # If ran out of cards, reshuffle the deck
        if self.size - self.current_card < 1:
            random.shuffle(self.card_list)
            self.current_card = 0
            print("Reshuffling...!!!")

        # Move to the next card
        self.current_card += 1

        # Return the current card
        return self.card_list[self.current_card - 1]


# List of possible card ranks
ranks = ['2', '3', '4', '5', '6', '7', '8', '9',
         '10', 'J', 'Q', 'K', 'A']

# List of possible card suits
suits = ['clubs', 'diamonds', 'hearts', 'spades']


def card_to_string(card_number):

    r = card_number % 13
    s = card_number // 13

    return ranks[r] + " of " + suits[s]


def deal_hand(deck):
    hand = []

    # Loop 5 times to get 5 cards
    for _ in range(5):
        hand.append(deck.deal())  # deal one card and add to hand

    return hand


def display_hand(hand):
    print("\nYour hand:")

    # Go through each card and print with position number
    for i in range(len(hand)):
        print(f"{i + 1}: {card_to_string(hand[i])}")


def replace_cards(hand, deck):

    # Ask user for input
    user_input = input(
        "\nEnter card positions to replace or press Enter to keep all: "
    )

    # If user presses Enter, keep the same hand
    if user_input.strip() == "":
        return hand

    # Split input by commas into a list
    positions = user_input.split(",")

    # Go through each position entered
    for pos in positions:
        pos = int(pos.strip()) - 1

        if 0 <= pos < 5:
            # Replace that card with a new one from deck
            hand[pos] = deck.deal()

    return hand



def main():

    deck = Deck(52)

    hand = deal_hand(deck)
    display_hand(hand)

    hand = replace_cards(hand, deck)

    print("\nFinal hand:")
    display_hand(hand)


# Run the program
main()