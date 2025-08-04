from stats import count_words, count_characters, sort_characters
import sys


def get_book_text(filepath):
    book_contents = ""
    with open(filepath) as f:
        book_contents = f.read()
    return book_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    num_words = count_words(book_text)
    num_characters = count_characters(book_text)
    sorted_characters = sort_characters(num_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_characters:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

main()
