def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    text = text.lower()
    char_counts = {}

    for char in text:
        if char.isalpha():  # Only count alphabetic characters
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1

    return char_counts


def generate_report(file_path, word_count, char_count):
    char_list = [{'char': char, 'num': num}
                 for char, num in char_count.items()]

    char_list.sort(key=lambda x: x['num'], reverse=True)

    # Print the report
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document")
    print()

    for item in char_list:
        print(f"The {item['char']} character was found {item['num']} times")

    print("--- End report ---")


def main():
    # Define the path to the file
    path_to_file = 'books/frankenstein.txt'

    # Open and read the file
    with open(path_to_file, 'r') as f:
        file_contents = f.read()

    # Count the number of words in the text file
    word_count = count_words(file_contents)

    # Count the number of characters in the text file
    char_count = count_characters(file_contents)

    generate_report(path_to_file, word_count, char_count)


main()
