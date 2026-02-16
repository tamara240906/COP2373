# List of 30 common spam words/phrases
SPAM_KEYWORDS = [
    "free", "winner", "congratulations", "urgent", "act now",
    "limited time", "click here", "claim now", "risk free", "guaranteed",
    "no obligation", "earn money", "make money", "work from home",
    "100% free", "special promotion", "exclusive deal", "call now",
    "apply now", "cheap", "credit card", "debt", "loan", "investment",
    "prize", "cash bonus", "offer expires", "buy now", "miracle", "lose weight"
]


def calculate_spam_score(message):
# Scans the message and returns spam score and a  list of triggered keywords

    score = 0
    triggered_words = []

    message = message.lower()

    for keyword in SPAM_KEYWORDS:
        occurrences = message.count(keyword)
        if occurrences > 0:
            score += occurrences
            triggered_words.append(keyword)

    return score, triggered_words


def rate_spam_likelihood(score):
# Returns spam Likelihood depending on the score
    if score == 0:
        return "Very unlikely to be spam"
    elif score <= 2:
        return "Unlikely to be spam"
    elif score <= 5:
        return "Possibly spam"
    elif score <= 10:
        return "Likely spam"
    else:
        return "Very likely spam"


def main():
    print("=== Spam Detection Program ===")
    message = input("Enter an email message:\n")

    score, triggered_words = calculate_spam_score(message)
    likelihood = rate_spam_likelihood(score)

# Display Results
    print("\n--- Results ---")
    print("Spam Score:", score)
    print("Likelihood:", likelihood)

    if triggered_words:
        print("Trigger Words Found:")
        for word in triggered_words:
            print("-", word)
    else:
        print("No spam keywords detected.")


# Run the program
main()