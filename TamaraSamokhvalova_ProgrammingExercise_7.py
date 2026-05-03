# Import regular expressions module
import re

# Function to extract sentences from a paragraph
def get_sentences(paragraph):
    # Regex pattern to find sentences
    pat = r'[A-Za-z0-9].*?[.!?](?=\s[A-Z0-9]|$)'

    # Find all matching sentences
    sentences = re.findall(pat, paragraph, flags=re.DOTALL | re.MULTILINE)

    return sentences


# Function to display sentences and count them
def display_sentences(sentences):
    # Print each sentence individually
    print("\nIndividual Sentences:\n")

    for i, sentence in enumerate(sentences, start=1):
        print(f"{i}. {sentence.strip()}")

    # Print total count
    print("\nTotal number of sentences:", len(sentences))


# Main function
def main():
    # Get paragraph input from user
    paragraph = input("Enter a paragraph: ")

    # Extract sentences
    sentences = get_sentences(paragraph)

    # Display results
    display_sentences(sentences)


# Run program
main()