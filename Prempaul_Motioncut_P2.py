def count_words(text):
    """
    Function to count the number of words in a given text.
    A word is defined as a sequence of characters separated by spaces.
    """
    words = text.split()  # Splitting text into words based on spaces
    return len(words)  # Returning the number of words

def main():
    """
    Main function to handle user input and display word count.
    """
    # User Input Handling  
    text = input("Enter a sentence or paragraph: ").strip()

    # Error Handling: Check for empty input
    if not text:
        print("Error: No input provided. Please enter some text.")
        return

    # Word Counting Logic  
    word_count = count_words(text)

    # Output Display  
    print(f"Word Count: {word_count}")g
    
# Ensuring code runs only when executed directly
if __name__ == "__main__":  
    main()