from stats import get_num_words, get_sorted_char_list
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Missing Argument!")
        print("Usage: python3 main.py <path_to_book>.")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = get_num_words(book_text)
    char_count = get_sorted_char_list(book_text)

    print("============ BOOKBOT ============")
    print("Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for c in char_count:
        if not c["char"].isalpha():
            continue
        print(f"{c["char"]}: {c["num"]}")

    print("============= END ===============")

main()