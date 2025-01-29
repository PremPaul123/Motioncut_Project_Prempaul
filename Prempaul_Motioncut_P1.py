import random
import string

# Step 1: Define default lists of adjectives and nouns
adjectives = ["Cool", "Happy", "Brave", "Silly", "Bright", "Lazy"]
nouns = ["Tiger", "Dragon", "Eagle", "Panda", "Shark", "Wizard"]

# Step 2: Function to validate non-empty lists
def validate_list(input_list, prompt):
    while not input_list:
        print("The list cannot be empty. Please provide valid inputs.")
        input_list = input(prompt).split(',')
        input_list = [word.strip().capitalize() for word in input_list]
    return input_list

# Step 3: Function to validate filename
def validate_filename(filename):
    invalid_chars = r'\/:*?"<>|'
    for char in invalid_chars:
        if char in filename:
            print(f"The filename cannot contain invalid characters: {invalid_chars}")
            return False
    return True

# Step 4: Function to generate a random username
def generate_username(include_numbers=True, include_special_chars=True, max_length=None):
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    username = adjective + noun

    # Add numbers if requested
    if include_numbers:
        username += str(random.randint(10, 99))

    # Add special characters if requested
    if include_special_chars:
        username += random.choice(string.punctuation)

    # Trim username if it exceeds max_length
    if max_length:
        if max_length < len(adjective) + len(noun):  # Ensure minimum length for adjective and noun
            raise ValueError("Maximum length is too short to accommodate an adjective and a noun.")
        username = username[:max_length]

    return username

# Step 5: Save usernames to a file
def save_usernames_to_file(usernames):
    filename = input("Enter the filename to save usernames (e.g., usernames.txt): ").strip()
    if not filename:
        filename = "usernames.txt"
    while not validate_filename(filename):  # Validate the filename
        filename = input("Enter a valid filename: ").strip()

    try:
        with open(filename, "a") as file:
            for username in usernames:
                file.write(username + "\n")
        print(f"Usernames saved to {filename}")
    except Exception as e:
        print(f"An error occurred while saving usernames: {e}")

# Step 6: Menu system for enhanced user experience
def main():
    global adjectives, nouns

    while True:
        print("\nWelcome to the Random Username Generator!")
        print("1. Generate Usernames")
        print("2. Customize Adjective List")
        print("3. Customize Noun List")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            try:
                usernames = []
                num_usernames = int(input("How many usernames would you like to generate? "))
                if num_usernames <= 0:  # Ensure a positive number of usernames
                    print("Please enter a positive number for usernames.")
                    continue

                include_numbers = input("Include numbers? (yes/no): ").strip().lower() == "yes"
                include_special_chars = input("Include special characters? (yes/no): ").strip().lower() == "yes"
                max_length = input("Enter the maximum length for usernames (or press Enter to skip): ")
                max_length = int(max_length) if max_length else None

                for _ in range(num_usernames):
                    username = generate_username(include_numbers, include_special_chars, max_length)
                    print("Generated Username:", username)
                    usernames.append(username)

                save_choice = input("Would you like to save these usernames to a file? (yes/no): ").strip().lower()
                if save_choice == "yes":
                    save_usernames_to_file(usernames)

            except ValueError as ve:
                print(f"Invalid input: {ve}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

        elif choice == "2":
            adjectives = input("Enter a list of adjectives separated by commas: ").split(',')
            adjectives = [adj.strip().capitalize() for adj in adjectives]
            adjectives = validate_list(adjectives, "Enter a list of adjectives separated by commas: ")

        elif choice == "3":
            nouns = input("Enter a list of nouns separated by commas: ").split(',')
            nouns = [noun.strip().capitalize() for noun in nouns]
            nouns = validate_list(nouns, "Enter a list of nouns separated by commas: ")

        elif choice == "4":
            print("Thank you for using the Random Username Generator. Goodbye!")
            break

        else:
            print("Invalid choice. Please select an option from the menu.")

if __name__ == "__main__":
    main()
