try:
    # Ask the user for the word they want to search for
    search_word = input("Enter the word you want to search for: ").strip().lower()

    with open('text.txt', 'r') as file:
        text = file.read().lower()  # Convert text to lowercase for case-insensitive search

    index = text.find(search_word)

    if index != -1:
        print(f'Found "{search_word}" at index {index}')
    else:
        print(f'"{search_word}" not found')

except FileNotFoundError:
    print("The file 'text.txt' does not exist.")
