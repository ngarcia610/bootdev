import sys
from stats import *

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
    text = get_book_text(book_path)

    num_words = count_words(text)
    char_counts = count_characters(text)
    sorted_chars = sort_characters(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_chars:
        char = item["char"]
        count = item["num"]

        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

main()