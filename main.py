from stats import words
from stats import num_of_chars
from stats import sort_dict
import sys


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
    book = get_book_text(path)
    num_of_words = words(book)
    all_characters = num_of_chars(book)
    sorted_list = sort_dict(all_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        print(f"{item['character']}: {item['count']}")
    print("============= END ===============")

main()