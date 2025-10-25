import sys

from stats import get_character_occurrences, get_word_count, sort_character_occurrences


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents


def main():
    argv = sys.argv
    if len(argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = argv[1]
    book_text = get_book_text(book_path)
    num_words = get_word_count(book_text)
    character_occurrences = get_character_occurrences(book_text)
    sorted_character_occurrences = sort_character_occurrences(character_occurrences)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for sorted_character_occurrence in sorted_character_occurrences:
        char = sorted_character_occurrence["char"]
        if char.isalpha():
            num = sorted_character_occurrence["num"]
            print(f"{char}: {num}")
    print("============= END ===============")


main()
